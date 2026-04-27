import pandas as pd

df = pd.read_csv("data/laliga_clean.csv")

# Creación de  columnas de puntos
df["puntos_local"] = 0
df["puntos_visitante"] = 0

# Asignación de puntos
df.loc[df["goles_local"] > df["goles_visitante"], "puntos_local"] = 3
df.loc[df["goles_local"] < df["goles_visitante"], "puntos_visitante"] = 3

df.loc[df["goles_local"] == df["goles_visitante"], "puntos_local"] = 1
df.loc[df["goles_local"] == df["goles_visitante"], "puntos_visitante"] = 1

# Agrupar equipos (local)
local = df.groupby("local").agg({
    "goles_local": "sum",
    "goles_visitante": "sum",
    "puntos_local": "sum"
}).rename(columns={
    "goles_local": "goles_favor",
    "goles_visitante": "goles_contra",
    "puntos_local": "puntos"
})

# Agrupar equipos (visitante)
visitante = df.groupby("visitante").agg({
    "goles_visitante": "sum",
    "goles_local": "sum",
    "puntos_visitante": "sum"
}).rename(columns={
    "goles_visitante": "goles_favor",
    "goles_local": "goles_contra",
    "puntos_visitante": "puntos"
})

# Unir
tabla = local.add(visitante, fill_value=0)

# Ordenar por puntos
tabla = tabla.sort_values(by="puntos", ascending=False)

print(tabla.head(10))

#Clasificación por temporada 

for temporada in df["temporada"].unique():
    print(f"\nTemporada: {temporada}")
    
    df_temp = df[df["temporada"] == temporada]
    
    local = df_temp.groupby("local").agg({
        "goles_local": "sum",
        "goles_visitante": "sum",
        "puntos_local": "sum"
    }).rename(columns={
        "goles_local": "goles_favor",
        "goles_visitante": "goles_contra",
        "puntos_local": "puntos"
    })

    visitante = df_temp.groupby("visitante").agg({
        "goles_visitante": "sum",
        "goles_local": "sum",
        "puntos_visitante": "sum"
    }).rename(columns={
        "goles_visitante": "goles_favor",
        "goles_local": "goles_contra",
        "puntos_visitante": "puntos"
    })

    tabla_temp = local.add(visitante, fill_value=0)
    tabla_temp = tabla_temp.sort_values(by="puntos", ascending=False)

    print(tabla_temp.head(5))