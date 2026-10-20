# Regresión discontinua: efecto local e inferencia

Usa esta guía cuando una regla de elegibilidad o asignación cambie en un umbral. Precisa puntaje, corte, dirección de la regla, fecha de medición, recepción efectiva y otras políticas que usen el mismo corte. Un salto en una figura no basta para atribuir un efecto causal.

## Marco de identificación

Distingue dos decisiones: sharp/fuzzy describe si el tratamiento cambia de forma determinista o probabilística en el corte; continuidad/local randomization describe el argumento de identificación. No uses ambos pares como sinónimos.

En sharp RD, con tratamiento al superar $c$, el marco de continuidad identifica:

$$
\tau(c)=\lim_{r\downarrow c}E[Y\mid R=r]
-\lim_{r\uparrow c}E[Y\mid R=r].
$$

Justifica continuidad de las medias de resultados potenciales en el corte, consistencia y ausencia de interferencia relevante. El efecto corresponde al umbral; la muestra dentro del ancho de banda no convierte automáticamente el parámetro en un ATE para toda esa ventana.

En fuzzy RD, define el salto de recepción y los supuestos de exclusión y monotonicidad locales que permiten interpretar el cociente entre salto de resultado y de tratamiento. Un salto pequeño en recepción plantea identificación débil. Consulta también [IV](iv.md); no interpretes el cociente como el efecto sobre todos los elegibles.

En local randomization, define una ventana y un mecanismo de asignación defendible dentro de ella, con los supuestos adicionales sobre resultados potenciales pertinentes a ese marco. La cercanía al corte no establece por sí sola una aleatorización. Selección de ventana, inferencia y población deben ser coherentes con esa justificación. Véase [Cattaneo, Idrobo y Titiunik (2020)](https://mdcattaneo.github.io/books/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf).

## Diagnósticos y estimación

| Decisión o hallazgo | Acción útil |
|---|---|
| Posible manipulación precisa del puntaje | Reconstruir medición e incentivos; examinar densidad y heaping con un método adecuado al soporte |
| Pocos valores distintos o puntaje discreto | Contar valores y observaciones por lado; revisar si la aproximación de continuidad o una ventana local es defendible |
| Otra regla cambia en el mismo corte | Reconocer el efecto conjunto o buscar variación adicional que separe intervenciones |
| Salto en covariables predeterminadas | Examinar composición y mecanismo; un test favorable no prueba continuidad de resultados potenciales |
| Exclusión de observaciones junto al corte | Explicar por qué y qué extrapolación introduce un donut RD; no presentarlo como reparación automática |

En el marco de continuidad, considera polinomios locales de bajo orden a cada lado, selección de ancho de banda y kernel explícitos. Evita polinomios globales de alto grado como solución por defecto. Separa el gráfico descriptivo por bins del estimador y del intervalo.

Un ancho de banda óptimo para error cuadrático medio puede dejar sesgo relevante para inferencia. Usa una construcción respaldada, como inferencia robusta con corrección de sesgo, o una estrategia de undersmoothing justificada. Restar una estimación de sesgo conservando el error estándar original no incorpora la incertidumbre de esa corrección. Examina dependencia, puntajes con masas y pocos clusters. [Cattaneo, Titiunik y Vazquez-Bare (2020)](https://mdcattaneo.github.io/papers/Cattaneo-Titiunik-VazquezBare_2020_Sage.pdf) desarrollan estas decisiones.

## Sensibilidad y alcance

Compara anchos de banda, órdenes locales y muestras sustantivamente defendibles; no selecciones por significación. Justifica cortes placebo y covariables predeterminadas como falsificaciones específicas. Una prueba de densidad no significativa no descarta toda manipulación; con soporte discreto, tampoco debe aplicarse una prueba pensada para un puntaje continuo sin revisar sus condiciones.

Planifica poder con densidad y variabilidad cerca del corte, curvatura, primera etapa si es fuzzy y estimador previsto. El tamaño total de la base puede ser poco informativo sobre precisión local.

Entrega efecto y población local, marco de identificación, muestra y valores de soporte por lado, ancho de banda, método de incertidumbre y sensibilidad. Esta guía no incorpora un estimador RD ejecutable; verifica la implementación elegida y evita atribuirle capacidades no comprobadas.
