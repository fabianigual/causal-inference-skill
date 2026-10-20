"""Diseño PSM sintético y diagnósticos; no estima impacto ni intervalos causales.

Logit, matching greedy 1:1 sin reemplazo, caliper 0.2 SD del logit en muestra inicial.
Sin pesos, clusters, restricciones exactas ni tratamiento multivaluado.
Ejecutar: python scripts/ejemplo_psm_diagnosticos.py --output-dir RUTA.
"""
from pathlib import Path
import argparse
import json
import sys
import numpy as np
import pandas as pd
import scipy
from scipy.special import expit
import statsmodels
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _check_data(data, columns):
    if not data.index.is_unique or data.empty:
        raise ValueError("Se requieren filas y un índice único por unidad.")
    if not np.isin(data["treated"], [0, 1]).all():
        raise ValueError("treated debe ser binario, sin faltantes.")
    if not np.isfinite(data[columns].to_numpy(dtype=float)).all():
        raise ValueError("Los valores del diseño deben ser finitos.")
    if any((data.treated == arm).sum() < 2 for arm in [0, 1]):
        raise ValueError("Se requieren al menos dos unidades en cada brazo.")


def greedy_pairs(data, score_col="logit_ps", caliper_sd=0.2, seed=42):
    """Matching 1:1 sin reemplazo. Orden tratado aleatorio; empates por orden control.

    Distancia absoluta en score_col; caliper_sd multiplica SD inicial (ddof=0).
    Con score constante, admite coincidencias exactas con umbral cero.
    Guarda IDs originales. No es matching óptimo ni el algoritmo de CausalML.
    """
    _check_data(data, [score_col])
    if not np.isfinite(caliper_sd) or caliper_sd <= 0:
        raise ValueError("caliper_sd debe ser finito y positivo.")
    score_sd = float(data[score_col].std(ddof=0))
    threshold = caliper_sd * score_sd
    rng = np.random.default_rng(seed)
    treated_ids = data.index[data.treated == 1].to_numpy().copy()
    rng.shuffle(treated_ids)
    available = list(data.index[data.treated == 0])
    records = []
    for treated_id in treated_ids:
        if not available:
            break
        distances = np.abs(data.loc[available, score_col].to_numpy()
                           - data.loc[treated_id, score_col])
        position = int(np.argmin(distances))
        if distances[position] <= threshold:
            control_id = available.pop(position)
            records.append({"pair_id": len(records), "treated_id": treated_id,
                            "control_id": control_id, "distance": float(distances[position]),
                            "caliper_absolute": threshold})
    return pd.DataFrame(records, columns=["pair_id", "treated_id", "control_id",
                                         "distance", "caliper_absolute"])


def balance_table(before, after, features):
    """Medias y SMD con denominador pooled pre fijo; solo filas sin pesos/reutilización.

    Variables categóricas requieren indicadores. Referencia constante genera NaN
    y una marca explícita, no un SMD cero inventado.
    """
    _check_data(before, features)
    _check_data(after, features)
    records = []
    for feature in features:
        pre_t, pre_c = [before.loc[before.treated == arm, feature] for arm in [1, 0]]
        post_t, post_c = [after.loc[after.treated == arm, feature] for arm in [1, 0]]
        reference = float(np.sqrt((pre_t.var(ddof=1) + pre_c.var(ddof=1)) / 2))
        records.append({"variable": feature, "mean_t_pre": float(pre_t.mean()),
                        "mean_c_pre": float(pre_c.mean()), "mean_t_post": float(post_t.mean()),
                        "mean_c_post": float(post_c.mean()), "sd_reference": reference,
                        "smd_pre": float((pre_t.mean() - pre_c.mean()) / reference)
                                   if reference > 0 else np.nan,
                        "smd_post": float((post_t.mean() - post_c.mean()) / reference)
                                    if reference > 0 else np.nan,
                        "reference_zero": reference == 0})
    return pd.DataFrame(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    root = args.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    features = ["x_continua", "x_binaria"]
    data = pd.DataFrame({"x_continua": rng.normal(size=1000),
                         "x_binaria": rng.binomial(1, 0.4, size=1000)})
    data.index.name = "unit_id"
    true_ps = expit(-0.9 + 1.1 * data.x_continua + 0.7 * data.x_binaria)
    data["treated"] = rng.binomial(1, true_ps)
    design_matrix = sm.add_constant(data[features], has_constant="add")
    fit = sm.Logit(data.treated, design_matrix).fit(disp=False)
    if not fit.mle_retvals["converged"]:
        raise RuntimeError("El logit no convergió; revisar separación y especificación.")
    data["logit_ps"] = design_matrix.to_numpy() @ np.asarray(fit.params)
    data["propensity"] = expit(data.logit_ps)
    pairs = greedy_pairs(data, seed=args.seed)
    if len(pairs) < 2:
        raise RuntimeError("Menos de dos pares; revisar soporte y diseño antes de continuar.")
    matched = data.loc[list(pairs.treated_id) + list(pairs.control_id)].copy()
    balance = balance_table(data, matched, features)
    data.to_csv(root / "diseno_sintetico.csv")
    matched.to_csv(root / "muestra_matched.csv")
    pairs.to_csv(root / "pares.csv", index=False)
    balance.to_csv(root / "balance.csv", index=False)
    (root / "balance.tex").write_text(balance.to_latex(index=False, float_format="%.3f",
        caption="Balance de covariables sintéticas: PSM greedy 1:1 sin reemplazo. "
                "SMD usa SD pooled previa fija, también para el indicador binario. "
                "El balance observado no demuestra ausencia de confusión no medida."), encoding="utf-8")
    plt.style.use(Path(__file__).resolve().parents[1] / "assets" / "paper.mplstyle")
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 7.7))
    positions = np.arange(len(features))
    axes[0, 0].scatter(balance.smd_pre.abs(), positions, color="#50758a", marker="o", label="Antes")
    axes[0, 0].scatter(balance.smd_post.abs(), positions, color="#222222", marker="s", label="Después")
    axes[0, 0].axvline(0.1, ls=":", color="0.6", label="Referencia 0.1")
    axes[0, 0].set(title="(a) Balance: Love plot", xlabel=r"$|SMD|$ (denominador pre fijo)",
                   yticks=positions, yticklabels=["Continua", "Binaria"], ylim=(-0.6, 1.6))
    axes[0, 0].legend(frameon=False, fontsize=9)
    for ax, frame, title in [(axes[0, 1], data, "(b) Propensión antes"),
                              (axes[1, 1], matched, "(d) Propensión después")]:
        for arm, color, label, style in [(0, "#50758a", "Control", "--"),
                                          (1, "#222222", "Tratado", "-")]:
            ax.hist(frame.loc[frame.treated == arm, "propensity"], bins=np.linspace(0, 1, 16),
                    density=True, histtype="step", color=color, linestyle=style, label=label)
        ax.set(title=title, xlabel="Propensión estimada", ylabel="Densidad", xlim=(0, 1))
        ax.legend(frameon=False, fontsize=9)
    axes[1, 0].hist(pairs.distance, bins=15, color="#50758a", edgecolor="white", lw=0.5)
    axes[1, 0].axvline(pairs.caliper_absolute.iloc[0], ls=":", color="#222222", label="Caliper")
    axes[1, 0].set(title="(c) Distancias de pares", xlabel="Distancia absoluta en logit", ylabel="Pares")
    axes[1, 0].legend(frameon=False, fontsize=9)
    n_treated = int(data.treated.sum())
    fig.subplots_adjust(left=0.09, right=0.98, top=0.94, bottom=0.22, wspace=0.30, hspace=0.55)
    fig.text(0.09, 0.04,
        f"Nota: diseño sintético, sin resultados posteriores. Tratados retenidos: {len(pairs)}/{n_treated} "
        f"({len(pairs)/n_treated:.1%}); excluidos: {n_treated-len(pairs)}.\n"
        "Matching greedy 1:1 sin reemplazo; caliper 0.2 SD inicial del logit (ddof=0).\n"
        "SMD: denominador pooled previo (ddof=1), fijo antes/después. 0.1 es orientativo.\n"
        "El soporte y el balance observado orientan el diseño; no demuestran identificación causal.",
        fontsize=9.5, va="bottom", linespacing=1.5)
    for extension in ["png", "svg"]:
        fig.savefig(root / f"psm_diagnosticos.{extension}")
    plt.close(fig)
    metadata = {"illustrative": True, "seed": args.seed, "n_original": len(data),
                "n_treated_original": n_treated, "n_pairs": len(pairs),
                "n_treated_excluded": n_treated - len(pairs),
                "n_control_unique": int(pairs.control_id.nunique()),
                "matching": "greedy 1:1, no replacement; randomized treated order",
                "caliper": "0.2 * initial logit SD, ddof=0",
                "caliper_absolute": float(pairs.caliper_absolute.iloc[0]),
                "smd_reference": "pooled pre-match SD, ddof=1, fixed; binary treated as indicator",
                "scope": "design diagnostics only; no outcome or causal effect inference",
                "versions": {"python": sys.version.split()[0], "numpy": np.__version__,
                             "pandas": pd.__version__, "scipy": scipy.__version__,
                             "statsmodels": statsmodels.__version__, "matplotlib": matplotlib.__version__}}
    (root / "metadatos.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    print(balance.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print(f"Pares: {len(pairs)}; tratados excluidos: {n_treated-len(pairs)}")


if __name__ == "__main__":
    main()
