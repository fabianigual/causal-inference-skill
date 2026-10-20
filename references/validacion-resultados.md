# Resultados de validación

Registro del 20 de octubre de 2026. Distingue pruebas numéricas, ejecución de ejemplos y comportamiento del asesor. Estos resultados corresponden al alcance descrito; no certifican cualquier análisis que use la skill.

## Cálculos y ejecución

Se ejecutó `python -m unittest discover -s tests -v`: 11 pruebas aprobadas. La batería de [pruebas metodológicas](../tests/test_metodologia.py) incluye:

- 100 comparaciones de Welch con SciPy bajo tamaños y varianzas distintos.
- Cinco escenarios de poder t contrastados con integración normal/chi-cuadrado independiente, incluido un efecto extremo; tolerancia relativa 10⁻⁶ y absoluta 10⁻⁹.
- Nueve cálculos de tamaño con distintos efectos y ratios, verificando poder después de redondear.
- 100 comparaciones de DiD con cuatro medias y un caso de covarianza temporal conocida.
- Scores constantes, caliper, ausencia de reutilización, falta de soporte y denominador SMD previo fijo, incluido el caso de referencia cero.
- Un ejemplo construido de efecto nulo donde matching sobre el resultado basal cambia el contraste DiD de cero a uno. Muestra una posibilidad metodológica, no la frecuencia del problema en una población real.

El ejemplo PSM se volvió a ejecutar después de corregir el score constante. Terminó correctamente y produjo 271 pares de 344 tratados, sin reutilización; los SMD posteriores fueron aproximadamente 0,005 y 0,023 para las covariables continua y binaria. Estos diagnósticos no demuestran ausencia de confusión.

En la auditoría previa a esta edición, el mismo día, se ejecutaron los tres ejemplos y seis escenarios DiD con 1.000 repeticiones cada uno. Error tipo I: 0,048–0,051; cobertura: 0,948–0,957, con MCSE de cobertura aproximado de 0,0064–0,0070. El ejemplo DiD no cambió en esta edición. La simulación impone tendencias paralelas, efecto constante y unidades independientes; no valida clusters ni adopción escalonada.

Entorno usado: Python 3.9.7, NumPy 2.0.2, pandas 2.3.3, SciPy 1.13.1, statsmodels 0.14.6, Matplotlib 3.9.4 y Jinja2 3.1.6. Estas versiones son distintas de los pins de `requirements.txt`; no se afirma reproducción exacta de ese entorno. El validador `quick_validate.py` de skill-creator aprobó la estructura con PyYAML 6.0.3. Esa comprobación no prueba corrección metodológica.

## Respuestas del asesor

Se entregaron ocho solicitudes a un agente con contexto independiente del autor de los cambios. Recibió la skill y referencias metodológicas; no recibió la auditoría ni las rúbricas. Los ocho casos se respondieron en una misma sesión, con una respuesta por caso. El autor calificó después las respuestas con cuatro criterios de 0 a 2 puntos y fallos críticos separados.

| Caso | Puntuación | Fallos críticos detectados |
|---|---:|---:|
| Matching y DiD | 8/8 | 0 |
| Invitación como instrumento | 8/8 | 0 |
| RD con puntaje discreto | 8/8 | 0 |
| AIPW y clipping | 8/8 | 0 |
| Pérdidas diferenciales | 8/8 | 0 |
| Tratamiento longitudinal | 8/8 | 0 |
| Valor de política | 8/8 | 0 |
| Ensayo con tres pares de municipios | 8/8 | 0 |

Se conservan [solicitudes y rúbricas](../tests/casos_asesor.json), [respuestas](../tests/evaluaciones/2026-10-20-respuestas.md) y [calificaciones, fundamentos y hashes de recursos](../tests/evaluaciones/2026-10-20.json). La versión exacta del modelo y los parámetros de muestreo no fueron expuestos por la herramienta y no se inventaron.

Es una comprobación de uso con casos públicos, calificada por el autor. No hay condición sin skill, repeticiones por caso ni evaluación sobre casos reservados. No permite estimar una tasa general de error ni atribuir una mejora causal a la skill. Para ampliar la evaluación, sigue [validación](validacion.md).

## Pendiente de comprobar

Las integraciones de `differences` y CausalML no se ejecutaron en esta revisión. Sus fragmentos siguen siendo esquemas de API con límites explícitos. Las nuevas guías de IV, RD, ajuste observacional, experimentos, selección y longitudinalidad no añaden estimadores ejecutables validados para esos diseños. Al incorporar implementaciones, registra versiones y comprueba estimando, sesgo, error tipo I y cobertura bajo escenarios pertinentes.
