# 3. Poder, precisión e inferencia

Para planificación, solicitar o construir escenarios de efecto mínimo sustantivamente relevante, nivel de significación, poder objetivo, variabilidad o riesgo basal, asignación entre brazos, número y tamaño de grupos, ICC, pérdidas y análisis previsto. No rellenar parámetros desconocidos con valores que parezcan empíricos: etiquetarlos como escenarios ilustrativos.

Cuando el presupuesto o la muestra están fijados, calcular el efecto mínimo detectable (MDE), la curva de poder y la precisión esperada. Presentar sensibilidad a los parámetros inciertos. No usar el efecto observado para calcular y presentar poder retrospectivo como información adicional a un resultado ya analizado.

Para diseños simples, usar fórmulas analíticas con condiciones explícitas. Para pocos grupos, tamaños desiguales, medidas repetidas, DiD, RD, incumplimiento o pérdidas complejas, usar procedimientos específicos o simulación del diseño. La simulación debe generar datos bajo escenarios explícitos, ejecutar el estimador y el método de incertidumbre previstos, y medir rechazo bajo la alternativa, error tipo I bajo el nulo y cobertura. Informar el error Monte Carlo de las tasas simuladas.

Un intervalo debe indicar nivel, parámetro, unidades, método y población. Seleccionar la distribución crítica y el estimador de varianza según el diseño; evitar tratar todos los casos como $\hat\tau\pm1.96SE$. Un IC estrecho puede coexistir con sesgo de identificación. Un resultado no significativo puede ser compatible con efectos sustantivos; discutir el intervalo y, cuando corresponda, pruebas de equivalencia con márgenes justificados.

Para resultados múltiples, efectos por subgrupo o event studies, distinguir inferencia puntual y simultánea, análisis confirmatorio y exploratorio. No escoger especificaciones, controles o ventanas para obtener significación.

## DiD y PSM

Para [DiD](did.md), planifica con varianza de cambios en el caso básico y simula calendario, dinámica, dependencia y estimador en diseños complejos. No confundas correlación pre–post con ICC ni número de personas con número de grupos de asignación. Para event studies, define si el objetivo es un efecto puntual, agregado o una familia de efectos.

Para [PSM](psm.md), incluye estimación de score, matching, pérdidas de tratados y reutilización en la simulación. Un cálculo condicional para pares puede ser un punto de partida, pero no valida el diseño construido ni su inferencia. La rutina de matching de una biblioteca no proporciona por sí sola un IC. Evalúa poder junto con retención, sesgo, error tipo I y cobertura.
