import pandas as pd


def cargar_datos(ruta="data/laliga_clean.csv"):
    return pd.read_csv(ruta)


def calcular_puntos(df):
    df = df.copy()

    df["puntos_local"] = 0
    df["puntos_visitante"] = 0

    df.loc[df["goles_local"] > df["goles_visitante"], "puntos_local"] = 3
    df.loc[df["goles_local"] < df["goles_visitante"], "puntos_visitante"] = 3

    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_local"] = 1
    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_visitante"] = 1

    return df