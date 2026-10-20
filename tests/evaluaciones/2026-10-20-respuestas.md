**matching_did**

No necesariamente: el emparejamiento puede haber empeorado la identificación. DiD requiere tendencias paralelas contrafactuales, no igualdad de niveles. Si los participantes tienen ingresos persistentemente mayores, igualar exactamente un ingreso anual ruidoso puede seleccionar tratados con shocks transitorios negativos y controles con shocks positivos. Su reversión posterior genera una diferencia de cambios incluso sin capacitación.

El balance perfecto de ese año no demuestra tendencias paralelas en la muestra emparejada; estas podrían ser plausibles antes y dejar de serlo después de seleccionar parejas. Reconstruiría la selección al programa y examinaría varios años de ingresos, su persistencia y shocks. Compararía el DiD original con diseños basados en covariables e historias previas sustantivamente justificadas, sin elegir por significación o apariencia del gráfico. Promedios históricos pueden reducir ruido, pero tampoco garantizan identificación.

Documentaría exclusiones, población objetivo y pesos, y usaría inferencia compatible con dependencia y emparejamiento.

**iv_incentivo**

No reportaría ese 2SLS como efecto de asistir para todos los participantes. La orientación laboral ofrece una vía por la cual la invitación puede afectar empleo sin asistencia: la exclusión está seriamente cuestionada. El sorteo respalda independencia, pero no elimina esa vía directa.

El efecto identificable por el sorteo, sujeto a seguimiento e interferencia, es el ITT de ofrecer el paquete de invitación y orientación. Para aislar capacitación necesitarías variación adicional, por ejemplo un diseño que mantenga la orientación comparable entre grupos.

Incluso con exclusión y monotonicidad defendibles, IV identificaría un LATE para quienes asisten debido a la invitación; no automáticamente el ATE ni ATT. Además, F=12 no garantiza cobertura del IC usual: corresponde revisar el diagnóstico adecuado al diseño y considerar inferencia robusta a instrumentos débiles, como Anderson–Rubin. Esa robustez no repara la violación de exclusión.

Presentaría primera etapa y forma reducida, y priorizaría el ITT del paquete.

**rd_discreta**

No basta. Miles de alumnos mejoran la precisión de las medias en cada puntaje, pero no crean observaciones arbitrariamente próximas al corte: solo hay dos valores por debajo y tres desde 60. Con soporte fijo y discreto, la continuidad por sí sola no identifica los límites laterales; necesitas supuestos adicionales sobre la forma de los resultados potenciales.

Un polinomio global de grado cuatro puede imponer prácticamente toda la extrapolación. Además, con cinco puntajes, incluir intercepto, cuatro potencias y un indicador de elegibilidad produce una especificación sin identificación separada de todos sus coeficientes.

Primero distinguiría oferta de recepción. Si no todos reciben la beca al ser elegibles, el efecto de recibirla requeriría un diseño fuzzy con primera etapa, exclusión y monotonicidad locales.

Consideraría restricciones de suavidad explícitas con inferencia o cotas que incorporen esa incertidumbre, o una ventana de aleatorización local si el mecanismo institucional la justifica. Examinaría manipulación y otras reglas en 60. No presentaría el salto significativo como evidencia causal suficiente.

**aipw_clipping**

No. La doble robustez se refiere a consistencia bajo identificación, soporte y condiciones sobre los modelos auxiliares; no garantiza cobertura de cualquier IC. Random forests y cross-fitting tampoco aseguran las tasas de convergencia y condiciones necesarias para inferencia asintótica.

Truncar propensiones a [0.1, 0.9] conservando todas las filas no define una población con overlap. Sigues promediando sobre la población original, pero modificas las correcciones de AIPW. Si las propensiones verdaderas exceden esos límites, el clipping altera incluso una propensión correctamente estimada: puede introducir sesgo cuando los modelos de resultado no son correctos. Si estos son consistentes, puede mantenerse consistencia bajo otras condiciones, sin garantizar automáticamente el IC usual.

Examinaría soporte, proporción afectada, pesos y sensibilidad al clipping. Para un efecto en una población con overlap, definiría explícitamente una restricción poblacional o ponderación y derivaría el estimador correspondiente. Reportaría por separado el cambio de estimando y las condiciones de inferencia; ninguna alternativa resuelve confusión no medida.

**perdidas**

No automáticamente. Las pérdidas diferenciales alertan sobre selección, pero sus tasas no determinan por sí solas la magnitud ni dirección del sesgo. El objetivo natural del ensayo es el efecto de asignación —ITT— en toda la muestra asignada, distinto del efecto de recibir tratamiento.

Imputar usando solo edad y sexo exige justificar que, dado el tratamiento y la información pertinente, los resultados faltantes sean comparables a los observados. La aleatorización no garantiza esa ignorabilidad de las pérdidas. Incluiría asignación, predictores basales del resultado, razones de pérdida e interacciones relevantes en un modelo compatible con el análisis. Una imputación única tampoco representa adecuadamente la incertidumbre.

Consideraría imputación múltiple o ponderación por observación bajo supuestos explícitos y positividad de seguimiento. Complementaría con sensibilidad a pérdidas no ignorables y, si procede, cotas. Las cotas de Lee requieren selección monotónica y normalmente corresponden a quienes serían observados bajo ambas asignaciones, no al ATE original.

Sin esos supuestos, presentaría identificación parcial o resultados condicionados a escenarios.

**tratamiento_longitudinal**

Una regresión convencional ajustada por todos los ingresos mensuales no identifica automáticamente el efecto total del régimen sostenido. Los ingresos actuales son consecuencia del subsidio previo y confusores de renovaciones posteriores: ajustarlos puede bloquear parte del efecto o introducir selección; omitirlos deja confusión para exposiciones posteriores.

Definiría el contraste, por ejemplo recibir subsidio cada mes durante seis meses frente a no recibirlo durante ese período, con elegibilidad y seguimiento alineados desde el inicio. Distinguiría ese régimen sostenido de una regla dinámica de renovación según ingresos.

Consideraría g-fórmula longitudinal o un modelo estructural marginal con ponderación por las probabilidades mensuales de tratamiento y, si corresponde, censura. Ambos requieren consistencia, intercambiabilidad secuencial dada la historia y positividad.

Revisaría especialmente esta última: si la renovación es determinista según ingresos, ciertas trayectorias podrían ser imposibles en algunos historiales y el contraste sostenido no estar identificado sin extrapolación. Evaluaría entonces una política dinámica factible. No clasificaría retrospectivamente a las personas como “tratadas seis meses” desde el inicio.

**politica**

El mejor Qini no demuestra mayor beneficio neto frente a la política actual. Evalúa ranking bajo determinadas condiciones; no determina el umbral óptimo, la calibración causal ni el costo de tratar.

Además, al probar umbrales y elegir 20% en el conjunto de prueba, lo convertiste en una muestra de selección. Su evaluación posterior será optimista si se trata la regla como previamente fijada.

Congelaría la regla, sus costos y restricciones, y conseguiría una evaluación independiente. Definiría el valor neto esperado de cada política en la misma población y horizonte, valorando resultados y costos en unidades comparables. Estimaría la diferencia frente a la política vigente mediante evaluación IPW o doblemente robusta, justificando asignación, soporte, confusión y dependencia; usaría la covarianza entre ambas estimaciones para el intervalo de la diferencia.

Separaría incertidumbre condicional a la regla fijada de incertidumbre del proceso de aprendizaje. Un ensayo prospectivo que compare ambas políticas sería una validación directa. La conclusión debería basarse en beneficio neto incremental e incertidumbre, no solo en Qini.

**ensayo_pares**

No debes permutar personas: se asignaron municipios dentro de pares. Las 12.000 personas no generan 12.000 asignaciones independientes. La prueba debe intercambiar las etiquetas de tratamiento entre los dos municipios de cada par, conservando la estructura del diseño.

Con tres pares hay solamente \(2^3=8\) asignaciones posibles, suponiendo sorteos independientes y equiprobables. Una prueba exacta no aleatorizada tiene valores p múltiplos de 1/8: el mínimo unilateral es 0,125. Para el contraste bilateral habitual basado en valor absoluto y simetría, el mínimo es 0,25. Por tanto, ese diseño no permite obtener p<0,05 mediante esas pruebas exactas.

Además, la prueba exacta de ausencia de efecto para todas las unidades —nulo agudo— no equivale a una prueba exacta de efecto promedio cero bajo heterogeneidad.

Reestimaría el contraste respetando pares y aclarando si se promedian municipios o personas. Reportaría estimación y limitaciones de incertidumbre. El p<0,01 de una regresión que ignora la asignación no confirma el efecto promedio positivo.

Archivos consultados: `SKILL.md`; `references/identificacion.md`, `references/did.md`, `references/psm.md`, `references/iv.md`, `references/rd.md`, `references/ajuste-observacional.md`, `references/seleccion-longitudinal.md`, `references/causalml.md`, `references/experimentos.md` y `references/poder-inferencia.md`. No consulté material del evaluador ni modifiqué archivos. No informo versión de modelo ni configuración no observables.
