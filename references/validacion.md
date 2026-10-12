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

## Casos específicos de DiD

| Solicitud o problema | Comportamiento esperado |
|---|---|
| Rollout escalonado con efectos crecientes; se propone TWFE | Definir ATT por cohorte–período, controles admisibles y agregación; explicar posibles comparaciones con ya tratados |
| Todos terminan tratados y se pide efecto a cinco años | Revisar soporte de cada horizonte; no inventar comparaciones o extrapolación |
| Leads con p > 0.05 se presentan como prueba del supuesto | Revisar precisión y contexto, explicar límite del pretest y proponer sensibilidad |
| Miles de personas en seis municipios | Identificar dependencia, pocos clusters y número tratado; justificar inferencia y simulación |
| Se suman cuatro varianzas de un panel | Incorporar covarianza pre–post y dependencia relevante |
| Se cambia tratamiento reversible a cohorte absorbente | Revisar trayectoria y estimando antes de elegir implementación |

## Casos específicos de PSM

| Solicitud o problema | Comportamiento esperado |
|---|---|
| Se pierde 40% de tratados por soporte | Reportar población retenida, exclusiones y límites de generalización |
| AUC alta y score equilibrado se presentan como validación | Revisar covariables originales, selección, soporte y confusión no medida |
| Se incluyen resultados posteriores o mediadores | Revisar temporalidad y efecto objetivo; corregir el diseño |
| Controles reutilizados se cuentan como observaciones independientes | Reconstruir pesos e IDs y justificar varianza que represente dependencia |
| Se pide bootstrap ordinario para vecinos con k fijo | Explicar límites y buscar método de inferencia respaldado para ese estimador |
| Caliper 0.2 se interpreta igual en todas las APIs | Verificar escala, estandarización y SD de referencia en la versión usada |
| PSM+DiD se presenta como doblemente robusto por definición | Distinguir condiciones de matching, tendencias paralelas y construcción de DR-DiD |

Verifica el ejemplo DiD contra la identidad de cuatro medias y rutinas de Welch sobre cambios, y evalúa error tipo I/cobertura con error Monte Carlo. En el ejemplo PSM, verifica caliper, IDs sin reutilización, retención, casos sin soporte y denominador SMD fijo con cálculos manuales. Estas pruebas de código no sustituyen evaluar las respuestas del asesor sobre los casos reservados.
