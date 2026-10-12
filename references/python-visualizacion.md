# 5. Python y estilo visual académico

Base propuesta: NumPy y pandas para datos; SciPy y statsmodels para cálculos e inferencia; Matplotlib para figuras. Elegir herramientas adicionales por diseño y verificar sus versiones y capacidades antes de usarlas. El nombre de una biblioteca no garantiza identificación ni inferencia válida.

Estilo: fondo blanco, tipografía serif, matemática Computer Modern, tamaños legibles al insertar la figura en una columna, líneas discretas, colores limitados con estilos de línea distinguibles en blanco y negro y leyendas breves. Tablas con aspecto booktabs, sin líneas verticales, unidades y notas sobre estimando, muestra y errores estándar. Exportar resultados numéricos y tablas LaTeX además de las versiones para lectura.

Matplotlib permite Mathtext con Computer Modern sin TeX externo. Si se requiere tipografía LaTeX completa, comprobar primero que exista una instalación utilizable y configurar `text.usetex=True`. Conservar exportación vectorial y PNG de vista previa. La estética no debe ocultar muestras pequeñas, incertidumbre ni restricciones de población.

| Pregunta | Figura pertinente | Información necesaria |
|---|---|---|
| ¿Qué supuestos conectan tratamiento y resultado? | DAG y cronología | Flechas propuestas, temporalidad y fuentes de contexto |
| ¿Hay comparación suficiente? | Soporte, balance y pesos | Población antes/después y tamaño efectivo pertinente |
| ¿Qué puede detectar este diseño? | Poder–muestra y MDE–muestra | Efecto, varianza, alpha, asignación y dependencia |
| ¿Qué precisión cabe esperar? | Semiancho de IC–muestra | Nivel, varianza y método; especificar si es planificación |
| ¿Cómo evolucionan los efectos? | Event study | Referencia, cohortes, tamaños y bandas puntuales/simultáneas |
| ¿Qué ocurre cerca del umbral? | RD con ajustes locales | Puntaje, umbral, ancho de banda y muestra usada |
| ¿Cuánto depende el resultado de una amenaza? | Curva o región de sensibilidad | Parámetro de sesgo y su justificación sustantiva |

La muestra adjunta (`../scripts/ejemplo_poder_precision.py`) compara curvas de poder de una prueba t con el MDE aproximado y el semiancho esperado de un IC normal. Es un ejercicio de planificación con parámetros supuestos; no contiene datos de una evaluación ni estima impactos.

Para reproducirla, usar las dependencias de `../requirements.txt` en un entorno de trabajo y ejecutar `python ../scripts/ejemplo_poder_precision.py --output-dir RUTA`. El script guarda todos los resultados en esa ruta y obtiene el estilo de `../assets/paper.mplstyle`. Las fórmulas de Welch se contrastaron con SciPy y statsmodels; también se verificaron tamaños de muestra, poder bajo el nulo y una cola extrema mediante integración independiente.


## Efectos heterogéneos con CausalML

Para CATE, meta-learners, árboles o bosques de uplift, usa la [referencia de CausalML](causalml.md). Selecciona algoritmo y métricas después de justificar identificación. Incorpora tablas de comparación, CATE predicho por subgrupos, soporte y curvas de uplift/Qini cuando el diseño permita evaluarlas. Distingue ranking, calibración e inferencia; aplica el estilo de paper después de los imports de CausalML que puedan cambiarlo.
