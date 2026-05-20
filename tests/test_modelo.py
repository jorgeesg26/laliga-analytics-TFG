import pandas as pd

from src.modelo import entrenar_modelo, predecir


def test_modelo_entrena_y_devuelve_accuracy():
    df = pd.DataFrame({
        "goles_local": [2, 1, 0, 3, 1, 2, 4, 0, 2, 1],
        "goles_visitante": [1, 1, 2, 0, 3, 2, 1, 0, 2, 3],
        "tiros_local": [10, 8, 5, 14, 7, 11, 15, 6, 9, 8],
        "tiros_visitante": [8, 8, 12, 5, 13, 10, 7, 6, 9, 12],
        "tiros_puerta_local": [5, 3, 2, 7, 3, 4, 8, 2, 4, 3],
        "tiros_puerta_visitante": [3, 3, 6, 2, 7, 4, 3, 2, 4, 6],
        "amarillas_local": [2, 1, 3, 1, 4, 2, 1, 2, 3, 1],
        "amarillas_visitante": [3, 2, 1, 2, 2, 3, 2, 1, 3, 4],
    })

    modelo, accuracy = entrenar_modelo(df)

    assert 0 <= accuracy <= 1

    resultado = predecir(modelo, [10, 8, 5, 3, 2, 3])[0]

    assert resultado in [0, 1, 2]