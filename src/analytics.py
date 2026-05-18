import pandas as pd


def cargar_datos(ruta="data/laliga_clean.csv"):
    try:
        df = pd.read_csv(ruta)
        return df
    except FileNotFoundError as error:
        raise FileNotFoundError(f"No se ha encontrado el archivo: {ruta}") from error
    except pd.errors.EmptyDataError as error:
        raise ValueError("El archivo CSV está vacío.") from error
    except Exception as error:
        raise RuntimeError(f"Error al cargar los datos: {error}") from error


def calcular_puntos(df):
    df = df.copy()

    df["puntos_local"] = 0
    df["puntos_visitante"] = 0

    df.loc[df["goles_local"] > df["goles_visitante"], "puntos_local"] = 3
    df.loc[df["goles_local"] < df["goles_visitante"], "puntos_visitante"] = 3

    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_local"] = 1
    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_visitante"] = 1

    return df