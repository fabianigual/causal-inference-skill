# 2. Identificación como núcleo

Antes de elegir una regresión, reconstruir cómo se asignó o recibió el tratamiento: regla administrativa, umbral, sorteo, decisión individual, rollout, cupos, incentivos o instrumento. Precisar qué variación ofrece una comparación creíble. Un algoritmo no descubre el mecanismo institucional a partir de una columna de tratamiento.

Fijar intervención, comparación, población, resultado, horizonte y momento cero. En problemas de tratamientos individuales, una especificación de ensayo objetivo puede ayudar a alinear elegibilidad, asignación y seguimiento. En DiD y RD, formular también los supuestos propios del diseño; no imponer un único marco de ajuste a todos los problemas.

Representar hipótesis causales con un DAG cuando ayude a elegir covariables, detectar selección o discutir mecanismos. Registrar qué flechas provienen de conocimiento sustantivo y qué alternativas se están considerando. Para estimar efectos totales, evaluar si ajustar por mediadores o colisionadores introduce un problema; otros estimandos pueden requerir estrategias distintas.

Cada supuesto debe registrar su estado con lenguaje preciso: justificado por el diseño, examinado mediante implicaciones observables, pendiente de contexto, cuestionado por evidencia o no verificable con estos datos. Un test favorable no convierte un supuesto contrafactual en un hecho comprobado.

Si la identificación no se sostiene, precisar qué efecto no puede respaldarse, qué análisis descriptivo sigue siendo válido y qué información, cambio de diseño o análisis de sensibilidad podría mejorar la situación. Considerar identificación parcial cuando el problema y los supuestos permitan construir cotas informativas.

### Amenazas que conviene revisar según el caso

| Amenaza | Qué debe examinar | Acción posible |
|---|---|---|
| Confusión no medida | Mecanismo de selección y covariables ausentes | Mejorar diseño o medición; sensibilidad y controles negativos con sus propios supuestos |
| Ajuste posterior al tratamiento | Temporalidad y papel causal de cada variable | Revisar el conjunto de ajuste y el estimando |
| Selección y pérdidas | Quién entra, permanece y tiene resultado observado | Describir pérdidas; modelar censura o construir cotas bajo supuestos explícitos |
| Falta de soporte | Comparabilidad en la población objetivo | Diagnosticar soporte; documentar cualquier restricción y cambio de estimando |
| Interferencia | Exposición entre unidades, redes o territorios | Redefinir exposición y efecto; considerar diseño por grupos o efectos indirectos |
| Anticipación y shocks | Calendario institucional y cambios simultáneos | Revisar controles, ventanas y supuestos de DiD |
| Cambios en medición | Instrumentos, registros, códigos y composición | Evaluar comparabilidad; validar datos y definiciones |
| Dependencia | Asignación, repetición temporal y correlación espacial | Elegir inferencia congruente con muestreo, asignación y dependencia |
| Generalización | Diferencia entre muestra analizada y población objetivo | Limitar alcance o justificar transporte bajo supuestos adicionales |

