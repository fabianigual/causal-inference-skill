# Selección, pérdidas y tratamientos longitudinales

Usa esta guía cuando faltan resultados, cambia la población observada o la exposición varía en el tiempo. Distingue datos ausentes, censura y resultados que dejan de estar definidos, como un resultado posterior a fallecimiento. No los conviertas en un mismo problema de imputación.

## Pérdidas y selección

Reconstruye quién era elegible, quién fue incluido, quién recibió asignación y quién tiene resultado observado en cada horizonte. Describe tasas, razones y momento de las pérdidas por brazo y covariables previas. Tasas similares no descartan selección distinta; tasas diferentes no cuantifican por sí solas el sesgo.

Antes de elegir un método, define si interesa la población originalmente elegible, los participantes o una población con resultado definido bajo ambas intervenciones. Analizar solo quienes permanecen puede cambiar tanto identificación como población.

| Procedimiento | Condiciones y límites que debe explicar |
|---|---|
| Casos completos | Justificar que la selección permite identificar el efecto solicitado; MAR por sí sola no valida cualquier análisis sin ajustar |
| Ponderación por observación o censura | Intercambiabilidad del proceso de observación dada la historia pertinente, positividad de seguimiento y estimación adecuada de probabilidades |
| Imputación múltiple | Mecanismo de ausencia y modelo compatibles con el análisis, tratamiento e interacciones relevantes; combinar incertidumbre entre y dentro de imputaciones |
| Sensibilidad MNAR | Definir cómo se apartan los resultados ausentes de lo supuesto bajo ignorabilidad y calibrar ese parámetro en unidades sustantivas |
| Cotas | Declarar restricciones sobre resultados y selección; reportar qué población y parámetro quedan parcialmente identificados |

MAR no es verificable con los datos observados sin información adicional. Ni imputación ni ponderación corrigen automáticamente pérdidas no ignorables. No limites la evaluación a predecir quién se pierde: examina qué información justificaría intercambiabilidad de observación y si hay historias con seguimiento casi nulo.

Las cotas de Lee pueden ser útiles bajo asignación exógena y selección monotónica, con las demás condiciones del diseño. En su caso básico acotan un efecto para quienes tendrían resultado observado bajo ambas asignaciones; no recuperan automáticamente el ATE de la población original. Explica dirección y plausibilidad de la monotonicidad y la regla de recorte. Véase [Lee (2009)](https://www.nber.org/papers/w11721).

## Exposición que cambia en el tiempo

Define una trayectoria o regla de tratamiento, su comparación y horizonte. Alinea elegibilidad, asignación y seguimiento en el momento cero; clasificar desde el inicio por una exposición que solo se conocerá después puede introducir sesgo de tiempo inmortal. Un ensayo objetivo puede ayudar a ordenar esas decisiones.

Si una covariable $L_t$ responde a tratamiento previo y predice tratamiento posterior y resultado, ajustarla en una regresión convencional puede bloquear parte del efecto o introducir selección; omitirla puede dejar confusión de exposiciones posteriores. La regla de evitar ajuste por mediadores no resuelve por sí sola este problema.

Considera g-fórmula, modelos estructurales marginales con ponderación o g-estimation según el régimen y los supuestos. Explicita consistencia, intercambiabilidad secuencial dada la historia y positividad para las decisiones de tratamiento y seguimiento pertinentes. La positividad puede deteriorarse al acumular historias; revisa pesos longitudinales, estabilización, truncamiento y alcance de la conclusión. [Hernán y Robins](https://miguelhernan.org/whatifbook) desarrollan estos métodos y sus condiciones.

No uses un score basal ni un meta-learner de tratamiento puntual como solución automática para exposición repetida. Distingue un régimen sostenido de una regla dinámica que responde a la historia. Para estimar efectos per-protocol en ensayos, conserva el ITT como pregunta distinta y justifica el ajuste adicional por adherencia y censura.

## Entrega y planificación

Entrega flujo de muestra, estimando, hipótesis de selección o de tratamiento secuencial, método elegido y sensibilidad. Si no puedes justificar ignorabilidad, ofrece escenarios o cotas con sus condiciones y limita la conclusión. Para poder, simula el proceso de pérdidas y recepción junto con el análisis previsto; inflar reclutamiento compensa cantidad esperada, no sesgo.

Esta referencia orienta decisiones; no incluye una implementación longitudinal o de cotas validada. Comprueba el procedimiento concreto antes de producir intervalos o atribuirle una población objetivo.
