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

Las fuentes de los ejemplos de API de `differences` y matching de CausalML se contrastaron con documentación el 12 de octubre de 2026; sus integraciones requieren validación en el entorno del análisis. Consulta [resultados de validación](validacion-resultados.md) para las ejecuciones y versiones de los ejemplos autocontenidos.

## Ajuste, selección y otros diseños

- Daw, J. R., & Hatfield, L. A. (2018). [Matching and Regression to the Mean in Difference-in-Differences Analysis](https://onlinelibrary.wiley.com/doi/10.1111/1475-6773.12993). Riesgos de emparejar resultados previos ruidosos en DiD.
- Imbens, G. W., & Angrist, J. D. (1994). [Identification and Estimation of Local Average Treatment Effects](https://www.nber.org/papers/t0118). Población local y supuestos para LATE.
- Angrist, J. D., Imbens, G. W., & Rubin, D. B. [Identification of Causal Effects Using Instrumental Variables](https://www.nber.org/papers/t0136). Marco de resultados potenciales para IV; versión de trabajo de 1993, publicada en 1996.
- Lee, D. S., McCrary, J., Moreira, M. J., & Porter, J. (2022). [Valid t-Ratio Inference for IV](https://www.nber.org/papers/w29124). Límites de inferencia convencional y fuerza del instrumento.
- Cattaneo, M. D., Titiunik, R., & Vazquez-Bare, G. (2020). [The Regression Discontinuity Design](https://mdcattaneo.github.io/papers/Cattaneo-Titiunik-VazquezBare_2020_Sage.pdf). Identificación, estimación, sesgo e inferencia local.
- Chernozhukov et al. (2018). [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://www.nber.org/papers/w23564). Scores ortogonales, cross-fitting y condiciones de inferencia.
- Lee, D. S. (2009). [Training, Wages, and Sample Selection: Estimating Sharp Bounds on Treatment Effects](https://www.nber.org/papers/w11721). Cotas bajo selección monotónica y población de interés.
- Lin, W. (2013). [Agnostic Notes on Regression Adjustments to Experimental Data: Reexamining Freedman's Critique](https://doi.org/10.1214/12-AOAS583). Ajuste basal e inferencia en experimentos.
- Athey, S., & Wager, S. (2021). [Policy Learning with Observational Data](https://onlinelibrary.wiley.com/doi/10.3982/ECTA15732). Aprendizaje y evaluación de reglas de tratamiento.

Referencias incorporadas en la revisión metodológica del 20 de octubre de 2026. Los enlaces a NBER pueden llevar a la versión de trabajo del artículo citado. Para selección y tratamientos longitudinales, consulta también el libro de Hernán y Robins incluido al inicio.
