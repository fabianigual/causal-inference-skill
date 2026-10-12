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

Puede orientar problemas experimentales y observacionales, diferencias en diferencias, regresión discontinua y estrategias con variables instrumentales. Los scripts incluidos cubren cálculos básicos de poder e inferencia; los diseños más complejos requieren un procedimiento adecuado al caso.

## Cómo está pensada

La identificación organiza el trabajo. La pregunta y el mecanismo de asignación llevan al estimando; el estimando y el diseño llevan a los supuestos, al estimador y a la forma de calcular la incertidumbre. Las recomendaciones deben explicar qué decisión mejora la evidencia y qué queda pendiente.

La base conceptual toma como referencia a [Hernán y Robins (2020)](https://miguelhernan.org/whatifbook). Cuando ayuda a ordenar temporalidad, elegibilidad, asignación y seguimiento, utiliza el marco de ensayo objetivo de [Hernán y Robins (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/).

La skill pone atención a problemas frecuentes: confusión no medida, ajuste por variables posteriores al tratamiento, falta de soporte, pérdidas de seguimiento, interferencia, anticipación, cambios en medición y dependencia entre observaciones. Cada alerta debe conectar el hallazgo con su consecuencia y una acción concreta.

Para diferencias en diferencias, considera el calendario de adopción y las comparaciones entre cohortes, siguiendo a [Callaway y Sant’Anna (2021)](https://doi.org/10.1016/j.jeconom.2020.12.001). También distingue un diagnóstico de pre-tendencias de una justificación del supuesto: un pretest puede tener poca potencia y condicionar el análisis a su resultado puede distorsionar la inferencia, como muestra [Roth (2022)](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf).

En regresión discontinua, considera el efecto en el umbral, el soporte y los diagnósticos pertinentes al marco elegido, con [Cattaneo, Idrobo y Titiunik (2020)](https://doi.org/10.1017/9781108684606) como referencia.

Para poder e intervalos, relaciona los cálculos con la muestra, la asignación y la dependencia. La precisión estadística y la identificación son preguntas distintas: un intervalo estrecho puede coexistir con sesgo, y un resultado no significativo puede admitir efectos relevantes.

## CausalML

La skill incorpora una [guía de uso de CausalML](references/causalml.md), la biblioteca de Python presentada por [Chen et al. (2020)](https://arxiv.org/abs/2002.11631).

Incluye criterios para elegir meta-learners y árboles o bosques causales/uplift, revisar propensión y soporte, separar entrenamiento de evaluación y considerar incertidumbre. El foco es estimar y evaluar efectos heterogéneos bajo un argumento de identificación explícito.

La guía distingue CATE de efecto individual, y ranking de calibración e inferencia. También revisa el uso de Qini/AUUC fuera de muestra y detalles de la API que pueden afectar la interpretación. Las firmas y capacidades deben comprobarse en la [documentación oficial de la versión utilizada](https://causalml.readthedocs.io/en/stable/causalml.html).

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

Los casos son ilustrativos. Las decisiones y los resultados de un análisis concreto dependen de su diseño y de la evidencia disponible.

## Ejemplo ejecutable en Python

Con las dependencias básicas instaladas, desde la raíz de este repositorio:

```bash
python scripts/ejemplo_poder_precision.py --output-dir outputs/demo
```

El script genera curvas de poder, MDE y precisión, una tabla CSV y LaTeX, figuras PNG y SVG y un archivo de metadatos. Usa parámetros supuestos para ilustrar planificación con dos brazos independientes; no analiza datos de una evaluación real.

[`requirements.txt`](requirements.txt) registra las versiones verificadas para este ejemplo en Python 3.12. [`requirements-causalml.txt`](requirements-causalml.txt) declara CausalML como recurso opcional; su instalación debe resolverse en un entorno compatible del análisis. Los entornos, datos y resultados se guardan fuera de los recursos de la skill.

## Qué contiene el repositorio

| Archivo o carpeta | Para qué sirve |
|---|---|
| [`SKILL.md`](SKILL.md) | Instrucciones y criterios que guían al asesor |
| [`references/identificacion.md`](references/identificacion.md) | Identificación, temporalidad y amenazas |
| [`references/poder-inferencia.md`](references/poder-inferencia.md) | Poder, precisión, intervalos y simulación |
| [`references/formulas.md`](references/formulas.md) | Fórmulas, notación y condiciones de uso |
| [`references/causalml.md`](references/causalml.md) | Selección, uso y evaluación con CausalML |
| [`references/python-visualizacion.md`](references/python-visualizacion.md) | Tablas y gráficos académicos en Python |
| [`references/validacion.md`](references/validacion.md) | Casos para revisar el comportamiento de la skill |
| [`references/fuentes.md`](references/fuentes.md) | Fuentes metodológicas y documentación técnica |
| [`scripts/`](scripts/) | Cálculos básicos y ejemplo reproducible |
| [`assets/paper.mplstyle`](assets/paper.mplstyle) | Estilo visual para Matplotlib |
| [`agents/openai.yaml`](agents/openai.yaml) | Nombre y descripción para la interfaz |

El `.gitignore` excluye entornos, caches, archivos locales, configuración de entorno y las carpetas de datos y resultados. Conserva el código, las referencias y los assets; no excluye de manera general extensiones como CSV, JSON, PNG, SVG o TEX.

## Referencias metodológicas

Estas referencias fundamentan el contenido metodológico. Al usar la skill en un trabajo, corresponde citar los métodos y el software efectivamente utilizados, junto con sus versiones.

1. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC. [Libro y materiales de los autores](https://miguelhernan.org/whatifbook).
2. Hernán, M. A., & Robins, J. M. (2016). Using big data to emulate a target trial when a randomized trial is not available. *American Journal of Epidemiology, 183*(8), 758–764. [DOI: 10.1093/aje/kwv254](https://doi.org/10.1093/aje/kwv254). [Texto completo](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/).
3. Callaway, B., & Sant’Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. [DOI: 10.1016/j.jeconom.2020.12.001](https://doi.org/10.1016/j.jeconom.2020.12.001). [Versión de los autores](https://psantanna.com/files/Callaway_SantAnna_2020.pdf).
4. Roth, J. (2022). Pretest with caution: Event-study estimates after testing for parallel trends. *American Economic Review: Insights, 4*(3), 305–322. [DOI: 10.1257/aeri.20210236](https://doi.org/10.1257/aeri.20210236). [Texto del autor](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf).
5. Cattaneo, M. D., Idrobo, N., & Titiunik, R. (2020). *A Practical Introduction to Regression Discontinuity Designs: Foundations*. Cambridge University Press. [DOI: 10.1017/9781108684606](https://doi.org/10.1017/9781108684606). [Manuscrito de los autores](https://mdcattaneo.github.io/books/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf).
6. Chen, H., Harinen, T., Lee, J.-Y., Yung, M., & Zhao, Z. (2020). *CausalML: Python package for causal machine learning*. arXiv:2002.11631. [DOI: 10.48550/arXiv.2002.11631](https://doi.org/10.48550/arXiv.2002.11631).

## Documentación técnica

Documentación consultada el 12 de octubre de 2026. Para reproducir resultados, registrar la versión utilizada y revisar la API correspondiente.

- **CausalML:** [repositorio de Uber](https://github.com/uber/causalml), [metodología](https://causalml.readthedocs.io/en/stable/methodology.html), [API](https://causalml.readthedocs.io/en/stable/causalml.html) y [validación](https://causalml.readthedocs.io/en/stable/validation.html).
- **statsmodels:** [poder de una prueba t para dos muestras](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html) e [intervalos de Welch](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.CompareMeans.tconfint_diff.html).
- **Matplotlib:** [expresiones matemáticas con Mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html) y [renderizado con LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html).
- **OpenAI:** [estructura y uso de skills](https://learn.chatgpt.com/docs/build-skills) y [evaluación de skills](https://developers.openai.com/blog/eval-skills).
