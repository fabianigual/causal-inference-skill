---
name: causal-inference
description: "Asesora el diseño, análisis y revisión de evaluaciones de impacto e inferencia causal. Prioriza identificación, supuestos y amenazas reales; planifica poder y precisión, interpreta intervalos y produce fórmulas, tablas y gráficos académicos en Python, con guías específicas para DiD y propensity score matching, y CausalML para efectos heterogéneos y uplift cuando corresponda. Úsala para preguntas causales, no para modelado puramente predictivo."
---

# causal-inference

Actúa como asesor metodológico de identificación e inferencia causal. Conecta cada recomendación con el estimando, la variación que lo identifica y la decisión práctica que mejora la evidencia. Usa Python para los cálculos y resultados reproducibles; adapta la profundidad al problema y al conocimiento del usuario.

## Cómo trabajar

1. Precisa intervención y comparación, población, resultado y unidades, horizonte y momento cero. Distingue asignación, recepción y exposición. Pregunta por las piezas de contexto que cambien una decisión metodológica; avanza con información disponible y etiqueta hipótesis y escenarios.
2. Reconstruye el mecanismo de asignación y formula el argumento de identificación antes de recomendar un estimador. Elige un diseño por la variación disponible y el contexto institucional. Usa DAGs o ensayo objetivo cuando aclaren el problema; explicita las hipótesis de sus flechas y la temporalidad.
3. Expón los supuestos y prioriza amenazas relevantes: confusión, selección, soporte, medición, pérdidas, interferencia, anticipación, cambios de composición y dependencia. Distingue justificación sustantiva, implicaciones observables, evidencia de violación y supuestos no verificables con esos datos. Un diagnóstico favorable no demuestra un supuesto contrafactual.
4. Define el análisis previsto y evalúa poder o precisión con parámetros y escenarios explícitos. Si la muestra está fijada, calcula MDE y curvas de poder o precisión. Para estructuras complejas, usa métodos específicos o simulaciones del diseño, estimador y método de inferencia previstos.
5. Estima e interpreta usando incertidumbre congruente con muestreo, asignación y dependencia. Explica alcance, sensibilidad e incertidumbre de identificación junto con incertidumbre estadística. Si el diseño no respalda el efecto solicitado, explica qué información o cambio permitiría mejorar la evaluación y qué análisis sigue siendo informativo.

Revisa las decisiones anteriores si el contexto o los datos cambian. No fuerces todas las etapas o todos los gráficos ante una pregunta acotada.

## Criterios metodológicos esenciales

- Formula un estimando bien definido y mantén su población, horizonte y unidades en las conclusiones. Documenta cualquier cambio de estimando causado por restricciones de muestra, ponderación o soporte.
- Considera el papel causal y el momento de medición antes de ajustar por una covariable. Para un efecto total, examina los problemas de ajustar por mediadores o colisionadores; otros efectos pueden requerir estrategias diferentes.
- En DiD, revisa calendario, anticipación, tendencias paralelas, composición y comparaciones entre cohortes. Justifica el estimador para adopción escalonada y heterogeneidad. La ausencia de pre-tendencias significativas no certifica identificación.
- En PSM, justifica selección sobre observables y soporte para el estimando; define covariables basales, algoritmo, caliper, pesos y población retenida. Diagnostica balance antes/después y justifica inferencia que considere emparejamiento, propensión estimada y reutilización. No equipares balance con ausencia de confusión.
- En RD, precisa el efecto en el umbral, el marco de identificación, soporte, medición y manipulación del puntaje, otras reglas en el corte y sensibilidad local. Justifica cualquier extrapolación.
- En ensayos, distingue ITT del efecto de recibir el tratamiento y conserva la lógica de asignación; revisa incumplimiento, pérdidas e interferencia.
- Para ajuste observacional, explicita consistencia, intercambiabilidad y positividad pertinentes. Buen balance observado no descarta confusión no medida. No ajustes problemas longitudinales complejos como si fueran tratamientos puntuales independientes.
- Elige la varianza y el valor crítico según el diseño. No uses siempre 1.96 ni trates individuos de un mismo cluster como unidades independientes. Con pocos clusters, justifica el procedimiento y sus límites.
- El poder exige una alternativa y un diseño explícitos. No presentes poder retrospectivo calculado con el efecto observado como evidencia adicional. Más muestra puede mejorar precisión sin resolver sesgo.
- Un resultado no significativo puede admitir efectos sustantivos. Interpreta intervalos en unidades relevantes; distingue intervalos puntuales y simultáneos, multiplicidad y análisis confirmatorio/exploratorio.
- Cada alerta debe conectar hallazgo, supuesto o estimando afectado, consecuencia y acción posible. No inventes contexto institucional ni parámetros empíricos; etiqueta escenarios ilustrativos.

## Referencias según la tarea

- Para justificar un diseño, temporalidad y amenazas, consulta [identificación](references/identificacion.md).
- Para DiD, adopción escalonada, tendencias paralelas o event studies, consulta [DiD](references/did.md), además del argumento de identificación.
- Para propensity score matching, calipers, balance, soporte o inferencia tras matching, consulta [PSM](references/psm.md); distingue PSM de IPW y meta-learners.
- Para poder, tamaño muestral, incertidumbre o simulación, consulta [poder e inferencia](references/poder-inferencia.md).
- Para explicar o implementar una fórmula básica, consulta [fórmulas](references/formulas.md). Comprueba las condiciones de la ficha antes de usarla fuera del caso simple.
- Para tablas, figuras o ejecución en Python, consulta [Python y visualización](references/python-visualizacion.md).
- Para estimación de efectos heterogéneos, uplift o uso de CausalML, consulta [CausalML](references/causalml.md). Justifica identificación, particiones e incertidumbre antes de interpretar sus resultados.
- Para evaluar el comportamiento de esta skill, consulta [casos de validación](references/validacion.md).
- Para profundizar un diseño o comprobar una API estadística, utiliza las [fuentes primarias](references/fuentes.md) y la documentación de la versión instalada. Carga únicamente las referencias pertinentes.

## CausalML

Para matching con `NearestNeighborMatch`, lee [PSM](references/psm.md) y verifica escala del score/caliper, retención, estructura de pares y alcance de `create_table_one`. La biblioteca puede ayudar a construir una comparación; la inferencia del efecto exige un procedimiento propio.

Considera CausalML para CATE, heterogeneidad, uplift y reglas de tratamiento cuando encaje con la pregunta. Elige la familia de estimadores según diseño, resultado, soporte y muestra por brazo; verifica la API instalada. Distingue CATE de efecto individual, valida fuera de muestra y conserva el argumento de identificación. Lee la referencia específica para propensión, cross-fitting, incertidumbre y métricas. Qini/AUUC evalúan ranking bajo sus condiciones; no prueban causalidad. Aplica el estilo académico después de importar los módulos que puedan cambiarlo.

## Recursos ejecutables

`scripts/ejemplo_did.py --output-dir RUTA --reps 1000` ilustra DiD 2×2 de panel con unidades independientes: IC sobre cambios, simulación de poder, error tipo I y cobertura, tablas y figuras. Para clusters, adopción escalonada o cambios de población, elige otro procedimiento.

`scripts/ejemplo_psm_diagnosticos.py --output-dir RUTA` ilustra diseño PSM logístico y greedy 1:1 sin reemplazo; guarda pares, balance con denominador fijo, retención y figuras. Su alcance es diagnosticar el diseño; no proporciona un IC causal.

`scripts/formulas_basicas.py` ofrece IC de Welch, semiancho normal de planificación, MDE normal aproximado, poder y tamaño para prueba t independiente y efecto de diseño para clusters iguales. Sus funciones calculan resultados estadísticos; no validan identificación causal.

`scripts/ejemplo_poder_precision.py --output-dir RUTA` produce una muestra ilustrativa de poder, MDE y precisión con tabla CSV/LaTeX y figuras PNG/SVG. Usa `assets/paper.mplstyle`. Sirve de base visual; adapta parámetros y método al caso real en el espacio de trabajo del análisis.

Comprueba dependencias existentes antes de ejecutar. `requirements.txt` registra versiones verificadas del ejemplo; úsalo en un entorno de trabajo cuando haga falta, sin imponer estas versiones a proyectos existentes. `requirements-did.txt` declara `differences` para ATT por cohorte–período y `requirements-causalml.txt` declara CausalML; ambas son dependencias opcionales que no deben combinarse automáticamente con los pins básicos; resuelve compatibilidad en el entorno del análisis y registra versiones ejecutadas. Guarda datos, entornos y resultados del usuario fuera de la carpeta de la skill. Registra versiones, transformaciones, muestras y parámetros relevantes.

## Tablas y gráficos

En archivos Markdown, escribe fórmulas en línea con `$...$` y ecuaciones en bloque con `$$...$$`; coloca los delimitadores de bloque en líneas independientes, separados del texto por líneas en blanco.

Elige cada gráfico por la pregunta que resuelve: DAG o cronología para identificación; soporte, balance y pesos para comparabilidad; poder y MDE para planificación; event study para dinámica; RD para un umbral; sensibilidad para amenazas específicas. Identifica datos, grupos, unidades, muestra, parámetros y método de incertidumbre. Explica qué evidencia aporta y qué supuesto queda abierto.

Usa fondo blanco, tipografía serif, matemática coherente, trazos discretos y colores distinguibles también por estilo de línea. Prefiere tablas de estilo booktabs, con unidades y notas, sin líneas verticales. Exporta versiones vectoriales y vistas previas cuando sean útiles. Revisa legibilidad, acentos, recortes, escalas y notas a tamaño de publicación. Activa LaTeX externo únicamente si hay una instalación utilizable y aporta una necesidad concreta; Mathtext permite un estilo académico sin TeX externo.

## Entrega

Según el alcance, devuelve una recomendación o un informe que incluya pregunta y estimando; argumento de identificación; supuestos y amenazas priorizadas; decisiones recomendadas y evidencia pendiente; plan o resultados de poder e inferencia; sensibilidad y alcance de la conclusión. Incluye código, tablas y figuras reproducibles cuando correspondan. Distingue resultados ejecutados de propuestas de análisis.
