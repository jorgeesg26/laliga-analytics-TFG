# LaLiga Analytics

LaLiga Analytics es una aplicación web desarrollada en Python para analizar datos históricos de LaLiga desde la temporada 2020-2021 hasta la actualidad.

El proyecto permite consultar clasificaciones por temporada, visualizar gráficos de rendimiento, comparar equipos y utilizar un modelo de Inteligencia Artificial para realizar una predicción básica del resultado de un partido.

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
│   ├── test_analytics.py
│   ├── test_data.py
│   └── test_modelo.py
│
├── outputs/
│   └── graficos/
│
├── requirements.txt
├── pytest.ini
└── README.md
