import pandas as pd

from src.analisis import calcular_puntos


def test_victoria_local_suma_tres_puntos():
    df = pd.DataFrame({
        "goles_local": [2],
        "goles_visitante": [1],
    })

    resultado = calcular_puntos(df)

    assert resultado.loc[0, "puntos_local"] == 3
    assert resultado.loc[0, "puntos_visitante"] == 0


def test_empate_suma_un_punto_a_cada_equipo():
    df = pd.DataFrame({
        "goles_local": [1],
        "goles_visitante": [1],
    })

    resultado = calcular_puntos(df)

    assert resultado.loc[0, "puntos_local"] == 1
    assert resultado.loc[0, "puntos_visitante"] == 1


def test_victoria_visitante_suma_tres_puntos():
    df = pd.DataFrame({
        "goles_local": [0],
        "goles_visitante": [2],
    })

    resultado = calcular_puntos(df)

    assert resultado.loc[0, "puntos_local"] == 0
    assert resultado.loc[0, "puntos_visitante"] == 3