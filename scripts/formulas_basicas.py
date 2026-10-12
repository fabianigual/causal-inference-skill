"""Cálculos iniciales de planificación e inferencia; no validan identificación causal.

Dependencias: numpy, scipy, statsmodels. Condiciones de cada función en su docstring.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.stats import norm, t, nct
from statsmodels.stats.power import TTestIndPower


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} debe ser finito y positivo.")
    return value


def _probability(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or not 0 < value < 1:
        raise ValueError(f"{name} debe estar estrictamente entre 0 y 1.")
    return value


def welch_ci(treated, control, alpha: float = 0.05) -> dict:
    """IC bilateral aproximado para medias de dos muestras independientes.

    Admite varianzas distintas. No admite clusters, parejas ni datos repetidos.
    Requiere varianza finita y condiciones para la aproximación de Welch.
    Las muestras no establecen por sí solas la interpretación causal.
    """
    alpha = _probability(alpha, "alpha")
    x, y = np.asarray(treated, dtype=float), np.asarray(control, dtype=float)
    if any(a.ndim != 1 or a.size < 2 or not np.isfinite(a).all() for a in (x, y)):
        raise ValueError("Se requieren dos vectores finitos con al menos dos observaciones.")
    vx, vy = float(x.var(ddof=1)), float(y.var(ddof=1))
    ax, ay = vx / x.size, vy / y.size
    if ax + ay <= 0:
        raise ValueError("No se puede construir el IC de Welch con varianza total cero.")
    se = math.sqrt(ax + ay)
    df = (ax + ay) ** 2 / (ax ** 2 / (x.size - 1) + ay ** 2 / (y.size - 1))
    estimate = float(x.mean() - y.mean())
    half = float(t.ppf(1 - alpha / 2, df)) * se
    return {"estimate": estimate, "se": se, "df": df,
            "ci_low": estimate - half, "ci_high": estimate + half,
            "confidence": 1 - alpha, "n_treated": int(x.size), "n_control": int(y.size),
            "method": "Welch; muestras independientes; IC bilateral aproximado"}


def normal_half_width(sigma: float, n_treated: float, n_control: float,
                      alpha: float = 0.05) -> float:
    """Semiancho de planificación: normal, brazos independientes, SD común supuesta."""
    sigma = _positive(sigma, "sigma")
    n1, n0 = _positive(n_treated, "n_treated"), _positive(n_control, "n_control")
    alpha = _probability(alpha, "alpha")
    return float(norm.ppf(1 - alpha / 2) * sigma * math.sqrt(1 / n1 + 1 / n0))


def normal_mde(sigma: float, n_treated: float, n_control: float,
               alpha: float = 0.05, power: float = 0.80) -> float:
    """MDE aproximado bilateral: normal, independencia y SD común supuesta."""
    sigma = _positive(sigma, "sigma")
    n1, n0 = _positive(n_treated, "n_treated"), _positive(n_control, "n_control")
    alpha, power = _probability(alpha, "alpha"), _probability(power, "power")
    if power <= 0.5 or power <= alpha:
        raise ValueError("Esta aproximación de MDE requiere poder mayor a 0.5 y a alpha.")
    return float((norm.ppf(1 - alpha / 2) + norm.ppf(power)) * sigma
                 * math.sqrt(1 / n1 + 1 / n0))


def independent_t_power(delta: float, sigma: float, n_treated: int,
                        n_control: int, alpha: float = 0.05) -> float:
    """Poder t bilateral: normalidad, independencia y varianza común.

    delta es un efecto alternativo supuesto, nunca un resultado estimado usado
    para justificar poder retrospectivo. No incorpora clusters ni pérdidas.
    """
    delta, sigma = abs(float(delta)), _positive(sigma, "sigma")
    if not math.isfinite(delta):
        raise ValueError("delta debe ser finito.")
    alpha = _probability(alpha, "alpha")
    for value in (n_treated, n_control):
        if int(value) != value or value < 2:
            raise ValueError("Cada brazo requiere un tamaño entero de al menos dos.")
    result = float(TTestIndPower().power(delta / sigma, n_treated, alpha,
                                        ratio=n_control / n_treated, alternative="two-sided"))
    if not math.isfinite(result):
        # En algunas versiones, CDF de la cola izquierda extrema devuelve NaN.
        # SF es finita en ese caso. Usar la identidad CDF=1-SF conserva el
        # cálculo t no central, sin reemplazarlo por una aproximación normal.
        df = n_treated + n_control - 2
        noncentrality = delta / sigma * math.sqrt(n_treated * n_control
                                                  / (n_treated + n_control))
        critical = float(t.ppf(1 - alpha / 2, df))
        result = float(nct.sf(critical, df, noncentrality)
                       + (1 - nct.sf(-critical, df, noncentrality)))
    if not math.isfinite(result) or not -1e-12 <= result <= 1 + 1e-12:
        raise RuntimeError("La rutina de poder devolvió un resultado inválido; revisar dependencias.")
    return min(1.0, max(0.0, result))


def independent_t_sample_size(delta: float, sigma: float, alpha: float = 0.05,
                              power: float = 0.80, ratio: float = 1.0) -> dict:
    """Tamaño para prueba t bilateral independiente con varianza común.

    ratio es n_control/n_treated. Redondea hacia arriba y recalcula el poder
    con la asignación entera resultante. No incorpora clusters ni pérdidas.
    """
    delta, sigma = _positive(abs(delta), "abs(delta)"), _positive(sigma, "sigma")
    alpha, power = _probability(alpha, "alpha"), _probability(power, "power")
    ratio = _positive(ratio, "ratio")
    if power <= alpha:
        raise ValueError("El poder objetivo debe superar alpha.")
    continuous = float(TTestIndPower().solve_power(effect_size=delta / sigma,
                       nobs1=None, alpha=alpha, power=power, ratio=ratio,
                       alternative="two-sided"))
    if not math.isfinite(continuous):
        raise RuntimeError("El cálculo de tamaño no convergió a un resultado finito.")
    n1 = max(2, math.ceil(continuous))
    n0 = max(2, math.ceil(n1 * ratio))
    return {"n_treated": n1, "n_control": n0, "n_total": n1 + n0,
            "power_achieved": independent_t_power(delta, sigma, n1, n0, alpha),
            "target_power": power, "alpha": alpha, "delta_assumed": delta,
            "sigma_assumed": sigma, "requested_ratio": ratio}


def equal_cluster_design_effect(m: float, icc: float) -> float:
    """DE simple: clusters de igual tamaño y correlación intercambiable.

    No valida inferencia con pocos clusters ni da sus grados de libertad.
    """
    m = _positive(m, "m")
    icc = float(icc)
    if m < 1 or not math.isfinite(icc) or not 0 <= icc <= 1:
        raise ValueError("m debe ser >= 1 e ICC debe estar entre 0 y 1.")
    return 1 + (m - 1) * icc
