# LaLiga Analytics

LaLiga Analytics es una aplicación web desarrollada en Python para analizar datos históricos de LaLiga desde la temporada 2020-2021 hasta la actualidad.

El proyecto permite consultar clasificaciones por temporada, visualizar gráficos de rendimiento, comparar equipos y utilizar un modelo de Inteligencia Artificial para realizar una predicción básica del resultado de un partido.

## Objetivo del proyecto

El objetivo principal es transformar varios archivos CSV con datos de partidos en una herramienta visual e interactiva.

A partir de los datos limpios, la aplicación calcula métricas deportivas como puntos, goles a favor, goles en contra, diferencia de goles y rankings ofensivos y defensivos.

Además, el proyecto incorpora una parte de Inteligencia Artificial mediante un modelo Random Forest Classifier, que predice si un partido termina con victoria local, empate o victoria visitante a partir de estadísticas introducidas por el usuario.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Scikit-learn
- Pytest
- GitHub

## Estructura del proyecto

```text
laliga-analytics-TFG/
│
├── app/
│   └── dashboard.py
│
├── data/
│   ├── 2020-2021.csv
│   ├── 2021-2022.csv
│   ├── 2022-2023.csv
│   ├── 2023-2024.csv
│   ├── 2024-2025.csv
│   ├── 2025-2026.csv
│   └── laliga_clean.csv
│
├── docs/
│   ├── uml_diagram.png
│   └── conclusiones_analisis.md
│
├── outputs/
│   └── graficos/
│
├── src/
│   ├── analisis.py
│   ├── analytics.py
│   ├── graficos.py
│   ├── main.py
│   ├── merge_data.py
│   ├── modelo.py
│   └── models.py
│
├── tests/
│   ├── __init__.py
│   ├── test_analytics.py
│   ├── test_data.py
│   └── test_modelo.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalación

Primero se recomienda crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Ejecutar el dashboard

Para lanzar la aplicación web con Streamlit:

```bash
streamlit run app/dashboard.py
```

Al ejecutar este comando, se abrirá una dirección local en el navegador desde la que se puede utilizar el dashboard de LaLiga Analytics.

## Ejecutar análisis por consola

También se puede ejecutar un análisis básico desde consola:

```bash
python src/main.py
```

Este comando carga el dataset limpio, calcula la clasificación general y muestra el Top 10 de equipos por puntos.

## Ejecutar pruebas

Para ejecutar las pruebas automáticas con Pytest:

```bash
pytest
```

Las pruebas comprueban aspectos como:

- existencia del dataset limpio;
- columnas principales del dataset;
- cálculo correcto de puntos;
- generación de la clasificación;
- entrenamiento y predicción del modelo de Inteligencia Artificial.

## Dataset utilizado

Los datos originales proceden de Football-Data y corresponden a diferentes temporadas de LaLiga.

A partir de los CSV originales se genera un archivo limpio llamado:

```text
data/laliga_clean.csv
```

Este archivo contiene las columnas necesarias para el análisis y para el modelo de IA:

- fecha;
- equipo local;
- equipo visitante;
- goles del equipo local;
- goles del equipo visitante;
- tiros;
- tiros a puerta;
- tarjetas amarillas;
- temporada.

## Modelo de Inteligencia Artificial

El proyecto utiliza un modelo Random Forest Classifier de Scikit-learn.

El modelo usa como variables de entrada:

- tiros del equipo local;
- tiros del equipo visitante;
- tiros a puerta del equipo local;
- tiros a puerta del equipo visitante;
- tarjetas amarillas del equipo local;
- tarjetas amarillas del equipo visitante.

La salida del modelo puede ser:

- victoria local;
- empate;
- victoria visitante.

En las pruebas realizadas, el modelo obtuvo una precisión aproximada del 50,9%.

## Programación orientada a objetos

El proyecto incorpora un módulo de clases en:

```text
src/models.py
```

Las clases principales son:

- DataManager;
- LaLigaDataManager;
- BaseAnalyzer;
- LaLigaAnalyzer;
- MatchPredictor.

Estas clases permiten organizar la carga de datos, la limpieza del dataset, el análisis deportivo y el modelo predictivo.

## Repositorio

El código fuente del proyecto está disponible en GitHub:

```text
https://github.com/jorgeesg26/laliga-analytics-TFG.git
```

## Autor

Jorge Salguero Abad
