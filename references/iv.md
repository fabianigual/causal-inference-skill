# Variables instrumentales: identificación e inferencia

Usa esta guía cuando la variación propuesta provenga de un instrumento, una invitación, un incentivo o una regla que cambie la recepción del tratamiento. Reconstruye por qué el instrumento modifica la participación y qué otras vías podrían afectar el resultado. Una primera etapa fuerte no justifica exclusión ni independencia.

## Estimando y supuestos

Distingue instrumento $Z$, tratamiento recibido $A$ y resultado $Y$. En el caso binario, $A(z)$ describe la recepción bajo cada valor del instrumento. Para interpretar el cociente de Wald como LATE, justifica consistencia, ausencia de interferencia relevante, independencia del instrumento respecto de los resultados y tratamientos potenciales, exclusión, relevancia y monotonicidad. Si la independencia es condicional a covariables, usa una identificación y un estimador acordes con ese condicionamiento; no apliques automáticamente el cociente bruto.

| Condición | Qué debe examinar |
|---|---|
| Relevancia | El instrumento cambia la recepción; magnitud y precisión de la primera etapa |
| Independencia | Sorteo, regla o mecanismo que haga defendible la comparación entre valores del instrumento |
| Exclusión | El instrumento afecta Y solo a través de A; revisar servicios adicionales, expectativas y efectos directos |
| Monotonicidad | Tras orientar Z, no hay unidades cuya recepción disminuya al pasar de Z=0 a Z=1 |

Con estos supuestos en el caso binario sin ajuste:

$$
\tau_{LATE}=E[Y(1)-Y(0)\mid A(1)>A(0)]
=\frac{E[Y\mid Z=1]-E[Y\mid Z=0]}
{E[A\mid Z=1]-E[A\mid Z=0]}.
$$

Explica quiénes serían los compliers según el mecanismo institucional. No se identifican individualmente a partir de la recepción observada. El efecto puede cambiar con el instrumento y no equivale en general al ATE o ATT. No extiendas esta fórmula a múltiples instrumentos o tratamientos continuos sin definir el parámetro y sus condiciones. Véanse [Imbens y Angrist (1994)](https://www.nber.org/papers/t0118) y [Angrist, Imbens y Rubin](https://www.nber.org/papers/t0136).

En un ensayo con incumplimiento, conserva el ITT como efecto de asignación. Usar la asignación como instrumento para recepción añade supuestos, especialmente exclusión; la aleatorización por sí sola no los satisface. Comparar receptores y no receptores no recupera automáticamente ese LATE.

## Estimación, incertidumbre y sensibilidad

Reporta primera etapa, forma reducida y estimación IV con la misma muestra y especificación. Usa una rutina IV que calcule la varianza del procedimiento completo; no tomes los errores estándar de una segunda regresión OLS sobre tratamiento predicho como inferencia 2SLS válida.

Examina fuerza del instrumento con diagnósticos adecuados a heterocedasticidad, clusters y número de instrumentos. La regla F > 10 no garantiza universalmente validez del IC convencional. Con instrumentos débiles, considera pruebas e intervalos robustos a identificación débil, como Anderson–Rubin bajo sus condiciones, y explica si el conjunto resulta amplio, disjunto o no acotado. No lo reemplaces por un intervalo estrecho para facilitar la presentación. [Lee et al. (2022)](https://www.nber.org/papers/w29124) estudian los límites de la inferencia basada en el t-ratio usual.

Respeta el nivel de asignación y dependencia. Pocos clusters pueden comprometer también la inferencia robusta a instrumentos débiles: robustez a un problema no resuelve el otro. Un test de sobreidentificación favorable tampoco demuestra que todos los instrumentos sean válidos.

Prioriza sensibilidad a vías directas, selección del instrumento, primera etapa heterogénea y población de compliers. Para poder, simula asignación del instrumento, recepción, resultado y procedimiento IV previsto; incluye escenarios de primera etapa débil. Más receptores observados no equivale a más variación instrumental.

## Entrega y ejecución

Devuelve argumento de identificación, población local, primera etapa y forma reducida, método de inferencia y alcance de la conclusión. Si exclusión no es defendible, explica qué efecto de asignación puede seguir siendo informativo. Esta guía no incorpora un estimador IV ejecutable; verifica documentación y condiciones de la implementación elegida antes de usarla.
