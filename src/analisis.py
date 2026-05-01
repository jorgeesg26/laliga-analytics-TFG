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


def calcular_clasificacion(df):
    df = calcular_puntos(df)

    local = df.groupby("local").agg({
        "goles_local": "sum",
        "goles_visitante": "sum",
        "puntos_local": "sum"
    }).rename(columns={
        "goles_local": "goles_favor",
        "goles_visitante": "goles_contra",
        "puntos_local": "puntos"
    })

    visitante = df.groupby("visitante").agg({
        "goles_visitante": "sum",
        "goles_local": "sum",
        "puntos_visitante": "sum"
    }).rename(columns={
        "goles_visitante": "goles_favor",
        "goles_local": "goles_contra",
        "puntos_visitante": "puntos"
    })

    tabla = local.add(visitante, fill_value=0)

    tabla["diferencia_goles"] = tabla["goles_favor"] - tabla["goles_contra"]

    tabla = tabla.sort_values(
        by=["puntos", "diferencia_goles", "goles_favor"],
        ascending=False
    )

    return tabla


def obtener_metricas_generales(df):
    partidos = len(df)
    goles_totales = int(df["goles_local"].sum() + df["goles_visitante"].sum())
    equipos = len(set(df["local"]).union(set(df["visitante"])))

    return partidos, goles_totales, equipos


def obtener_top_goles(tabla, n=10):
    return tabla.sort_values(by="goles_favor", ascending=False).head(n)


def obtener_top_defensa(tabla, n=10):
    return tabla.sort_values(by="goles_contra", ascending=True).head(n)