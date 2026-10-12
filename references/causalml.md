# CausalML en el asesor causal

Usa [CausalML](https://github.com/uber/causalml) cuando la pregunta requiera estimar heterogeneidad del efecto, comparar estrategias de uplift o evaluar una regla de tratamiento. Selecciona el método después de formular la identificación. Esta referencia orienta la elección, el uso de la API y la revisión de resultados; verifica las firmas y capacidades de la versión instalada antes de ejecutar código. Fuentes oficiales consultadas el 12 de octubre de 2026.

## Objetivo y condiciones de interpretación

El efecto condicional es

$$
\tau(x)=E[Y(1)-Y(0)\mid X=x].
$$

El CATE describe un promedio condicional. Una predicción para una persona con covariables x no revela su diferencia individual de resultados potenciales. Ni siquiera un experimento observa ambos resultados potenciales de una misma persona.

Para ajuste observacional, justifica consistencia, intercambiabilidad condicional y positividad para la población objetivo. Distingue covariables de ajuste de modificadores del efecto; no elimines confusores por baja importancia predictiva. En experimentos, respeta el mecanismo de asignación y distingue ITT de recepción. Examina pérdidas e interferencia. La flexibilidad del modelo de resultados no elimina estos requisitos.

Si el efecto se identifica por DiD, RD o IV, conserva sus supuestos, población y variación identificadora. Un meta-learner de ajuste convencional no reemplaza esa estrategia. Si se considera un módulo específico de la biblioteca, comprueba qué parámetro identifica y qué supuestos adicionales necesita.

## Elección de estimador

La [metodología oficial](https://causalml.readthedocs.io/en/stable/methodology.html) describe familias que conviene comparar según el tamaño de muestra por brazo, el resultado y la complejidad de la heterogeneidad. Usa una base simple y una alternativa justificada; compara con una misma evaluación fuera de muestra. No selecciones por la magnitud del efecto ni por su significación.

| Familia | Uso a considerar | Punto de atención |
|---|---|---|
| S-learner | Modelo de resultados que incorpora tratamiento y covariables | La regularización puede atenuar interacciones relevantes; comprobar heterogeneidad recuperada |
| T-learner | Modelos de resultados separados por brazo | Los brazos pequeños y la extrapolación pueden generar diferencias inestables |
| X-learner | Aprendizaje de efectos a partir de resultados imputados | Considerar desequilibrio entre brazos, soporte y modelos auxiliares |
| R/DR learners | Aprendizaje con modelos auxiliares de resultado y asignación | Verificar uso de propensión, particiones y condiciones del procedimiento; no prometer robustez frente a confusión no medida |
| Árboles y bosques causales/uplift | Segmentación y relaciones no lineales | Comprobar muestra por brazo en hojas, regularización y separación de selección y estimación |

La [API oficial](https://causalml.readthedocs.io/en/stable/causalml.html) incluye `BaseSRegressor`, `BaseTRegressor`, `BaseXRegressor`, `BaseRRegressor` y `BaseDRRegressor`, así como variantes para clasificación. También incluye `CausalTreeRegressor`, `CausalRandomForestRegressor`, `UpliftTreeClassifier` y `UpliftRandomForestClassifier`. Verifica el soporte de resultado, múltiples brazos, propensión e intervalos de la clase concreta; las capacidades no son universales.

## Preparación y particiones

- Define grupo de control, etiquetas y orden de brazos, variables anteriores al tratamiento y escala del resultado. En resultados binarios, explica la escala del efecto estimado; evita confundir probabilidad de respuesta con incremento causal.
- Audita faltantes y soporte, y decide su tratamiento antes de modelar. Entrena transformaciones, imputación, selección de variables y tuning usando exclusivamente las particiones de entrenamiento.
- Separa entrenamiento, selección de modelos y evaluación final. Si las unidades se repiten, están agrupadas o tienen estructura temporal, construye particiones que respeten esa dependencia y el escenario de aplicación. Un split aleatorio por fila no basta en esos casos.
- Para métodos que requieren predicciones de modelos auxiliares fuera de muestra, comprueba o implementa cross-fitting congruente con el diseño. Cross-fitting y un holdout externo cumplen funciones diferentes; no los presentes como intercambiables ni asumas que toda clase los incorpora automáticamente.
- Cuando el algoritmo use propensión, en un ensayo considera las probabilidades conocidas de asignación, incluidas estratificación o múltiples brazos. En observacionales, estima y diagnostica propensión según el análisis. Documenta cualquier clipping o trimming y sus efectos sobre población y estimando.

Un detalle relevante de la implementación: en el [T-learner documentado](https://causalml.readthedocs.io/en/stable/_modules/causalml/inference/meta/tlearner.html), `p` no se utiliza en el ajuste. Pasarlo no convierte al método en un estimador ponderado por propensión. El T-learner ajusta resultados por covariables mediante modelos separados y necesita sus condiciones de identificación y estimación.

## Ejemplo de API: tratamiento binario y resultado continuo

Este ejemplo supone observaciones independientes, seguimiento completo y un argumento de identificación ya formulado. `X`, `A` e `Y` son arrays alineados; X contiene únicamente covariables justificadas y codificadas, A usa 0 para control y 1 para tratamiento. La partición es ilustrativa y debe adaptarse al diseño. Los hiperparámetros son un punto de partida, no valores optimizados.

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from causalml.inference.meta import BaseTRegressor

assert set(np.unique(A)) == {0, 1}
X_train, X_test, a_train, a_test, y_train, y_test = train_test_split(
    X, A, Y, test_size=0.30, stratify=A, random_state=42
)
model = BaseTRegressor(
    control_name=0,
    learner=RandomForestRegressor(
        n_estimators=200, min_samples_leaf=20, random_state=42
    ),
)
model.fit(X=X_train, treatment=a_train, y=y_train)
pred = np.asarray(model.predict(X=X_test))
assert pred.shape == (len(y_test), 1)  # contraste 1 frente a 0
cate = pred[:, 0]
assert np.isfinite(cate).all()
evaluation = pd.DataFrame({"y": y_test, "w": a_test, "T-learner": cate})
```

La tabla contiene resultados observados y predicciones reservadas para evaluación. Promediar CATE predicho describe una agregación dependiente del modelo en esa muestra; justifica su relación con la población objetivo y el estimando. No construyas un IC de ATE usando solamente la dispersión de estas predicciones dividida por raíz de n.

## Evaluación e incertidumbre

En datos reales, un error predictivo bajo de Y no prueba buen desempeño causal. Usa validación externa, estabilidad y sensibilidad bajo supuestos explícitos. La [guía oficial de validación](https://causalml.readthedocs.io/en/stable/validation.html) ofrece evaluaciones con simulación, comparación de estimadores y curvas de uplift. En simulaciones con efectos conocidos puedes calcular error del CATE o PEHE y error del ATE; no calcules estas métricas tratando como verdad una predicción estimada en datos reales.

Para ranking, examina uplift, ganancia y Qini/AUUC fuera de muestra. Explica definición, normalización, población y comparador. Estas métricas de ordenamiento no demuestran calibración del CATE ni descartan confusión. En observacionales o probabilidades de asignación variables, justifica una evaluación ajustada apropiada; no atribuyas automáticamente interpretación causal a diferencias brutas entre tratados y controles en subconjuntos seleccionados.

En un experimento con asignación aleatoria de probabilidad constante, puede examinarse el siguiente cálculo de Qini en el holdout del ejemplo:

```python
from causalml.metrics import get_qini

# No hay columna tau_true: se evalúa con resultados y asignación observados.
curve = get_qini(
    evaluation, outcome_col="y", treatment_col="w",
    treatment_effect_col="tau_true", normalize=False
)
```

El [código oficial de métricas](https://causalml.readthedocs.io/en/stable/_modules/causalml/metrics/visualize.html) interpreta `treatment_effect_col` como efecto verdadero cuando esa columna existe. Resérvala para una verdad conocida, por ejemplo de una simulación; no pongas allí CATE predicho. Mantén las predicciones en columnas de modelo y evita otras columnas que puedan ser interpretadas como modelos.

Para intervalos, verifica qué devuelve `estimate_ate`, `return_ci` o la rutina de la clase: estimando, nivel, procedimiento, muestra y supuestos. No generalices capacidades entre clases o versiones. Un bootstrap por filas puede ser inadecuado para clusters; justifica la unidad de remuestreo, la repetición de ajuste y selección, y sus condiciones de validez. No presentes intervalos de CATE como cobertura de efectos individuales ni como bandas simultáneas sin una construcción específica. Para subgrupos y reglas de tratamiento elegidos con datos, considera selección, multiplicidad y evaluación independiente.

Las rutinas de sensibilidad o placebos requieren una amenaza y una interpretación sustantivas. Que una perturbación deje estable el resultado no certifica ausencia de sesgo no medido.

## Gráficos y tablas académicas

Prepara una tabla de modelos con estimando, muestra por brazo, particiones, ajuste de propensión, métricas e incertidumbre. Usa histogramas de CATE como distribución de predicciones; gráficos por subgrupo con estimación e incertidumbre adecuadas; soporte de propensión; y curvas de uplift/Qini para ranking cuando su evaluación esté justificada. Incluye una base simple y tamaños de muestra. Justifica cualquier resumen de importancia de variables como interpretación del modelo, no como identificación de mecanismos causales.

El módulo de métricas documentado puede modificar el estilo de Matplotlib al importarse. Aplica `assets/paper.mplstyle` después de importar CausalML y antes de crear figuras. Puedes calcular las curvas con CausalML y dibujarlas directamente con Matplotlib para conservar tipografía, unidades y notas coherentes. Exporta tablas numéricas y LaTeX y figuras vectoriales con vistas previas cuando corresponda.

## Dependencias y reproducción

Comprueba primero el entorno del análisis y la versión instalada de `causalml`. La [instalación oficial](https://causalml.readthedocs.io/en/stable/installation.html) recomienda pip o conda; las versiones documentadas actualmente requieren Python 3.11 o posterior. Reconfirma esta condición para la versión elegida. Ciertos módulos neuronales necesitan extras adicionales.

`requirements-causalml.txt` declara el recurso opcional. Resuélvelo en un entorno del proyecto, comprueba compatibilidad e importación y registra las versiones que realmente se ejecutaron. No combines a ciegas esa instalación con los pins del ejemplo básico de poder. Instala extras únicamente cuando el método solicitado los necesite. Conserva semillas, particiones, reglas de preprocesamiento, mapeo de brazos y definición de métricas.

Este módulo añade orientación y ejemplos contrastados con documentación y código fuente. No implica que CausalML se haya instalado ni ejecutado en el equipo. Al realizar un análisis, informa qué código se ejecutó y qué resultados permanecen propuestos.

## Propensity score matching

Para matching con CausalML, consulta [PSM](psm.md): selección sobre observables, población retenida, balance, calipers, pares/pesos, inferencia y sensibilidad. `NearestNeighborMatch` y `create_table_one` apoyan la etapa de diseño; no equivalen a un meta-learner ni certifican un IC del efecto. Distingue la muestra emparejada de la estructura de pares necesaria para el análisis posterior.
