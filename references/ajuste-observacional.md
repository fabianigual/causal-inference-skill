# Ajuste observacional: estandarización, IPW y AIPW

Usa esta guía para efectos promedio identificados mediante covariables observadas. Define primero ATE o ATT, población, horizonte y conjunto de ajuste. Justifica consistencia, intercambiabilidad y soporte pertinentes con [identificación](identificacion.md). La elección entre modelos no resuelve confusión no medida.

## Elegir el procedimiento

Sea $e(X)=P(A=1\mid X)$ y $m_a(X)=E[Y\mid A=a,X]$.

| Procedimiento | Qué debe justificar y comprobar |
|---|---|
| Estandarización | Modelar resultados por brazo y promediar contrastes sobre la población objetivo; examinar especificación y extrapolación |
| IPW | Estimar o conocer propensión; definir pesos para el estimando, normalización, balance y concentración por brazo |
| AIPW | Combinar modelos de resultado y propensión; comprobar condiciones de consistencia e inferencia, particiones y soporte |
| Matching | Definir comparación, retención y estimando; seguir la guía [PSM](psm.md) para pares, pesos e inferencia |

Para ATE, IPW usa pesos $1/e(X)$ en tratados y $1/[1-e(X)]$ en controles. Para ATT, una construcción usual deja peso 1 en tratados y $e(X)/[1-e(X)]$ en controles, con normalización coherente. No intercambies estas poblaciones ni confundas pesos de tratamiento con pesos de muestreo o censura. Si se combinan, deriva qué distribución representa el producto.

El ATT puede identificarse bajo intercambiabilidad de la media de Y(0) y soporte de controles para los tratados; no requiere automáticamente todas las condiciones del ATE. Define el ajuste necesario para ese objetivo y reporta exclusiones.

## AIPW e inferencia con modelos flexibles

Para ATE binario, una construcción habitual promedia:

$$
\widehat\psi_i=\widehat m_1(X_i)-\widehat m_0(X_i)
+\frac{A_i\{Y_i-\widehat m_1(X_i)\}}{\widehat e(X_i)}
-\frac{(1-A_i)\{Y_i-\widehat m_0(X_i)\}}{1-\widehat e(X_i)},
\qquad \widehat\tau=\frac1n\sum_i\widehat\psi_i.
$$

Bajo identificación, soporte y regularidad, la doble robustez de consistencia permite que sea correcto el modelo de propensión o el conjunto de modelos de resultados. No significa robustez a confusión no medida, ni garantiza que cualquier IC conserve cobertura cuando uno de los modelos falla. Verifica teoría de inferencia para la forma de ajuste y el escenario de especificación usados.

Con ML, considera cross-fitting: estima modelos auxiliares sin la observación evaluada, incluyendo preprocesamiento y tuning, y combina contribuciones fuera de muestra. Para datos dependientes, define particiones y varianza que respeten esa dependencia. Cross-fitting reduce problemas de sobreajuste; no sustituye condiciones de convergencia, momentos y positividad. En el caso i.i.d. usual, una condición suficiente sobre el resto de segundo orden exige que el producto de errores L2 de propensión y resultado sea $o_p(n^{-1/2})$, junto con las demás condiciones del procedimiento. No impongas esa tasa como una regla universal para todo estimador o diseño. Véase [Chernozhukov et al.](https://www.nber.org/papers/w23564).

En el caso i.i.d. con expansión asintóticamente lineal válida, la dispersión de las contribuciones de influencia permite estimar incertidumbre. No uses solo la dispersión de CATE predicho dividida por raíz de n. Con clusters, representa la dependencia en las contribuciones y en la inferencia; remuestrear filas no la incorpora.

## Soporte, selección y sensibilidad

Examina propensión por brazo, balance ponderado de covariables originales, pesos extremos y concentración sobre unidades originales. El ESS es un diagnóstico, no grados de libertad. Un score predictivamente preciso puede producir una comparación causal poco informativa.

Distingue trimming de clipping. Excluir observaciones por soporte puede cambiar la población y el estimando; documenta la regla y la retención. Truncar propensiones o pesos sin excluir observaciones puede introducir sesgo para el objetivo original y no define automáticamente un nuevo efecto causal. Justifica el compromiso y compara alternativas previstas, sin seleccionar por el resultado.

Si hay pérdidas o tratamiento repetido, consulta [selección y longitudinalidad](seleccion-longitudinal.md). Un AIPW para tratamiento puntual y seguimiento completo no cubre automáticamente esos procesos.

## Entrega y comprobación

Reporta estimando, ajuste causal, modelos auxiliares, pesos y particiones, población retenida, método de incertidumbre y sensibilidad a confusión no medida. Compara estimadores sobre la misma población cuando la comparación tenga sentido. Estabilidad entre ellos no demuestra identificación.

Para validar una implementación, usa DGP con verdad conocida y escenarios con ambos modelos correctos, solo propensión correcta, solo resultados correctos, ambos incorrectos y soporte débil. Evalúa sesgo y cobertura por separado: consistencia doblemente robusta no establece cobertura de un procedimiento de inferencia arbitrario. Esta guía no añade una implementación AIPW validada; selecciona y comprueba la que corresponda al análisis.
