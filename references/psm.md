# Propensity score matching: diseño, soporte e inferencia

Usa esta guía cuando se proponga PSM, se revise una muestra emparejada o se busquen controles observacionales comparables. Empieza por selección y covariables; el algoritmo viene después. Diferencia matching de ponderación IPW, estratificación y uso de la propensión en meta-learners.

Lectura rápida: [identificación](#1-identificación-y-población-objetivo), [matching](#3-diseñar-el-matching), [balance](#4-diagnosticar-comparabilidad), [intervalos](#6-intervalos-y-puntos-de-atención), [poder y sensibilidad](#7-poder-y-sensibilidad), [Python/CausalML](#8-causalml-y-python), [PSM + DiD](#9-psm-combinado-con-did).

## 1. Identificación y población objetivo

Define tratamiento binario $A$, resultado y horizonte, elegibilidad y covariables previas $X$. La propensión es:

$$
e(X)=P(A=1\mid X).
$$

El verdadero score balancea covariables observadas: $A\perp X\mid e(X)$. Bajo intercambiabilidad condicional, consistencia y soporte pertinente, puede usarse para identificar efectos. Emparejar por un score estimado no garantiza balance en una muestra finita ni controla confusores ausentes. Esta es la distinción central de [Rosenbaum y Rubin (1983)](https://doi.org/10.1093/biomet/70.1.41).

Para ATT suele bastar justificar la media contrafactual $E[Y(0)\mid A=1,X]=E[Y(0)\mid A=0,X]$ y que haya controles en el soporte de los tratados, $e(X)<1$ allí. Para ATE se necesita soporte de ambos brazos en la población objetivo, además de las condiciones para ambos resultados potenciales. Examina interferencia y versiones del tratamiento. La selección del diseño requiere contexto; consulta [identificación](identificacion.md).

Si se descartan tratados sin comparación, reporta el efecto objetivo para la población retenida y las condiciones bajo las que podría generalizarse. No etiquetes automáticamente el resultado como ATT de todos los tratados o ATE. Describe características de retenidos y excluidos, y qué pregunta queda fuera del alcance.

## 2. Covariables y modelo de propensión

Reconstruye asignación con un DAG o una cronología. Prioriza causas previas del tratamiento y del resultado, y variables basales relevantes para pronóstico. No incluyas mediadores ni colisionadores por estar disponibles; una variable previa tampoco es automáticamente adecuada. Variables que predicen fuertemente tratamiento pero no resultado pueden empeorar soporte y precisión; evalúa su papel sustantivo.

Separa decisiones de diseño de resultados posteriores: define modelos, calipers y criterios de balance sin escogerlos por el efecto estimado o su significación. Un resultado **previo** puede ser una covariable útil. Evita fuga temporal, identificadores sin significado causal y datos posteriores al momento cero.

Empieza con un modelo interpretable, por ejemplo logístico, y añade no linealidades o interacciones justificadas si el balance lo requiere. Puedes usar ML, documentando preprocesamiento y selección. AUC alta mide predicción de asignación; no es el objetivo del diseño ni demuestra comparabilidad. Un modelo que separa casi perfectamente los brazos puede revelar ausencia de soporte. Trata faltantes con una estrategia explícita; eliminar filas puede cambiar la población.

## 3. Diseñar el matching

| Decisión | Qué registrar y revisar |
|---|---|
| Restricciones exactas | Variables basales que deben coincidir, y disponibilidad dentro de cada estrato |
| Distancia | Score bruto, logit del score o distancia sobre covariables; unidades y estandarización |
| Caliper | Umbral, escala y SD de referencia; sensibilidad a alternativas previstas |
| Ratio | 1:1, 1:k o variable; número real de controles por tratado |
| Reemplazo | Reutilización de controles, sus pesos y dependencia resultante |
| Orden y empates | Algoritmo greedy/óptimo, semilla y reglas reproducibles |
| Restricción de soporte | Regla y población excluida; no borrar casos buscando significación |

A modo de escenario inicial puede explorarse un caliper de 0.2 SD del logit; no es una regla universal. Define qué SD y qué población se usan. PSM greedy puede perder buenos emparejamientos por el orden, y podar más puede empeorar balance. Compara matching exacto, distancias sobre covariables u optimización de balance si encajan con la pregunta. [King y Nielsen (2019)](https://gking.harvard.edu/publication/why-propensity-scores-should-not-be-used-for-matching/) documentan problemas del uso de PSM como poda; evalúa resultados del diseño concreto.

Conserva identificadores originales, tabla de pares o conjuntos, distancias, pesos, tratados descartados y controles reutilizados. Los datos emparejados por sí solos pueden perder la estructura necesaria para inferencia. Restricciones geográficas o temporales deben responder a comparabilidad y exposición, sin ajustar por variables afectadas por tratamiento.

Un score constante no implica falta de soporte: con probabilidades de asignación iguales puede ser el valor correcto. En ese caso, los candidatos empatan; registra la regla de desempate y revisa covariables originales. El ejemplo autocontenido admite coincidencias exactas con caliper absoluto cero. Esto no convierte un score constante mal especificado en evidencia de comparabilidad.

## 4. Diagnosticar comparabilidad

Reporta balance antes/después en covariables originales, no solo en propensión. Usa diferencias estandarizadas, prevalencias, distribuciones, interacciones relevantes y varianzas. Los p-valores de diferencias basales dependen del tamaño muestral y no son el criterio de balance. Un umbral $|SMD|<0.1$ es orientativo, no una prueba de ausencia de sesgo. Estas herramientas y sus límites se discuten en [Austin (2009)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3472075/).

Para comparar antes/después con una escala estable, fija un denominador pre-matching, por ejemplo:

$$
s_{ref,j}=\sqrt{(s_{T,j,pre}^2+s_{C,j,pre}^2)/2},
\qquad
SMD_{j,post}=\frac{\bar X_{T,j,post}^{w}-\bar X_{C,j,post}^{w}}{s_{ref,j}}.
$$

Declara la convención, especialmente para variables binarias. Descompón categorías en indicadores y revisa categorías raras. Si la varianza de referencia es cero, informa esa condición: no fabriques un SMD cero ante una diferencia. Usa pesos de matching cuando corresponda.

Visualiza soporte de propensión antes y después, retención por covariables clave y distancias. Cuantifica tratados retenidos/excluidos, controles únicos, ratio logrado y reutilización. Para pesos positivos, $ESS=(\sum_i w_i)^2/\sum_i w_i^2$ describe concentración sobre **unidades originales**. Es un diagnóstico; no proporciona grados de libertad ni reemplaza el poder o la varianza del estimador.

Si queda desbalance importante, vuelve al diseño o limita la conclusión. No ajustes automáticamente el resultado hasta conseguir significación; una regresión posterior debe tener un objetivo y condiciones explícitos.

## 5. Estimación del efecto

Con $\mathcal T_M$ como tratados retenidos y $\mathcal J(i)$ sus controles, pesos $w_{ij}\ge0$ que suman uno para cada tratado:

$$
\widehat\tau_M=\frac{1}{N_{T,M}}\sum_{i\in\mathcal T_M}
\left(Y_i-\sum_{j\in\mathcal J(i)}w_{ij}Y_j\right).
$$

Un control reutilizado recibe peso agregado por sus usos. Si el ratio varía, promediar todas las filas control sin esos pesos puede producir otro contraste. Reporta el estimando y condiciones para interpretar causalmente esta estimación. Un ajuste de resultados adicional no convierte automáticamente PSM en un estimador doblemente robusto.

Para resultado binario, distingue diferencia marginal de riesgos, razón de riesgos y odds ratio; no intercambies un coeficiente logístico condicional con un efecto marginal. Para tiempo hasta evento, define horizonte, censura y medida de efecto antes del modelo.

## 6. Intervalos y puntos de atención

La incertidumbre debe reflejar método de matching, propensión estimada, pesos, reutilización y muestreo. No uses el IC de dos muestras independientes sobre filas emparejadas o duplicadas. En 1:1 sin reemplazo, un análisis de diferencias por par puede ser adecuado **bajo condiciones específicas**; no justifica por sí solo toda la incertidumbre de haber construido esos pares.

[Abadie e Imbens (2008)](https://doi.org/10.3982/ECTA6474) muestran que el bootstrap ordinario de remuestrear y volver a emparejar puede fallar para matching por vecinos con número fijo. Elige varianza analítica o un procedimiento de remuestreo con teoría aplicable al estimador. No extiendas esa prohibición a todo método denominado matching. [Abadie e Imbens (2016)](https://doi.org/10.3982/ECTA11293) muestran que estimar la propensión afecta la distribución del estimador; no la trates automáticamente como conocida.

Con controles compartidos entre pares, agrupar solo por par no elimina dependencia entre pares. Con escuelas o municipios, conserva además el nivel de dependencia original. Explica si la inferencia es condicional al diseño emparejado o incorpora su construcción. Si la implementación solo empareja y calcula balance, no atribuyas a esa salida un IC causal validado.

## 7. Poder y sensibilidad

Planifica a partir de efecto relevante, distribución de covariables, selección, soporte, ratio, pérdidas y método de inferencia. Simula **toda** la secuencia: población, tratamiento, score estimado, matching, exclusiones, resultados y análisis previsto. Mide error tipo I, cobertura, sesgo, poder y tratados retenidos; incluye error Monte Carlo y escenarios de soporte débil. Con efectos heterogéneos, define si la verdad de cada repetición corresponde a los tratados retenidos o a una población fija; no evalúes cobertura contra un ATT distinto del objetivo estimado. Una fórmula de dos brazos que ignora la poda y reutilización puede ser engañosa.

Para un diseño de pares independientes ya especificado y diferencia con SD $\sigma_d$, una aproximación inicial es:

$$
\mathrm{MDE}\approx(z_{1-\alpha/2}+z_{1-\beta})\,\sigma_d/\sqrt{N_{pares}}.
$$

Es planificación condicional a ese diseño de pares y su varianza supuesta. No es una fórmula general para PSM estimado ni permite sustituir $N_{pares}$ por ESS. Véase [poder e inferencia](poder-inferencia.md).

Evalúa confusión no medida con una sensibilidad congruente con el diseño. En el marco apropiado de estudios emparejados, $\Gamma$ puede acotar diferencias en odds de asignación por factores no observados; reporta contraste, supuestos y umbral relevante, siguiendo a [Rosenbaum (1987)](https://doi.org/10.1093/biomet/74.1.13). No lo interpretes como cantidad de sesgo observada. Compara especificaciones justificadas y otros estimadores con el mismo objetivo y población; estabilidad no demuestra identificación.

## 8. CausalML y Python

CausalML proporciona `NearestNeighborMatch` y `create_table_one`. En el [código documentado](https://causalml.readthedocs.io/en/stable/_modules/causalml/match.html), el caso sin reemplazo admite una columna; el caliper usa su SD. Para explorar logit, pásalo explícitamente:

```python
import numpy as np
from causalml.match import NearestNeighborMatch, create_table_one

# df tiene índice único; propensity está estimada usando covariables basales.
assert df.index.is_unique
assert np.isfinite(df["propensity"]).all()
assert df["propensity"].between(0, 1, inclusive="neither").all()
diseno = df.assign(logit_ps=np.log(df.propensity / (1 - df.propensity)))
matcher = NearestNeighborMatch(caliper=0.2, replace=False, ratio=1,
                               random_state=42)
matched = matcher.match(data=diseno, treatment_col="treated", score_cols=["logit_ps"])
balance = create_table_one(matched, treatment_col="treated", features=covariables)
```

Revisa la versión instalada, agotamiento de controles y estratos pequeños. La salida es una muestra, no una tabla de pares ni un IC. `create_table_one` recalcula su denominador: usa una convención fija para comparar SMD. Es un esquema de API, no una ejecución validada de CausalML.

El [ejemplo de diagnósticos](../scripts/ejemplo_psm_diagnosticos.py) es autocontenido con dependencias básicas: estima un logit sintético, realiza matching greedy 1:1 sin reemplazo y conserva pares. Exporta balance con denominador fijo, retención, distancias y gráficos PNG/SVG. Ilustra la fase de diseño sin estimar un impacto ni asignarle un IC.

Figuras pertinentes: Love plot de balance; soporte por brazo antes/después; distribuciones de covariables críticas; distancias y retención; concentración de pesos si se reutilizan controles; intervalos de sensibilidad cuando haya un procedimiento válido. Anota muestra, escala, pesos, convención de SMD y límite causal de cada diagnóstico.

## 9. PSM combinado con DiD

Emparejar con covariables e historias previas puede mejorar comparabilidad para DiD. No reemplaza tendencias paralelas condicionales, ausencia de anticipación ni disponibilidad de controles sin exposición. Define el matching en el pre, conserva la estructura longitudinal y pesos, y aplica una inferencia adecuada a ambas etapas. No emparejes usando resultados posteriores. Un DiD doblemente robusto tiene una construcción específica, como la de [Sant’Anna y Zhao (2020)](https://doi.org/10.1016/j.jeconom.2020.06.003); no equivale a cualquier combinación de PSM y regresión. Sigue la [guía DiD](did.md).

Antes de emparejar resultados previos o sus tendencias, examina persistencia, ruido transitorio y selección. Igualar niveles basales ruidosos entre grupos con diferencias persistentes puede introducir regresión a la media y sesgar un DiD que era válido sin matching. Justifica tendencias paralelas para la población emparejada; el balance del pre no establece ese supuesto. [Daw y Hatfield (2018)](https://onlinelibrary.wiley.com/doi/10.1111/1475-6773.12993) estudian esta amenaza. Compara diseños defendibles por el contexto, sin escoger el que produzca trayectorias visualmente más parecidas.

## 10. Entrega del asesor

Incluye pregunta y población objetivo, argumento de selección, covariables y temporalidad, algoritmo completo, balance y soporte, pérdidas de población, estructura de pares/pesos, estimación e inferencia justificadas, poder y sensibilidad. Si no hay controles comparables o confusores decisivos están ausentes, explica qué puede describirse y qué información permitiría mejorar la evaluación.
