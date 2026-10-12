"""DiD 2x2 ilustrativo: panel completo, unidades independientes y dos grupos.

No admite clusters, adopción escalonada, pesos, pérdidas ni cortes repetidos.
Ejecutar desde el repositorio: python scripts/ejemplo_did.py --output-dir RUTA.
Simula poder, error tipo I y cobertura; exporta CSV, LaTeX, PNG, SVG y metadatos.
"""
from pathlib import Path
import argparse
import json
import sys
import numpy as np
import pandas as pd
import scipy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from formulas_basicas import welch_ci, normal_mde


def did_2x2_panel(pre, post, treated, alpha=0.05):
    """Diferencia de cambios e IC de Welch; una fila por unidad independiente.

    La dependencia temporal dentro de la unidad se incorpora al calcular cambios.
    El usuario debe justificar identificación e independencia entre unidades.
    """
    pre, post = np.asarray(pre, dtype=float), np.asarray(post, dtype=float)
    treated = np.asarray(treated)
    if (pre.ndim != 1 or post.shape != pre.shape or treated.shape != pre.shape
            or not np.isfinite(pre).all() or not np.isfinite(post).all()
            or not np.isin(treated, [0, 1]).all()):
        raise ValueError("Vectores alineados, finitos y tratamiento binario requeridos.")
    changes = post - pre
    result = welch_ci(changes[treated == 1], changes[treated == 0], alpha)
    result["method"] = "DiD 2x2 de panel; Welch sobre cambios de unidades independientes"
    return result


def synthetic_panel(rng, n_per_arm=80, rho=0.5, effect=0.30):
    """DGP normal con tendencias paralelas y efecto constante conocidos por construcción."""
    if (int(n_per_arm) != n_per_arm or n_per_arm < 2 or not -1 < rho < 1
            or not np.isfinite(effect)):
        raise ValueError("Tamaño entero >=2, -1<rho<1 y efecto finito requeridos.")
    treated = np.repeat([0, 1], int(n_per_arm))
    errors = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], treated.size)
    pre = 2 + 0.5 * treated + errors[:, 0]
    post = 2 + 0.5 * treated + 0.2 + effect * treated + errors[:, 1]
    return pd.DataFrame({"id": np.arange(treated.size), "treated": treated,
                         "pre": pre, "post": post})


def simulate_design(rng, reps, rho, effect, n_per_arm=80, alpha=0.05):
    """Repite DGP, estimación e IC previstos; MCSE para rechazo y cobertura."""
    if int(reps) != reps or reps < 2:
        raise ValueError("Se requieren al menos dos repeticiones enteras.")
    estimates, rejected, covered = [], [], []
    for _ in range(reps):
        data = synthetic_panel(rng, n_per_arm, rho, effect)
        result = did_2x2_panel(data.pre, data.post, data.treated, alpha)
        estimates.append(result["estimate"])
        rejected.append(result["ci_low"] > 0 or result["ci_high"] < 0)
        covered.append(result["ci_low"] <= effect <= result["ci_high"])
    rejection, coverage = float(np.mean(rejected)), float(np.mean(covered))
    return {"rho": rho, "effect": effect, "n_per_arm": n_per_arm, "reps": reps,
            "rejection_rate": rejection,
            "rejection_mcse": float(np.sqrt(rejection * (1 - rejection) / reps)),
            "coverage": coverage,
            "coverage_mcse": float(np.sqrt(coverage * (1 - coverage) / reps)),
            "bias": float(np.mean(estimates) - effect),
            "mde_normal_80": normal_mde(np.sqrt(2 * (1 - rho)), n_per_arm,
                                         n_per_arm, alpha, 0.80)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--reps", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.reps < 2:
        parser.error("--reps debe ser >= 2")
    root = args.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=True)
    plt.style.use(Path(__file__).resolve().parents[1] / "assets" / "paper.mplstyle")
    rng = np.random.default_rng(args.seed)
    data = synthetic_panel(rng)
    result = did_2x2_panel(data.pre, data.post, data.treated)
    data.to_csv(root / "panel_sintetico.csv", index=False)
    pd.DataFrame([result]).to_csv(root / "estimacion.csv", index=False)
    records = [simulate_design(rng, args.reps, rho, effect)
               for rho in [0.0, 0.5, 0.8] for effect in [0.0, 0.3]]
    table = pd.DataFrame(records)
    table.to_csv(root / "simulacion.csv", index=False)
    (root / "simulacion.tex").write_text(table.to_latex(index=False, float_format="%.3f",
        caption="DiD sintético 2x2: unidades independientes, SD por período 1, alpha 0.05. "
                "Rechazo bajo efecto cero: error tipo I; bajo efecto 0.3: poder. "
                "MCSE: error Monte Carlo. MDE normal aproximado para poder 0.80."),
        encoding="utf-8")
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))
    means = data.groupby("treated")[["pre", "post"]].mean()
    axes[0].plot([0, 1], means.loc[0], "o--", color="#50758a", label="Control")
    axes[0].plot([0, 1], means.loc[1], "s-", color="#222222", label="Tratado")
    counterfactual = means.loc[1, "pre"] + means.loc[0, "post"] - means.loc[0, "pre"]
    axes[0].plot([0, 1], [means.loc[1, "pre"], counterfactual], ":",
                 color="#9a6237", label="Proyección paralela")
    axes[0].set(title="(a) Medias y contraste DiD", ylabel="Resultado (unidades)",
                xticks=[0, 1], xticklabels=["Pre", "Post"])
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    for effect, label, marker, color in [(0, "Error tipo I", "o", "#50758a"),
                                        (0.3, "Poder: efecto 0.30", "s", "#222222")]:
        rows = table[table.effect == effect]
        axes[1].errorbar(rows.rho, rows.rejection_rate, yerr=1.96 * rows.rejection_mcse,
                         fmt=marker + "--", color=color, capsize=3, label=label)
    axes[1].axhline(0.05, ls=":", color="0.65", lw=0.8)
    axes[1].set(title="(b) Detección según correlación", xlabel=r"Correlación pre–post, $\rho$",
                ylabel="Probabilidad de rechazo", ylim=(0, 1), xticks=[0, 0.5, 0.8])
    axes[1].legend(loc="upper left", frameon=False, fontsize=9)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.90, bottom=0.31, wspace=0.32)
    fig.text(0.08, 0.05,
        f"Nota: datos sintéticos; 80 unidades independientes por brazo. DiD estimado: {result['estimate']:.3f}; "
        f"IC 95% [{result['ci_low']:.3f}, {result['ci_high']:.3f}].\n"
        "IC de Welch sobre cambios. Panel (b): barras de ±1.96 MCSE de tasas simuladas.\n"
        "Las tendencias paralelas se impusieron en la simulación; la figura no las demuestra en datos reales.",
        fontsize=9, va="bottom", linespacing=1.5)
    for extension in ["png", "svg"]:
        fig.savefig(root / f"did.{extension}")
    plt.close(fig)
    metadata = {"illustrative": True, "seed": args.seed, "reps": args.reps,
                "design": "balanced 2x2 panel; independent units; Gaussian period errors",
                "true_effect": 0.3, "alpha": 0.05,
                "limits": ["no clusters", "no staggered adoption", "no missing data",
                           "parallel trends imposed, not tested", "no unmeasured bias modeled"],
                "versions": {"python": sys.version.split()[0], "numpy": np.__version__,
                             "pandas": pd.__version__, "scipy": scipy.__version__,
                             "matplotlib": matplotlib.__version__}}
    (root / "metadatos.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    print(table.to_string(index=False, float_format=lambda x: f"{x:.3f}"))


if __name__ == "__main__":
    main()
