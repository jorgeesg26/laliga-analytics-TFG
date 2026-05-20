# Conclusiones del análisis de datos

Este documento recoge las principales conclusiones obtenidas durante el desarrollo de **LaLiga Analytics**, a partir del dataset limpio `laliga_clean.csv` y de las métricas calculadas en la aplicación.

## 1. Objetivo del análisis

El objetivo del análisis no era únicamente mostrar resultados de partidos, sino transformar los datos originales en información más útil para interpretar el rendimiento de los equipos de LaLiga. Para ello se calcularon métricas como puntos, goles a favor, goles en contra, diferencia de goles y rankings ofensivos y defensivos.

Además, el análisis se integró en un dashboard desarrollado con Streamlit para que los resultados pudieran consultarse de forma visual y sencilla, sin tener que trabajar directamente con los archivos CSV.

## 2. Preparación del dataset

El dataset final utilizado en el proyecto se generó a partir de varios archivos CSV, cada uno correspondiente a una temporada distinta. Durante la preparación se seleccionaron únicamente las columnas necesarias para el análisis deportivo, descartando variables que no aportaban valor directo al objetivo del proyecto.

Las columnas utilizadas incluyen información como fecha, equipo local, equipo visitante, goles, tiros, tiros a puerta, tarjetas amarillas y temporada. Después, todos los archivos se unificaron en un único dataset limpio llamado `laliga_clean.csv`.

Este proceso fue importante porque permitió trabajar con una base de datos común para todas las partes del proyecto: análisis estadístico, visualización y modelo de Inteligencia Artificial.

## 3. Conclusiones sobre el rendimiento de los equipos

Una de las conclusiones principales es que los equipos con mayor regularidad en puntos suelen mantener también una diferencia de goles positiva. En el dataset actual destacan equipos como Real Madrid, Barcelona y Atlético de Madrid, que aparecen en las primeras posiciones de la clasificación acumulada.

También se observa que el rendimiento ofensivo y el rendimiento defensivo no siempre coinciden exactamente. Un equipo puede destacar mucho en goles a favor, pero no necesariamente ser el que menos goles encaja. Por este motivo, en el dashboard se separaron los rankings ofensivos y defensivos para poder analizar cada apartado por separado.

El análisis por temporadas permite ver mejor la evolución de los equipos. Al filtrar una temporada concreta, la clasificación y los gráficos se actualizan, lo que facilita comparar el rendimiento de cada club en diferentes años.

## 4. Utilidad de las visualizaciones

Los gráficos han sido una parte importante del proyecto porque ayudan a interpretar los datos de forma más rápida. Aunque la tabla de clasificación contiene toda la información, los gráficos permiten detectar visualmente qué equipos destacan en puntos, goles a favor o goles en contra.

El comparador de equipos también resulta útil porque permite enfrentar dos clubes dentro de una misma temporada y ver sus diferencias principales. Esta funcionalidad hace que el análisis sea más interactivo y más fácil de explicar durante la defensa del proyecto.

## 5. Conclusiones sobre el modelo de Inteligencia Artificial

El modelo de Inteligencia Artificial utilizado es un Random Forest Classifier. Su objetivo es predecir si un partido termina con victoria local, empate o victoria visitante a partir de variables como tiros, tiros a puerta y tarjetas amarillas.

La precisión obtenida fue aproximadamente del 50,9%. Este resultado no debe entenderse como una predicción perfecta, sino como una primera aproximación al uso de Machine Learning en un contexto deportivo.

El fútbol es difícil de predecir porque influyen muchos factores que no aparecen en el dataset, como lesiones, alineaciones, estado de forma, decisiones arbitrales o importancia del partido. Aun así, el modelo consigue superar una predicción aleatoria entre tres clases, lo que indica que detecta ciertos patrones en los datos disponibles.

## 6. Limitaciones detectadas

La principal limitación del análisis es que el dataset contiene variables del propio partido, pero no incluye suficiente información previa al encuentro. Por ejemplo, no se tienen en cuenta aspectos como la racha reciente de cada equipo, la posición en la tabla antes del partido, bajas por lesión, alineaciones o enfrentamientos directos anteriores.

Otra limitación es que el modelo de IA predice a partir de estadísticas introducidas por el usuario, no únicamente a partir del nombre de los equipos antes de jugarse el partido. Por tanto, debe entenderse como una demostración práctica de Machine Learning aplicado al fútbol, no como una herramienta profesional de predicción deportiva.

## 7. Mejoras futuras

Como mejora futura, sería interesante ampliar el dataset con más temporadas históricas y añadir nuevas competiciones, como Champions League, Premier League o Copa del Rey.

También se podría mejorar el modelo de IA incorporando variables previas al partido, como puntos por partido, goles promedio, rendimiento como local o visitante, rachas recientes y posición en la clasificación. Con más información, el modelo tendría una base más completa para realizar predicciones.

Por último, el dashboard podría desplegarse en la nube para que cualquier usuario pudiera acceder a la aplicación sin necesidad de instalar el proyecto en local.

## 8. Conclusión final

En conjunto, el proyecto demuestra cómo un conjunto de archivos CSV puede transformarse en una aplicación completa de análisis deportivo. A través de Python, Pandas, Streamlit y Scikit-learn, se ha creado un sistema que permite limpiar datos, calcular métricas, visualizar resultados y aplicar un modelo básico de Inteligencia Artificial.

La principal aportación del proyecto es unir análisis de datos, visualización e IA en una misma herramienta sencilla y funcional.
