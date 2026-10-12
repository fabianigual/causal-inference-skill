# Referencias para mantener el contenido

- Hernán y Robins: [Causal Inference: What If](https://miguelhernan.org/whatifbook), fundamento general de estimandos, identificación y temporalidad.
- Hernán y Robins (2016): [Using Big Data to Emulate a Target Trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), organización de tratamientos, elegibilidad y seguimiento.
- Callaway y Sant'Anna: [Difference-in-Differences with Multiple Time Periods](https://psantanna.com/files/Callaway_SantAnna_2020.pdf), estimandos y comparaciones en DiD.
- Roth (2022): [Pretest with Caution](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf), límites de los pretests de tendencias.
- Cattaneo, Idrobo y Titiunik: [A Practical Introduction to RD Designs](https://mdcattaneo.github.io/books/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf), identificación, inferencia y falsificación en RD.
- [statsmodels: poder para dos muestras](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html) y [IC de Welch](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.CompareMeans.tconfint_diff.html).
- [Estudio de ICC, desequilibrio y poder en ensayos por clusters](https://pmc.ncbi.nlm.nih.gov/articles/PMC2747741/), condiciones de la corrección simple.
- Matplotlib: [Mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html) y [renderizado con LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html).
- OpenAI Docs: [estructura de skills](https://learn.chatgpt.com/docs/build-skills) y [evaluación de comportamiento](https://developers.openai.com/blog/eval-skills).

- CausalML: [repositorio de Uber](https://github.com/uber/causalml), [metodología](https://causalml.readthedocs.io/en/stable/methodology.html), [API](https://causalml.readthedocs.io/en/stable/causalml.html), [quickstart](https://causalml.readthedocs.io/en/stable/quickstart.html) y [validación](https://causalml.readthedocs.io/en/stable/validation.html).
- CausalML: [T-learner, código fuente documentado](https://causalml.readthedocs.io/en/stable/_modules/causalml/inference/meta/tlearner.html), [métricas y estilos](https://causalml.readthedocs.io/en/stable/_modules/causalml/metrics/visualize.html) e [instalación](https://causalml.readthedocs.io/en/stable/installation.html). Verificar condiciones y API de la versión elegida.

## DiD y PSM: referencias específicas

1. Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics, 225*(2), 175–199. [DOI: 10.1016/j.jeconom.2020.09.006](https://doi.org/10.1016/j.jeconom.2020.09.006).
2. Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *The Review of Economic Studies, 90*(5), 2555–2591. [DOI: 10.1093/restud/rdad018](https://doi.org/10.1093/restud/rdad018). [Texto de los autores](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf).
3. Roth, J., Sant’Anna, P. H. C., Bilinski, A., & Poe, J. (2023). *What’s trending in difference-in-differences? A synthesis of the recent econometrics literature*. [Manuscrito de los autores, arXiv:2201.01194v3](https://arxiv.org/abs/2201.01194v3).
4. Sant’Anna, P. H. C., & Zhao, J. (2020). Doubly robust difference-in-differences estimators. *Journal of Econometrics, 219*(1), 101–122. [DOI: 10.1016/j.jeconom.2020.06.003](https://doi.org/10.1016/j.jeconom.2020.06.003). [Versión de los autores](https://psantanna.com/files/SantAnna_Zhao_DRDID.pdf).
5. Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika, 70*(1), 41–55. [DOI: 10.1093/biomet/70.1.41](https://doi.org/10.1093/biomet/70.1.41).
6. Austin, P. C. (2009). Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples. *Statistics in Medicine, 28*(25), 3083–3107. [DOI: 10.1002/sim.3697](https://doi.org/10.1002/sim.3697). [Texto completo](https://pmc.ncbi.nlm.nih.gov/articles/PMC3472075/).
7. Abadie, A., & Imbens, G. W. (2008). On the failure of the bootstrap for matching estimators. *Econometrica, 76*(6), 1537–1557. [DOI: 10.3982/ECTA6474](https://doi.org/10.3982/ECTA6474).
8. Abadie, A., & Imbens, G. W. (2016). Matching on the estimated propensity score. *Econometrica, 84*(2), 781–807. [DOI: 10.3982/ECTA11293](https://doi.org/10.3982/ECTA11293).
9. Rosenbaum, P. R. (1987). Sensitivity analysis for certain permutation inferences in matched observational studies. *Biometrika, 74*(1), 13–26. [DOI: 10.1093/biomet/74.1.13](https://doi.org/10.1093/biomet/74.1.13).
10. King, G., & Nielsen, R. (2019). Why propensity scores should not be used for matching. *Political Analysis, 27*(4), 435–454. [Publicación y materiales de los autores](https://gking.harvard.edu/publication/why-propensity-scores-should-not-be-used-for-matching/).

### Software y ejemplos

- `differences`: [repositorio](https://github.com/bernardodionisi/differences), [constructor ATTgt](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.__init__/), [fit](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.fit/) y [aggregate](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.aggregate/). Dependencia opcional para análisis que la requieran.
- [HonestDiD oficial](https://github.com/asheshrambachan/HonestDiD): implementación y ejemplos de sensibilidad en R, con enlace a Stata. No atribuirle una API Python verificada.
- [CausalML matching: código documentado](https://causalml.readthedocs.io/en/stable/_modules/causalml/match.html): matching, escala de caliper y definición de balance.

Consultadas el 12 de octubre de 2026. Los ejemplos de API de `differences` y matching de CausalML fueron contrastados con documentación; requieren validación en el entorno del análisis. Los dos ejemplos sintéticos autocontenidos se ejecutaron con las dependencias básicas.
