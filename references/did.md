# Diferencias en diferencias: identificación, diseño e inferencia

Usa esta guía para asesorar un DiD, revisar uno existente o planificar su poder. Empieza por el calendario y el contrafactual. Una regresión con efectos fijos y una figura de event study son herramientas cuyo significado depende de esas decisiones.

Lectura rápida: [identificación](#2-estimando-y-argumento-de-identificación), [estimador](#4-elegir-el-estimador), [diagnósticos](#5-diagnósticos-y-amenazas-reales), [inferencia y sensibilidad](#6-inferencia-pocos-clusters-y-sensibilidad), [poder](#7-poder-y-precisión), [Python](#8-python-y-visualizaciones).

## 1. Reconstruir el problema

Precisa la unidad de intervención, observación y dependencia; primera exposición y anuncio; resultado, escala y frecuencia; población y horizonte. Pregunta por qué unas unidades entraron antes que otras y qué pasó al mismo tiempo. Distingue panel de cortes transversales repetidos y tratamiento absorbente de entradas, salidas o cambios de intensidad.

Construye una tabla unidad–período con exposición, cohorte, elegibilidad, covariables basales, resultado y disponibilidad. Revisa duplicados, fechas, unidades ya tratadas al inicio, cambios de definición y pérdidas. Produce un mapa del calendario y cuenta unidades tratadas y controles utilizables por comparación. Un dato ausente no equivale a resultado cero ni a ausencia de tratamiento.

## 2. Estimando y argumento de identificación

En el caso simple, $D=1$ indica pertenencia al grupo tratado; $t=0,1$ son pre y post. El objetivo es el ATT en el post para esa población. Consistencia, exposición bien definida y ausencia de interferencia relevante conectan resultados observados con potenciales. Sin anticipación, el pre todavía representa ausencia del programa.

El supuesto central es:

$$
E[Y_1(0)-Y_0(0)\mid D=1]
=E[Y_1(0)-Y_0(0)\mid D=0].
$$

Se refiere a la evolución **sin tratamiento**. No exige igualdad de niveles iniciales. Su plausibilidad depende de selección, contexto y shocks; observar trayectorias previas parecidas aporta evidencia limitada.

Con covariables basales $X$, puedes justificar tendencias paralelas condicionales. La comparación debe promediar cambios de controles comparables sobre la distribución de $X$ de los tratados. Introducir $X$ como términos lineales en una regresión cualquiera no garantiza ese ajuste. Examina soporte para cada comparación y evita controlar por respuestas al programa. El alcance poblacional debe seguir las restricciones de soporte. Consulta también [identificación](identificacion.md).

En adopción escalonada, $G=g$ es la primera fecha de tratamiento y $Y_t(g)$ el resultado bajo esa trayectoria:

$$
ATT(g,t)=E[Y_t(g)-Y_t(\infty)\mid G=g],\qquad t\ge g.
$$

Define controles nunca tratados o todavía no tratados, excluyendo períodos de anticipación. Justifica tendencias paralelas para esas comparaciones. La agregación debe expresar la población y el horizonte deseados; pesos por cohorte, calendario o tiempo desde adopción responden preguntas distintas. Este enfoque sigue a [Callaway y Sant’Anna (2021)](https://doi.org/10.1016/j.jeconom.2020.12.001).

## 3. Fórmulas del caso básico

$$
\widehat\tau_{DiD}
=(\bar Y_{T,1}-\bar Y_{T,0})-(\bar Y_{C,1}-\bar Y_{C,0}).
$$

Para un panel completo de unidades independientes, define $\Delta Y_i=Y_{i,1}-Y_{i,0}$. La estimación es una diferencia de medias de cambios y su error estándar es:

$$
\widehat{SE}=\sqrt{s_{\Delta,T}^2/n_T+s_{\Delta,C}^2/n_C},
\qquad
\operatorname{Var}(\Delta Y)=\sigma_1^2+\sigma_0^2-2\operatorname{Cov}(Y_1,Y_0).
$$

Puedes construir un IC de Welch sobre los cambios bajo sus condiciones. Esto conserva la covarianza pre–post; sumar cuatro varianzas independientes en un panel la omite. Si hay municipios, escuelas o shocks compartidos, esta fórmula individual deja de ser adecuada. Para cortes repetidos, documenta quién representa cada celda y estima su covarianza según el muestreo. Véase F10 y F12 en [fórmulas](formulas.md).

## 4. Elegir el estimador

| Escenario | Decisión inicial | Punto de atención |
|---|---|---|
| Dos grupos, dos períodos | Diferencia de cambios; ajuste si se justifica DiD condicional | Panel, composición y dependencia |
| Adopción común, varios períodos | Contrastes por período y agregación prevista | Referencia, anticipación y horizonte |
| Adopción escalonada, efectos heterogéneos | Estimar ATT por cohorte y período con comparaciones admisibles | Controles disponibles y pesos explícitos |
| Tratamiento reversible o intensidad variable | Reformular estimando y buscar un método para esa trayectoria | No recodificar automáticamente como primera adopción absorbente |
| Uno o pocos grupos tratados | Evaluar un diseño y una inferencia específicos | Miles de personas no crean miles de asignaciones independientes |

Con adopción escalonada, TWFE puede usar grupos ya tratados como controles y mezclar efectos de distintas cohortes y horizontes. Los leads y lags de una regresión convencional pueden contaminarse entre sí y producir aparentes pre-tendencias por heterogeneidad. Justifica cualquier uso de TWFE y considera estimadores compatibles con el objetivo; [Sun y Abraham (2021)](https://doi.org/10.1016/j.jeconom.2020.09.006) muestran el problema para event studies.

Si todas las unidades terminan tratadas, los últimos períodos pueden carecer de controles admisibles. Restringe el horizonte o explica la hipótesis adicional que permitiría extrapolar. No rellenes celdas no identificadas con cero.

## 5. Diagnósticos y amenazas reales

| Hallazgo | Qué afecta | Acción útil |
|---|---|---|
| El programa llega tras una caída del resultado | Selección temporal y posible reversión a la media | Reconstruir elegibilidad y comparar trayectorias y shocks previos |
| Anuncio anterior a implementación | Pre y controles posiblemente expuestos | Definir ventana de anticipación y revisar fechas alternativas justificadas |
| Política simultánea exclusiva de tratados | Contrafactual sin programa | Documentar la política; reconocer falta de separación si no hay variación adicional |
| Migración, pérdidas o renovación de la muestra | Población y evolución observada | Comparar composición y seguimiento por grupo y fecha |
| Beneficios hacia controles cercanos | Interferencia y contraste de exposición | Redefinir exposición, comparar distancias o justificar otra comparación |
| Cambio de medición o escala | Comparabilidad temporal y supuesto de tendencias | Armonizar datos y justificar niveles, logaritmos u otra escala |

En un event study, informa referencia omitida, cohortes y unidades que contribuyen a cada horizonte. Separa cambios de efecto de cambios en composición. Compara, cuando sea útil, una ventana común con cohortes constantes. Presenta bandas puntuales o simultáneas según la pregunta; una prueba conjunta de leads también requiere una interpretación propia.

Los pretests pueden tener poco poder y seleccionar análisis que distorsionen estimación e inferencia. No declares “se cumple tendencias paralelas” porque $p>0.05$, ni elijas controles o ventana para conseguirlo. Describe qué desviaciones admiten los intervalos y su relevancia sustantiva. Véase [Roth (2022)](https://doi.org/10.1257/aeri.20210236).

Placebos de fecha, resultados o grupos pueden revelar problemas específicos, si se justifica por qué deberían dar cero. No constituyen un certificado global. Agregar tendencias lineales por grupo cambia la extrapolación contrafactual; debe explicarse y someterse a sensibilidad.

Si construyes controles mediante matching sobre resultados previos, revisa también la [regresión a la media inducida por el emparejamiento](psm.md#9-psm-combinado-con-did). Tendencias paralelas en la población original no garantizan tendencias paralelas después de esa selección.

## 6. Inferencia, pocos clusters y sensibilidad

Identifica el nivel que comparte asignación y shocks, además de la repetición por unidad. Usa una varianza que represente esa dependencia; registra número total y tratado de clusters, desigualdad de tamaños, procedimiento y valor crítico. La inferencia asintótica puede fallar con pocos grupos o alta concentración. Un wild cluster bootstrap requiere condiciones propias; la inferencia por randomización requiere un mecanismo de asignación defendible. Ninguno sustituye controles comparables. Para el marco general, consulta [Roth et al. (2023)](https://arxiv.org/abs/2201.01194).

Evalúa sensibilidad a controles admisibles, anticipación, composición, escala, horizonte y shocks concretos. Para desviaciones de tendencias paralelas, [Rambachan y Roth (2023)](https://doi.org/10.1093/restud/rdad018) permiten inferencia bajo restricciones explícitas sobre magnitud o suavidad de las desviaciones. Reporta la restricción, su calibración sustantiva y los intervalos resultantes, incluyendo el valor en que cambia una conclusión relevante. Conserva la matriz completa de covarianza; desplazar un IC por una pendiente elegida no implementa ese método.

Las implementaciones oficiales de [HonestDiD](https://github.com/asheshrambachan/HonestDiD) son recursos en R/Stata. Si se requiere el método, usa una implementación contrastada y lleva resultados y covarianzas a Python para tablas y figuras; no inventes una API Python equivalente.

## 7. Poder y precisión

Define un efecto mínimo relevante, su dinámica y el contraste confirmatorio. En el caso independiente de dos períodos, usa la varianza de **cambios** para una aproximación inicial. Con SD común $\sigma$ y correlación pre–post $\rho$, $\sigma_\Delta^2=2\sigma^2(1-\rho)$. La correlación individual pre–post no es la ICC de un municipio.

Para un diseño real, simula el calendario de adopción, números y tamaños de grupos, shocks por grupo y fecha, autocorrelación, heterogeneidad, pérdidas y anticipación previstas. Ejecuta el estimador y el procedimiento de inferencia que se usarán, incluyendo la agregación. Mide rechazo bajo el nulo, cobertura y poder bajo alternativas. Para una tasa simulada $\hat p$ con $B$ repeticiones:

$$
MCSE(\hat p)=\sqrt{\hat p(1-\hat p)/B}.
$$

Presenta escenarios y error Monte Carlo. Aumentar personas dentro de pocos municipios puede aportar menos que sumar municipios o controles. Más períodos pueden ayudar, pero también introducir cambios de medición y exposición. Evalúa el diseño completo; no sustituyas su varianza por un efecto de diseño genérico.

## 8. Python y visualizaciones

El [ejemplo DiD](../scripts/ejemplo_did.py) ejecuta un panel sintético 2×2 de unidades independientes: diferencia de cambios, IC de Welch, simulación de poder/error tipo I/cobertura y tablas CSV/LaTeX. Produce tendencias en niveles y poder según correlación pre–post. Es una base comprobable para ese caso; no implementa adopción escalonada ni dependencia por municipios.

Para ATT por cohorte–período, considera [`differences`](https://bernardodionisi.github.io/differences/latest/), como dependencia opcional. Comprueba versión, codificación de nunca tratados y el índice unidad–tiempo antes de adaptar este esquema:

```python
from importlib.metadata import version
from differences import ATTgt

# panel: MultiIndex unidad–tiempo, cohorte constante y codificada para esta API.
# Supuestos, soporte y municipio como nivel de dependencia justificados previamente.
modelo = ATTgt(data=panel, cohort_column="cohorte",
               base_period="universal", anticipation=0)
tabla_gt = modelo.fit(formula="y", control_group="never_treated",
                      est_method="dr", cluster_var="municipio",
                      boot_iterations=999, random_state=42)
tabla_evento = modelo.aggregate("event", cluster_var="municipio",
                                boot_iterations=999, random_state=42)
print(version("differences"))
```

Es un esquema contrastado con las firmas documentadas de [constructor](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.__init__/), [fit](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.fit/) y [aggregate](https://bernardodionisi.github.io/differences/latest/api/differences.ATTgt.aggregate/); no una ejecución validada de la biblioteca. Confirma tipo de banda y manejo de clusters de la versión instalada. 999 repeticiones es un parámetro ilustrativo, no una garantía para pocos clusters.

Elige gráficos por el problema: mapa de adopción y controles disponibles; tendencias en niveles; event study con tamaños y cohortes; intervalos de sensibilidad; curvas de poder y MDE por escenarios. Usa [estilo académico](python-visualizacion.md) y notas con estimando, población, comparación, referencia y método de incertidumbre.

## 9. Entrega del asesor

Devuelve un argumento de identificación, tabla de comparaciones admisibles, amenazas priorizadas y decisiones pendientes. Adjunta especificación del estimador y agregación, diagnóstico con límites, inferencia, poder o precisión, sensibilidad y alcance poblacional. Si faltan controles o hay un shock inseparable, restringe la interpretación y explica qué evidencia adicional ayudaría.
