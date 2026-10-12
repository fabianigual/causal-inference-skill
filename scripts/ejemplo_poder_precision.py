"""Muestra académica de planificación; parámetros ilustrativos, sin datos reales.

Dependencias: numpy, pandas, scipy, statsmodels, matplotlib, jinja2.
Versiones verificadas: ../requirements.txt; usar un entorno de trabajo.
Ejecutar: python ejemplo_poder_precision.py --output-dir RUTA
Escribe figura PNG/SVG, tabla CSV/LaTeX y metadatos en --output-dir.
"""
from pathlib import Path
import argparse
from importlib.metadata import version
import json
import sys
import numpy as np
import pandas as pd
import scipy
import statsmodels
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm
from formulas_basicas import (normal_half_width, normal_mde,
                             independent_t_sample_size, independent_t_power)


def main():
    parser = argparse.ArgumentParser(description="Muestra ilustrativa de poder y precisión")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="Carpeta de resultados; usar el espacio de trabajo del análisis")
    args = parser.parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    root = args.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=True)
    plt.style.use(skill_root / "assets" / "paper.mplstyle")
    alpha, target, sigma = 0.05, 0.80, 1.0
    effect_sizes = [0.10, 0.20, 0.30]
    sizes = np.arange(20, 1601, 4)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.3))
    colors = ["#222222", "#50758a", "#9a6237"]
    line_styles = ["-", "--", "-."]
    for d, color, style in zip(effect_sizes, colors, line_styles):
        values = np.array([independent_t_power(d, sigma, int(n), int(n), alpha)
                           for n in sizes])
        if not np.isfinite(values).all():
            raise RuntimeError("La rutina de poder produjo valores no finitos; revisar versiones.")
        axes[0].plot(sizes, values, color=color, linestyle=style, label=rf"$d={d:.2f}$")
    axes[0].axhline(target, color="0.65", lw=0.8, linestyle=":")
    axes[0].text(1530, 0.815, r"$1-\beta=0.80$", ha="right", va="bottom", color="0.35", fontsize=10)
    axes[0].set(title="(a) Poder de la prueba t bilateral", xlabel=r"Observaciones por brazo, $n$",
                ylabel=r"Poder, $1-\beta$", ylim=(0, 1.04), xlim=(0, 1600))
    axes[0].legend(loc="lower right", frameon=False)
    mde = [normal_mde(sigma, n, n, alpha, target) / sigma for n in sizes]
    half_width = [normal_half_width(sigma, n, n, alpha) / sigma for n in sizes]
    axes[1].plot(sizes, mde, color=colors[0], label="MDE para poder 0.80")
    axes[1].plot(sizes, half_width, color=colors[1], linestyle="--", label="Semiancho del IC 95%")
    axes[1].set(title="(b) MDE y precisión esperadas", xlabel=r"Observaciones por brazo, $n$",
                ylabel=r"Magnitud en unidades de $\sigma$", xlim=(0, 1600), ylim=(0, 0.95))
    axes[1].legend(loc="upper right", frameon=False)
    for ax in axes:
        ax.set_xticks([0, 400, 800, 1200, 1600])
        ax.grid(axis="y", color="0.9", linewidth=0.5)
        ax.set_axisbelow(True)
    fig.subplots_adjust(left=0.075, right=0.99, top=0.90, bottom=0.32, wspace=0.30)
    fig.text(0.075, 0.055,
             "Nota: planificación ilustrativa; dos brazos independientes, asignación 1:1 y varianza común.\n"
             r"$\alpha=0.05$. Panel (a): normalidad y cálculo t. Panel (b): aproximación normal, $\sigma$ supuesta."
             "\nLas curvas describen detección y precisión; requieren un argumento de identificación causal aparte.",
             fontsize=9.5, va="bottom", linespacing=1.45)
    fig.savefig(root / "poder_precision.png")
    fig.savefig(root / "poder_precision.svg")
    plt.close(fig)

    records = []
    for d in effect_sizes:
        result = independent_t_sample_size(delta=d, sigma=sigma, alpha=alpha, power=target)
        n = result["n_treated"]
        records.append({"d_supuesto": d, "n_por_brazo": n, "n_total": result["n_total"],
                        "poder_logrado": result["power_achieved"],
                        "semiancho_IC95_normal_sigma": normal_half_width(sigma, n, n, alpha)})
    table = pd.DataFrame(records)
    table.to_csv(root / "tabla_planificacion.csv", index=False)
    latex_table = table.rename(columns={"d_supuesto": r"$d$ supuesto",
        "n_por_brazo": r"$n$ por brazo", "n_total": r"$N$ total",
        "poder_logrado": "Poder", "semiancho_IC95_normal_sigma": r"Semiancho IC / $\sigma$"})
    (root / "tabla_planificacion.tex").write_text(latex_table.to_latex(index=False,
        float_format="%.3f", escape=False,
        caption="Planificación ilustrativa de dos brazos independientes (asignación 1:1). "
                "Tamaño calculado para prueba t bilateral, alpha 0.05 y poder 0.80; "
                "semiancho del IC por aproximación normal con varianza supuesta.",
        label="tab:planificacion"), encoding="utf-8")
    metadata = {"illustrative": True, "alpha": alpha, "target_power": target,
                "sigma_assumed": sigma, "allocation_ratio": 1.0,
                "power_method": "two-sample pooled t-test under normality; statsmodels; "
                                "noncentral-t SF identity fallback for invalid extreme-tail CDF",
                "precision_method": "normal planning approximation with assumed SD",
                "assumptions": ["independent observations", "equal variance", "no clusters",
                                "complete follow-up", "causal identification assessed separately"],
                "versions": {"python": sys.version.split()[0], "numpy": np.__version__,
                             "pandas": pd.__version__, "scipy": scipy.__version__,
                             "statsmodels": statsmodels.__version__, "matplotlib": matplotlib.__version__,
                             "jinja2": version("jinja2")},
                "normal_z_critical": float(norm.ppf(1 - alpha / 2))}
    (root / "metadatos_ejemplo.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(table.to_string(index=False, float_format=lambda x: f"{x:.4f}"))


if __name__ == "__main__":
    main()
