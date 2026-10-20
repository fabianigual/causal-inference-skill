# Experimentos: asignación, estimación e incertidumbre

Usa esta guía cuando el argumento causal provenga de asignación aleatoria. Reconstruye unidad, probabilidades, bloques, pares, restricciones de asignación y momento de exposición. Distingue unidad asignada, observada y analizada. La etiqueta «experimento» no determina por sí sola el estimador ni su varianza.

## Estimando y diseño

Define ITT como efecto de asignación y precisa horizonte, resultado y población. Distingue inferencia sobre las unidades del ensayo de generalización a una población; la segunda puede requerir información de selección o transporte. Pérdidas e interferencia pueden comprometer identificación aun cuando la asignación inicial haya sido aleatoria.

| Diseño | Decisión de análisis |
|---|---|
| Aleatorización individual simple | Contraste según asignación; diferenciar incertidumbre de randomización y muestreo según el objetivo |
| Bloques o estratos | Respetar probabilidades y agregación entre bloques; no usar un contraste bruto si pondera otra población |
| Pares de unidades o clusters | Conservar pares, contraste y mecanismo de asignación; los individuos dentro del cluster no crean asignaciones adicionales |
| Probabilidades desiguales | Usar una construcción compatible, como Horvitz–Thompson o Hájek bajo sus condiciones; declarar normalización |
| Conglomerados | Definir si el efecto promedia personas o clusters; considerar tamaños, ponderación y dependencia |

Con incumplimiento, no sustituyas ITT por una comparación de receptores. Para un efecto de recepción mediante asignación instrumental, consulta [IV](iv.md). Para pérdidas o efectos per-protocol con adherencia cambiante, consulta [selección y longitudinalidad](seleccion-longitudinal.md).

## Ajuste basal y precisión

Considera ANCOVA o ajuste por covariables basales pronósticas según diseño y estimando. En el caso de aleatorización completa y condiciones de regularidad, una regresión con tratamiento, covariables centradas e interacciones tratamiento–covariable permite ajuste flexible con inferencia robusta apropiada. No atribuyas a cualquier especificación OLS garantías de precisión o cobertura. [Lin (2013)](https://doi.org/10.1214/12-AOAS583) desarrolla este resultado y sus límites asintóticos.

Define el ajuste antes de observar resultados cuando sea confirmatorio. El resultado basal puede mejorar precisión en un ensayo; no traslades automáticamente las condiciones de ANCOVA experimental a un DiD observacional. Planifica poder usando la varianza y dependencia del estimador previsto, no una fórmula sin ajuste si la ganancia basal es parte del diseño.

## Dependencia, pocos grupos y pruebas

Con clusters, registra número total y por brazo, desigualdad de tamaños y concentración de información. Errores agrupados convencionales pueden funcionar mal con pocos grupos. Considera correcciones de muestra pequeña, bootstrap o inferencia por randomización solo con condiciones defendibles para ese diseño; no fijes un número universal de clusters que garantice validez.

La inferencia por randomización debe reproducir las asignaciones permitidas, incluidos bloques y pares. Una prueba exacta de una hipótesis nula aguda, como ausencia de efecto para toda unidad, no es automáticamente una prueba exacta de efecto promedio cero con heterogeneidad. Explica el nulo y las condiciones de cualquier inversión para construir intervalos. Agrupar errores no corrige interferencia ni selección.

Para test A/B, revisa asignación persistente, usuarios repetidos, proporción prevista por variante y registro de exposición. Si se observan resultados durante el experimento, define horizonte fijo o un procedimiento secuencial válido; repetir tests convencionales y detenerse cuando p < 0.05 altera el error tipo I. Declara métrica principal, resguardos y tratamiento de multiplicidad.

## Entrega

Reporta protocolo de asignación, muestra por brazo y bloque/cluster, ITT con incertidumbre, ajuste basal, pérdidas y límites de generalización. Con pocos grupos, reconoce si los datos no respaldan inferencia precisa. La referencia de [poder e inferencia](poder-inferencia.md) orienta escenarios y simulación; los ejemplos básicos del repositorio solo cubren brazos independientes.
