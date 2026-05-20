import pandas as pd


COLUMNAS_OBLIGATORIAS = [
    "fecha",
    "local",
    "visitante",
    "goles_local",
    "goles_visitante",
    "tiros_local",
    "tiros_visitante",
    "tiros_puerta_local",
    "tiros_puerta_visitante",
    "amarillas_local",
    "amarillas_visitante",
    "temporada",
]


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


def validar_columnas(df, columnas_obligatorias=None):
    if columnas_obligatorias is None:
        columnas_obligatorias = COLUMNAS_OBLIGATORIAS

    columnas_faltantes = [
        columna for columna in columnas_obligatorias if columna not in df.columns
    ]

    if columnas_faltantes:
        raise ValueError(
            f"Faltan columnas obligatorias en el dataset: {columnas_faltantes}"
        )

    return True


def limpiar_dataset(df):
    df = df.copy()

    validar_columnas(df)

    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True, errors="coerce")

    columnas_numericas = [
        "goles_local",
        "goles_visitante",
        "tiros_local",
        "tiros_visitante",
        "tiros_puerta_local",
        "tiros_puerta_visitante",
        "amarillas_local",
        "amarillas_visitante",
    ]

    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna], errors="coerce")

    df = df.dropna(subset=["fecha", "local", "visitante", "temporada"])
    df[columnas_numericas] = df[columnas_numericas].fillna(0).astype(int)

    return df


def calcular_puntos(df):
    df = df.copy()

    df["puntos_local"] = 0
    df["puntos_visitante"] = 0

    df.loc[df["goles_local"] > df["goles_visitante"], "puntos_local"] = 3
    df.loc[df["goles_local"] < df["goles_visitante"], "puntos_visitante"] = 3

    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_local"] = 1
    df.loc[df["goles_local"] == df["goles_visitante"], "puntos_visitante"] = 1

    return df


def calcular_clasificacion(df):
    df = calcular_puntos(df)

    local = df.groupby("local").agg({
        "goles_local": "sum",
        "goles_visitante": "sum",
        "puntos_local": "sum",
    }).rename(columns={
        "goles_local": "goles_favor",
        "goles_visitante": "goles_contra",
        "puntos_local": "puntos",
    })

    visitante = df.groupby("visitante").agg({
        "goles_visitante": "sum",
        "goles_local": "sum",
        "puntos_visitante": "sum",
    }).rename(columns={
        "goles_visitante": "goles_favor",
        "goles_local": "goles_contra",
        "puntos_visitante": "puntos",
    })

    tabla = local.add(visitante, fill_value=0)
    tabla["diferencia_goles"] = tabla["goles_favor"] - tabla["goles_contra"]

    tabla = tabla.sort_values(
        by=["puntos", "diferencia_goles", "goles_favor"],
        ascending=False,
    )

    return tabla