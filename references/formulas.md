# 4. Catálogo inicial de fórmulas

Notación: $A$ es tratamiento recibido, $Z$ asignación, $C$ covariables previas, $Y(a)$ resultado potencial, $n_a$ tamaño de cada brazo, $s_a^2$ varianza muestral, $z_q$ y $t_{q,\nu}$ cuantiles normal y t. Cada ficha futura debe incluir supuestos, derivación breve, parámetros, implementación, ejemplo y límites.

### F1. Estimandos básicos

$$
\tau_{ATE}=E[Y(1)-Y(0)],\qquad
\tau_{ATT}=E[Y(1)-Y(0)\mid A=1]
$$


Definen el objetivo; su definición no establece cómo identificarlo con datos observados. Precisar población, intervención y horizonte para que sean parámetros bien definidos.

### F2. Identificación mediante ajuste

$$
\tau_{ATE}=E_C\{E[Y\mid A=1,C]-E[Y\mid A=0,C]\}.
$$


La igualdad requiere consistencia, intercambiabilidad condicional ($Y(a)\perp A\mid C$) y positividad para ambos tratamientos en el soporte de la población objetivo. La ausencia de interferencia o una definición adecuada de exposición también importa. La estimación requiere además condiciones propias del procedimiento estadístico. Esto no es la fórmula universal de identificación de DiD, IV o RD.

### F3. Diferencia de medias e ITT

$$
\widehat\tau=\bar Y_1-\bar Y_0.
$$

Si los grupos están definidos por asignación aleatoria $Z$, identifica el efecto de asignación en la población correspondiente bajo las condiciones del ensayo. Comparar receptores y no receptores $A$ necesita un argumento de identificación propio. Revisar pérdidas, interferencia y versiones del tratamiento antes de interpretar causalmente.

### F4. Error estándar para dos muestras independientes

$$
\widehat{SE}=\sqrt{\frac{s_1^2}{n_1}+\frac{s_0^2}{n_0}}.
$$

Corresponde a muestras independientes con varianzas finitas; no incorpora parejas, clusters ni medidas repetidas. Para inferencia aproximada de Welch:

$$
\nu=\frac{(s_1^2/n_1+s_0^2/n_0)^2}
{(s_1^2/n_1)^2/(n_1-1)+(s_0^2/n_0)^2/(n_0-1)}.
$$

### F5. Intervalo de confianza de Welch

$$
IC_{1-\alpha}=\widehat\tau\pm t_{1-\alpha/2,\nu}\widehat{SE}.
$$

Es un intervalo aproximado bajo las condiciones del método. Su cobertura estadística no incorpora por sí sola sesgo por confusión, selección o errores de medición. El nivel de confianza describe la cobertura del procedimiento en repeticiones, no una probabilidad frecuentista del parámetro fijo dado el intervalo observado.

### F6. Poder bajo aproximación normal bilateral

Para un efecto alternativo fijo $\delta$ y un SE de planificación tratado como conocido:

$$
\lambda=\delta/SE,\qquad
\mathrm{Poder}=\Phi(-z_{1-\alpha/2}-\lambda)
+1-\Phi(z_{1-\alpha/2}-\lambda).
$$

Requiere una estadística aproximadamente normal, centrada correctamente y con la varianza supuesta. El ejemplo Python usa el cálculo de poder t para dos muestras independientes con varianza común, en lugar de esta aproximación.

### F7. MDE y tamaño muestral aproximados

Para dos brazos independientes, varianza común $\sigma^2$ y prueba bilateral:

$$
\mathrm{MDE}\approx(z_{1-\alpha/2}+z_{1-\beta})\,
\sigma\sqrt{\frac1{n_1}+\frac1{n_0}}.
$$

Con asignación equilibrada, el tamaño por brazo es:

$$
n\approx\frac{2\sigma^2(z_{1-\alpha/2}+z_{1-\beta})^2}{\delta^2}.
$$

Son aproximaciones de planificación. Para muestras pequeñas, considerar el cálculo t; para otros diseños, usar su varianza y su método de inferencia. Expresar MDE en unidades sustantivas y efecto estandarizado cuando ayude.

### F8. Efecto de diseño por clusters

$$
DE=1+(m-1)\rho.
$$

Es una corrección simple para clusters de tamaño igual $m$, ICC $\rho$ y correlación intracluster intercambiable, en el contexto de análisis apropiado. No resuelve inferencia con pocos clusters, tamaños desiguales, estructuras multinivel ni series temporales. No convertir $N/DE$ en grados de libertad ni usarlo para justificar inferencia causal.

### F9. Reclutamiento ante pérdidas

$$
n_{reclutar}\approx\frac{n_{analizar}}{1-r}.
$$

$r$ es la proporción esperada de pérdidas. Planificar por brazo y escenario. Esta inflación compensa cantidad esperada, no sesgo por pérdida selectiva; tampoco reemplaza el modelado de pérdidas en diseños complejos.

### F10. DiD de dos grupos y dos períodos

$$
\widehat\tau_{DiD}=
(\bar Y_{T,post}-\bar Y_{T,pre})
-(\bar Y_{C,post}-\bar Y_{C,pre}).
$$

Identifica un efecto sobre tratados bajo los supuestos pertinentes de tendencias paralelas, ausencia de anticipación y otras condiciones del diseño. La composición y la interferencia deben examinarse. Para inferencia, si $v=(1,-1,-1,1)'$ corresponde al orden $(Tpost,Tpre,Cpost,Cpre)$:

$$
\widehat{\mathrm{Var}}(\widehat\tau_{DiD})=v'\widehat\Sigma v.
$$

$\widehat\Sigma$ es la matriz de covarianza de las cuatro medias estimadas. Debe incorporar repetición de unidades y dependencia relevante; no sumar cuatro varianzas como si todas las celdas fueran independientes. La fórmula básica no cubre automáticamente adopción escalonada.


### F11. CATE y estimación T-learner

$$
\tau(x)=E[Y(1)-Y(0)\mid X=x],\qquad
\widehat\tau_T(x)=\widehat m_1(x)-\widehat m_0(x).
$$

$m_a(x)=E[Y\mid A=a,X=x]$. La interpretación causal requiere los supuestos pertinentes de identificación; los modelos separados añaden condiciones de estimación y soporte. CATE es un promedio condicional, no la diferencia individual observada de resultados potenciales. Para implementación y validación, consulta [CausalML](causalml.md).

### F12. DiD de panel: varianza de cambios y ATT por cohorte

$$
\Delta Y_i=Y_{i,post}-Y_{i,pre},\qquad
\widehat\tau=\overline{\Delta Y}_T-\overline{\Delta Y}_C,\qquad
\widehat{SE}^2=s_{\Delta,T}^2/n_T+s_{\Delta,C}^2/n_C.
$$

La última igualdad requiere independencia entre unidades y un panel completo sin pesos. Usa F5 sobre cambios para un IC de Welch bajo sus condiciones. No incorpora shocks compartidos entre personas de un municipio. Para planificación simple, $\operatorname{Var}(\Delta Y)=\sigma_{post}^2+\sigma_{pre}^2-2\operatorname{Cov}(Y_{post},Y_{pre})$. El [ejemplo DiD](../scripts/ejemplo_did.py) ejecuta este caso.

Para adopción absorbente escalonada:

$$
ATT(g,t)=E[Y_t(g)-Y_t(\infty)\mid G=g],\qquad
\theta=\sum_{(g,t)\in\mathcal I}\omega_{g,t}ATT(g,t),\qquad
\sum_{(g,t)\in\mathcal I}\omega_{g,t}=1.
$$

$\mathcal I$ contiene comparaciones identificables y $\omega_{g,t}\ge0$ define el objetivo agregado. Es una definición de estimando, no un estimador universal. La elección de controles, pesos, horizonte e inferencia se desarrolla en [DiD](did.md), con referencias a Callaway y Sant’Anna (2021).

### F13. Propensión y contraste de matching

$$
e(X)=P(A=1\mid X),\qquad
\widehat\tau_M=\frac{1}{N_{T,M}}\sum_{i\in\mathcal T_M}
\left(Y_i-\sum_{j\in\mathcal J(i)}w_{ij}Y_j\right),\qquad
\sum_{j\in\mathcal J(i)}w_{ij}=1.
$$

$\mathcal T_M$ son tratados retenidos; $\mathcal J(i)$ son controles de cada tratado y $w_{ij}\ge0$. Con 1:k uniforme, $w_{ij}=1/k_i$. El peso agregado de un control reutilizado es $W_j=\sum_i w_{ij}$. El contraste requiere identificación y condiciones de aproximación del matching; no proporciona automáticamente su varianza. Consulta [PSM](psm.md) para población, soporte e inferencia y las fuentes de Rosenbaum–Rubin y Abadie–Imbens.

### F14. SMD con referencia fija y concentración de pesos

$$
s_{ref,j}=\sqrt{(s_{T,j,pre}^2+s_{C,j,pre}^2)/2},\qquad
SMD_{j,m}=\frac{\bar X_{T,j,m}^{w}-\bar X_{C,j,m}^{w}}{s_{ref,j}}.
$$

$m$ indica muestra antes o después del matching. Esta convención usa una SD pre fija para comparar balance en la misma escala; hay otras convenciones que deben declararse. Para indicadores binarios, declarar el denominador utilizado. Con referencia cero, informar que el SMD no está definido. El [ejemplo PSM](../scripts/ejemplo_psm_diagnosticos.py) implementa la versión sin pesos y sin reemplazo.

$$
ESS=\frac{(\sum_i w_i)^2}{\sum_i w_i^2}.
$$

Calcular sobre unidades originales por brazo, con pesos no negativos y suma positiva. Cuantifica concentración de pesos; no es el tamaño de muestra de un experimento equivalente ni los grados de libertad de un IC.

### F15. MDE condicional de pares y error Monte Carlo

$$
\mathrm{MDE}\approx(z_{1-\alpha/2}+z_{1-\beta})\,\frac{\sigma_d}{\sqrt{N_{pares}}},
\qquad
MCSE(\hat p)=\sqrt{\hat p(1-\hat p)/B}.
$$

El MDE es una aproximación normal para un diseño de pares independientes ya especificado, con SD de diferencias $\sigma_d$ supuesta. No incorpora construcción de PSM, poda, reutilización o clusters. MCSE describe error de una tasa obtenida con $B$ repeticiones independientes; no es incertidumbre del efecto causal. Véanse [PSM](psm.md) y [DiD](did.md) para simulación del análisis completo.
