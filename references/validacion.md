# 7. Validación del asesor

Probar solicitudes realistas con información incompleta: programa asignado a ocho municipios con miles de personas; capacitación con pérdidas selectivas; DiD con rollout y anticipación; tratamiento cuya intensidad responde a resultados previos; RD con poco soporte junto al umbral.

Evaluar si identifica el parámetro y el mecanismo de asignación, prioriza amenazas relevantes, reconoce límites de observabilidad, elige inferencia apropiada, calcula poder para el análisis previsto y explica qué decisión mejora la evidencia. Incluir casos donde la respuesta correcta sea restringir una conclusión o pedir una pieza decisiva de contexto.

Validar los cálculos contra rutinas de referencia y casos conocidos. Para procedimientos complejos, evaluar sesgo, error tipo I y cobertura mediante simulación repetida, incluyendo error Monte Carlo. Comparar el comportamiento del asesor con y sin la skill sobre casos reservados; la validación de estructura de archivos no prueba corrección metodológica.


## Casos para la integración de CausalML

- Un análisis presenta CATE como efecto individual comprobado: debe reformular interpretación y explicar qué puede identificarse.
- Un modelo usa el mismo conjunto para ajustar, escoger subgrupos y reportar Qini: debe proponer particiones y evaluación independientes, con selección explícita.
- Un análisis observacional atribuye interpretación causal a AUUC bruto: debe examinar asignación, soporte y evaluación ajustada, sin certificar ausencia de confusión.
- Un usuario pasa propensión a un T-learner y lo describe como IPW: debe revisar la implementación y distinguir ajuste por modelos de resultados de ponderación.
- La tabla pasa CATE estimado como `treatment_effect_col` a las métricas: debe reservar ese argumento para verdad conocida y usar columnas de predicciones de modelo.
- Se pide un IC por fila en un ensayo por municipios: debe justificar incertidumbre congruente con dependencia y evitar asumir que el bootstrap de la biblioteca la incorpora.
- Se solicitan gráficos estilo LaTeX y los imports cambian rcParams: debe restaurar el estilo académico y revisar legibilidad.

Probar ejecución en un entorno compatible cuando se añadan scripts o se realice un análisis con CausalML. Para ejemplos conceptuales, distinguir comprobación de firmas y sintaxis de ejecución real. En simulaciones, usar efectos verdaderos conocidos para evaluar sesgo, cobertura y heterogeneidad recuperada; un experimento real no proporciona efectos individuales verdaderos observados.
