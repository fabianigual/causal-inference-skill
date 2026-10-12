# causal-inference

Una skill para Codex, pensada para inferencia causal y evaluación de impacto.

La idea es que funcione como un asesor y una guía para hacer buena inferencia causal en escenarios reales, con todos los problemas que eso conlleva. Busco que sea técnica, que conozca los supuestos, detecte puntos de atención y use visualizaciones ad hoc al problema.

El foco está en la **identificación causal**: qué efecto quiero estimar, para quién, qué comparación permite aprender sobre ese efecto y bajo qué supuestos. A partir de eso, incorpora cálculo de poder, efecto mínimo detectable, intervalos de confianza y análisis de sensibilidad. También incluye un set de fórmulas, partiendo con las básicas, y recursos en Python para trabajar con tablas y gráficos con un estilo visual cercano al de LaTeX usado en papers.

## Para qué sirve

- Diseñar una evaluación antes de implementar una intervención.
- Revisar qué puede identificarse con los datos disponibles y qué información falta.
- Examinar un análisis existente: estimando, supuestos, covariables, dependencia e interpretación.
- Planificar muestra, poder y precisión, considerando las características del diseño.
- Explorar heterogeneidad del efecto y modelos de uplift con CausalML cuando corresponda.
- Preparar resultados reproducibles en Python, con tablas, gráficos y referencias metodológicas.

Puede orientar problemas experimentales y observacionales, diferencias en diferencias, propensity score matching, regresión discontinua y estrategias con variables instrumentales. DiD y PSM cuentan con guías específicas. Los scripts incluyen poder e inferencia básicos, un DiD sintético 2×2 y diagnósticos PSM; los diseños más complejos requieren un procedimiento adecuado al caso.

## Cómo está pensada

La identificación organiza el trabajo. La pregunta y el mecanismo de asignación llevan al estimando; el estimando y el diseño llevan a los supuestos, al estimador y a la forma de calcular la incertidumbre. Las recomendaciones deben explicar qué decisión mejora la evidencia y qué queda pendiente.

La base conceptual toma como referencia a [Hernán y Robins (2020)](https://miguelhernan.org/whatifbook). Cuando ayuda a ordenar temporalidad, elegibilidad, asignación y seguimiento, utiliza el marco de ensayo objetivo de [Hernán y Robins (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/).

La skill pone atención a problemas frecuentes: confusión no medida, ajuste por variables posteriores al tratamiento, falta de soporte, pérdidas de seguimiento, interferencia, anticipación, cambios en medición y dependencia entre observaciones. Cada alerta debe conectar el hallazgo con su consecuencia y una acción concreta.

Para diferencias en diferencias, considera el calendario de adopción y las comparaciones entre cohortes, siguiendo a [Callaway y Sant’Anna (2021)](https://doi.org/10.1016/j.jeconom.2020.12.001). También distingue un diagnóstico de pre-tendencias de una justificación del supuesto: un pretest puede tener poca potencia y condicionar el análisis a su resultado puede distorsionar la inferencia, como muestra [Roth (2022)](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf).

En regresión discontinua, considera el efecto en el umbral, el soporte y los diagnósticos pertinentes al marco elegido, con [Cattaneo, Idrobo y Titiunik (2020)](https://doi.org/10.1017/9781108684606) como referencia.

Para poder e intervalos, relaciona los cálculos con la muestra, la asignación y la dependencia. La precisión estadística y la identificación son preguntas distintas: un intervalo estrecho puede coexistir con sesgo, y un resultado no significativo puede admitir efectos relevantes.

## DiD y propensity score matching

La [guía DiD](references/did.md) profundiza identificación, calendario y anticipación, tendencias paralelas, elección de controles, adopción escalonada, ATT por cohorte y período, event studies, pocos clusters, sensibilidad, poder e intervalos. Considera los problemas de los event studies convencionales con heterogeneidad descritos por [Sun y Abraham (2021)](https://doi.org/10.1016/j.jeconom.2020.09.006) y la sensibilidad propuesta por [Rambachan y Roth (2023)](https://doi.org/10.1093/restud/rdad018).

La [guía PSM](references/psm.md) profundiza selección sobre observables, ATT y ATE, soporte, covariables basales, calipers, reemplazo, ratio, balance, población retenida e inferencia. Parte del papel de la propensión de [Rosenbaum y Rubin (1983)](https://doi.org/10.1093/biomet/70.1.41) y revisa las dificultades del bootstrap ordinario y de la propensión estimada con [Abadie e Imbens (2008)](https://doi.org/10.3982/ECTA6474) y [Abadie e Imbens (2016)](https://doi.org/10.3982/ECTA11293).

La idea es que indique cómo tomar decisiones en un problema real: qué comparación puede defenderse, qué población representa el efecto y qué puntos de atención quedan abiertos. Las dos guías incluyen fórmulas, propuestas de tablas y gráficos, planificación y sensibilidad. También explican cómo combinar matching y DiD sin asumir que un método resuelve automáticamente los supuestos del otro.

## CausalML

La skill incorpora una [guía de uso de CausalML](references/causalml.md), la biblioteca de Python presentada por [Chen et al. (2020)](https://arxiv.org/abs/2002.11631).

Incluye criterios para elegir meta-learners y árboles o bosques causales/uplift, revisar propensión y soporte, separar entrenamiento de evaluación y considerar incertidumbre. El foco es estimar y evaluar efectos heterogéneos bajo un argumento de identificación explícito.

La guía distingue CATE de efecto individual, y ranking de calibración e inferencia. También revisa el uso de Qini/AUUC fuera de muestra y detalles de la API que pueden afectar la interpretación. Las firmas y capacidades deben comprobarse en la [documentación oficial de la versión utilizada](https://causalml.readthedocs.io/en/stable/causalml.html).

## Instalación

1. Descarga o clona este repositorio.
2. Copia la carpeta que contiene `SKILL.md`, junto con sus recursos, en `~/.agents/skills/causal-inference/`. Crea los directorios si hace falta. Si ya tienes la skill instalada, actualiza esa instalación.
3. Abre Codex y escribe `$causal-inference` seguido de tu pregunta o problema.

Codex detecta las skills locales automáticamente; si no aparece, reinicia Codex. Consulta la [documentación oficial de instalación y uso](https://learn.chatgpt.com/docs/build-skills).

Para ejecutar los ejemplos Python, instala sus dependencias según la sección de ejemplos ejecutables.

## Ejemplos de uso

Cuando la skill esté registrada en Codex, puedes invocarla con `$causal-inference` y describir el problema. Conviene incluir lo que sabes sobre asignación, unidades, fechas, resultado y datos disponibles; la skill debe ayudarte a precisar lo demás.

### 1. Revisar identificación en un programa real

```text
$causal-inference

Quiero evaluar un programa de capacitación que se implementó en distintos
municipios en tres etapas. Tengo datos anuales de empleo antes y después,
y la participación dependió de cupos y decisiones de cada municipio.

Ayúdame a precisar el estimando y a reconstruir el mecanismo de asignación.
Indica qué estrategia de identificación sería defendible, qué supuestos
necesita, los principales puntos de atención y qué datos adicionales pedirías.
Propón gráficos que ayuden a revisar el diseño y la comparabilidad.
```

### 2. Planificar poder y precisión

```text
$causal-inference

Estoy diseñando una evaluación con asignación por centro. Tengo presupuesto
para 24 centros y aproximadamente 80 personas por centro, con asignación 1:1.
Me interesa detectar un efecto de 0,20 desviaciones estándar sobre un resultado
continuo, con significación de 5% y poder de 80%.

La ICC es incierta: considera escenarios entre 0,02 y 0,08, y pérdidas de 10%.
Revisa qué puede detectar el diseño, explica las aproximaciones y cuándo
convendría simular el análisis previsto. Genera una tabla de escenarios y
gráficos de poder, MDE y precisión en Python, con estilo de paper.
```

### 3. Explorar heterogeneidad con CausalML

```text
$causal-inference

Tengo datos de un experimento con tratamiento binario y un resultado continuo.
Quiero explorar si el efecto cambia según covariables medidas antes de la
asignación. Las observaciones son independientes y tengo seguimiento completo.

Ayúdame a elegir una base simple y un estimador de CausalML para comparar.
Define las particiones, el preprocesamiento y la evaluación fuera de muestra.
Explica cómo interpretar el CATE y evaluar subgrupos e incertidumbre.
Prepara tablas y gráficos útiles, con los supuestos y límites de cada resultado.
```

### 4. Diseñar y revisar un PSM

```text
$causal-inference

Quiero evaluar una capacitación voluntaria con datos de participantes y
no participantes. Tengo edad, educación, empleo e ingresos medidos antes
del programa, y empleo un año después. Propongo propensity score matching.

Revisa qué ATT sería identificable y qué factores de selección pueden faltar.
Ayúdame a definir covariables, caliper, ratio y reemplazo. Compara balance y
soporte antes y después; muestra quiénes quedan fuera y cómo cambia la población.
Propón un procedimiento defendible para intervalos, poder y sensibilidad.
Genera Love plots y tablas con estilo de paper. Si sirve CausalML, revisa su API.
```

Los casos son ilustrativos. Las decisiones y los resultados de un análisis concreto dependen de su diseño y de la evidencia disponible.

## Ejemplos ejecutables en Python

Con las dependencias básicas instaladas, desde la raíz de este repositorio:

```bash
python scripts/ejemplo_poder_precision.py --output-dir outputs/demo-poder
python scripts/ejemplo_did.py --output-dir outputs/demo-did --reps 1000
python scripts/ejemplo_psm_diagnosticos.py --output-dir outputs/demo-psm
```

El primer ejemplo genera curvas de poder, MDE y precisión para dos brazos independientes. El segundo estima DiD 2×2 sobre cambios de un panel sintético y simula poder, error tipo I y cobertura. El tercero muestra matching greedy 1:1, conserva pares y produce balance, soporte, distancias y retención; ilustra el diseño sin estimar un impacto. Exportan CSV, tablas LaTeX, PNG/SVG y metadatos. Las muestras son sintéticas y las condiciones de cada ejemplo están documentadas.

[`requirements.txt`](requirements.txt) registra las versiones verificadas para los ejemplos básicos en Python 3.12. [`requirements-did.txt`](requirements-did.txt) declara `differences` para ATT por cohorte–período y [`requirements-causalml.txt`](requirements-causalml.txt) declara CausalML como recursos opcionales; sus instalaciones deben resolverse en un entorno compatible del análisis, sin combinar automáticamente estos recursos con los pins básicos. Los esquemas de API de esas bibliotecas se contrastaron con documentación; los nuevos ejemplos autocontenidos sí se ejecutaron y revisaron. Los entornos, datos y resultados se guardan fuera de los recursos de la skill.

## Qué contiene el repositorio

| Archivo o carpeta | Para qué sirve |
|---|---|
| [`SKILL.md`](SKILL.md) | Instrucciones y criterios que guían al asesor |
| [`references/identificacion.md`](references/identificacion.md) | Identificación, temporalidad y amenazas |
| [`references/did.md`](references/did.md) | DiD: identificación, estimadores, inferencia, poder y sensibilidad |
| [`references/psm.md`](references/psm.md) | PSM: diseño, soporte, balance, matching, inferencia y sensibilidad |
| [`references/poder-inferencia.md`](references/poder-inferencia.md) | Poder, precisión, intervalos y simulación |
| [`references/formulas.md`](references/formulas.md) | Fórmulas, notación y condiciones de uso |
| [`references/causalml.md`](references/causalml.md) | Selección, uso y evaluación con CausalML |
| [`references/python-visualizacion.md`](references/python-visualizacion.md) | Tablas y gráficos académicos en Python |
| [`references/validacion.md`](references/validacion.md) | Casos para revisar el comportamiento de la skill |
| [`references/fuentes.md`](references/fuentes.md) | Fuentes metodológicas y documentación técnica |
| [`scripts/`](scripts/) | Cálculos básicos y ejemplos reproducibles de poder, DiD y PSM |
| [`assets/paper.mplstyle`](assets/paper.mplstyle) | Estilo visual para Matplotlib |
| [`agents/openai.yaml`](agents/openai.yaml) | Nombre y descripción para la interfaz |

El `.gitignore` excluye entornos, caches, archivos locales, configuración de entorno y las carpetas de datos y resultados. Conserva el código, las referencias y los assets; no excluye de manera general extensiones como CSV, JSON, PNG, SVG o TEX.

## TODOs

La idea es seguir profundizando la skill con tareas verificables: qué recurso se entregará, qué problema resolverá y cómo se comprobará. El foco sigue siendo la identificación causal y las decisiones que permiten hacer una evaluación defendible en escenarios reales.

### Prioridad alta

- [ ] Ejecutar los casos de validación existentes y evaluar identificación, supuestos, elección del estimador, inferencia y recomendaciones prácticas.
- [ ] Incluir casos donde corresponda limitar la conclusión causal o solicitar información decisiva.
- [ ] Ejecutar las integraciones con `differences` y CausalML en entornos reproducibles, registrando versiones y resultados.
- [ ] Añadir un ejemplo completo de DiD con adopción escalonada: ATT por cohorte y período, agregación, event study e incertidumbre.
- [ ] Añadir un ejemplo completo de PSM con estimación del efecto e intervalos respaldados para el algoritmo elegido, documentando exclusiones, pesos y reutilización.
- [ ] Desarrollar un caso completo de **test A/B para diseño de productos**, por ejemplo una variante de onboarding: definir la hipótesis, población elegible, unidad de asignación, efecto de asignación (ITT), métrica principal y métricas de resguardo; planificar poder, MDE, tamaño de muestra y duración; analizar efectos absolutos y relativos con intervalos y traducir los resultados a una decisión de producto.

### Profundización metodológica

- [ ] Ampliar simulaciones de poder y precisión para clusters, tamaños desiguales, autocorrelación, pérdidas y soporte débil; revisar sesgo, error tipo I y cobertura.
- [ ] Incorporar ejemplos ejecutables de sensibilidad a tendencias paralelas y confusión no medida, con parámetros interpretables.
- [ ] Profundizar pérdidas selectivas, incumplimiento e interferencia, conectando cada problema con identificación e inferencia.
- [ ] Desarrollar módulos específicos de regresión discontinua y variables instrumentales.
- [ ] Completar las fichas de fórmulas con condiciones de uso, derivación breve, ejemplo numérico e implementación contrastada.
- [ ] En test A/B, revisar asignación persistente y usuarios con observaciones repetidas, desbalance respecto de la proporción de asignación prevista (SRM), registro de exposición y problemas de instrumentación; definir cómo tratar métricas múltiples, consultas repetidas a resultados y reglas de parada, distinguiendo horizonte fijo y análisis secuencial.

### Visualización y mantenimiento

- [ ] Crear funciones reutilizables para mapas de adopción, event studies, Love plots, soporte y sensibilidad, con exportación académica.
- [ ] Para el caso A/B, generar en Python tablas por variante, efectos e intervalos, curvas de poder/MDE y diagnósticos de asignación y seguimiento temporal, con estilo de paper y notas sobre muestra, unidades y método de incertidumbre.
- [ ] Incorporar un caso aplicado reproducible con datos públicos y contexto documentado.
- [ ] Automatizar comprobaciones de código, referencias locales y formato matemático.
- [ ] Definir licencia, criterios de contribución y revisión periódica de referencias y APIs.

## Referencias metodológicas

Estas referencias fundamentan el contenido metodológico. Al usar la skill en un trabajo, corresponde citar los métodos y el software efectivamente utilizados, junto con sus versiones.

1. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC. [Libro y materiales de los autores](https://miguelhernan.org/whatifbook).
2. Hernán, M. A., & Robins, J. M. (2016). Using big data to emulate a target trial when a randomized trial is not available. *American Journal of Epidemiology, 183*(8), 758–764. [DOI: 10.1093/aje/kwv254](https://doi.org/10.1093/aje/kwv254). [Texto completo](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/).
3. Callaway, B., & Sant’Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. [DOI: 10.1016/j.jeconom.2020.12.001](https://doi.org/10.1016/j.jeconom.2020.12.001). [Versión de los autores](https://psantanna.com/files/Callaway_SantAnna_2020.pdf).
4. Roth, J. (2022). Pretest with caution: Event-study estimates after testing for parallel trends. *American Economic Review: Insights, 4*(3), 305–322. [DOI: 10.1257/aeri.20210236](https://doi.org/10.1257/aeri.20210236). [Texto del autor](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf).
5. Cattaneo, M. D., Idrobo, N., & Titiunik, R. (2020). *A Practical Introduction to Regression Discontinuity Designs: Foundations*. Cambridge University Press. [DOI: 10.1017/9781108684606](https://doi.org/10.1017/9781108684606). [Manuscrito de los autores](https://mdcattaneo.github.io/books/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf).
6. Chen, H., Harinen, T., Lee, J.-Y., Yung, M., & Zhao, Z. (2020). *CausalML: Python package for causal machine learning*. arXiv:2002.11631. [DOI: 10.48550/arXiv.2002.11631](https://doi.org/10.48550/arXiv.2002.11631).

7. Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics, 225*(2), 175–199. [DOI: 10.1016/j.jeconom.2020.09.006](https://doi.org/10.1016/j.jeconom.2020.09.006).
8. Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *The Review of Economic Studies, 90*(5), 2555–2591. [DOI: 10.1093/restud/rdad018](https://doi.org/10.1093/restud/rdad018). [Texto de los autores](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf).
9. Roth, J., Sant’Anna, P. H. C., Bilinski, A., & Poe, J. (2023). *What’s trending in difference-in-differences? A synthesis of the recent econometrics literature*. [Manuscrito de los autores, arXiv:2201.01194v3](https://arxiv.org/abs/2201.01194v3).
10. Sant’Anna, P. H. C., & Zhao, J. (2020). Doubly robust difference-in-differences estimators. *Journal of Econometrics, 219*(1), 101–122. [DOI: 10.1016/j.jeconom.2020.06.003](https://doi.org/10.1016/j.jeconom.2020.06.003). [Versión de los autores](https://psantanna.com/files/SantAnna_Zhao_DRDID.pdf).
11. Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika, 70*(1), 41–55. [DOI: 10.1093/biomet/70.1.41](https://doi.org/10.1093/biomet/70.1.41).
12. Austin, P. C. (2009). Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples. *Statistics in Medicine, 28*(25), 3083–3107. [DOI: 10.1002/sim.3697](https://doi.org/10.1002/sim.3697). [Texto completo](https://pmc.ncbi.nlm.nih.gov/articles/PMC3472075/).
13. Abadie, A., & Imbens, G. W. (2008). On the failure of the bootstrap for matching estimators. *Econometrica, 76*(6), 1537–1557. [DOI: 10.3982/ECTA6474](https://doi.org/10.3982/ECTA6474).
14. Abadie, A., & Imbens, G. W. (2016). Matching on the estimated propensity score. *Econometrica, 84*(2), 781–807. [DOI: 10.3982/ECTA11293](https://doi.org/10.3982/ECTA11293).
15. Rosenbaum, P. R. (1987). Sensitivity analysis for certain permutation inferences in matched observational studies. *Biometrika, 74*(1), 13–26. [DOI: 10.1093/biomet/74.1.13](https://doi.org/10.1093/biomet/74.1.13).
16. King, G., & Nielsen, R. (2019). Why propensity scores should not be used for matching. *Political Analysis, 27*(4), 435–454. [Publicación y materiales de los autores](https://gking.harvard.edu/publication/why-propensity-scores-should-not-be-used-for-matching/).

## Documentación técnica

Documentación consultada el 12 de octubre de 2026. Para reproducir resultados, registrar la versión utilizada y revisar la API correspondiente.

- **CausalML:** [repositorio de Uber](https://github.com/uber/causalml), [metodología](https://causalml.readthedocs.io/en/stable/methodology.html), [API](https://causalml.readthedocs.io/en/stable/causalml.html) y [validación](https://causalml.readthedocs.io/en/stable/validation.html).
- **DiD:** [`differences`](https://bernardodionisi.github.io/differences/latest/) y [HonestDiD](https://github.com/asheshrambachan/HonestDiD).
- **Matching CausalML:** [código documentado de matching y balance](https://causalml.readthedocs.io/en/stable/_modules/causalml/match.html).
- **statsmodels:** [poder de una prueba t para dos muestras](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html) e [intervalos de Welch](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.CompareMeans.tconfint_diff.html).
- **Matplotlib:** [expresiones matemáticas con Mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html) y [renderizado con LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html).
- **OpenAI:** [estructura y uso de skills](https://learn.chatgpt.com/docs/build-skills) y [evaluación de skills](https://developers.openai.com/blog/eval-skills).
