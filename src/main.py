import pandas as pd
import matplotlib.pyplot as plt

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

# Equipos más ofensivos (más goles a favor)
print("\nEquipos más ofensivos:")
print(tabla.sort_values(by="goles_favor", ascending=False).head(5))

#gráficos de goles a favor
top_goles = tabla.sort_values(by="goles_favor", ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_goles.index, top_goles["goles_favor"])
plt.xticks(rotation=45)
plt.title("Top equipos por goles")
plt.tight_layout()

plt.savefig("outputs/graficos/top_goles.png")
plt.show()

# Equipos más defensivos (menos goles encajados)
print("\nEquipos más defensivos:")
print(tabla.sort_values(by="goles_contra").head(5))

# Calcular tiros a puerta totales
df["tiros_puerta_total"] = df["tiros_puerta_local"] + df["tiros_puerta_visitante"]
df["goles_total"] = df["goles_local"] + df["goles_visitante"]

eficiencia = df.groupby("local").agg({
    "goles_local": "sum",
    "tiros_puerta_local": "sum"
})

eficiencia["ratio"] = eficiencia["goles_local"] / eficiencia["tiros_puerta_local"]

print("\nEquipos más eficientes:")
print(eficiencia.sort_values(by="ratio", ascending=False).head(5))

#tarjetas 
tarjetas = df.groupby("local").agg({
    "amarillas_local": "sum"
}).sort_values(by="amarillas_local", ascending=False)

print("\nEquipos con más tarjetas:")
print(tarjetas.head(5))

#equipos mas defensivos
top_defensa = tabla.sort_values(by="goles_contra").head(10)

plt.figure(figsize=(10,5))
plt.bar(top_defensa.index, top_defensa["goles_contra"])
plt.xticks(rotation=45)
plt.title("Equipos más defensivos")
plt.tight_layout()

plt.savefig("outputs/graficos/defensa.png")
plt.show()