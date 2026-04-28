import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="LaLiga Analytics",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ LaLiga Analytics")
st.write("Análisis de rendimiento de equipos de La Liga desde la temporada 2020 hasta la actualidad.")

df = pd.read_csv("data/laliga_clean.csv")

temporadas = sorted(df["temporada"].unique())
temporada = st.selectbox("Selecciona una temporada", temporadas)

df_temp = df[df["temporada"] == temporada].copy()

df_temp["puntos_local"] = 0
df_temp["puntos_visitante"] = 0

df_temp.loc[df_temp["goles_local"] > df_temp["goles_visitante"], "puntos_local"] = 3
df_temp.loc[df_temp["goles_local"] < df_temp["goles_visitante"], "puntos_visitante"] = 3
df_temp.loc[df_temp["goles_local"] == df_temp["goles_visitante"], "puntos_local"] = 1
df_temp.loc[df_temp["goles_local"] == df_temp["goles_visitante"], "puntos_visitante"] = 1

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

tabla = local.add(visitante, fill_value=0)
tabla["diferencia_goles"] = tabla["goles_favor"] - tabla["goles_contra"]
tabla = tabla.sort_values(by=["puntos", "diferencia_goles"], ascending=False)

col1, col2, col3 = st.columns(3)

col1.metric("Partidos analizados", len(df_temp))
col2.metric("Goles totales", int(df_temp["goles_local"].sum() + df_temp["goles_visitante"].sum()))
col3.metric("Equipos", len(tabla))

st.subheader(f"🏆 Clasificación {temporada}")
st.dataframe(tabla, use_container_width=True)

st.subheader("📊 Top 10 equipos por puntos")

top10 = tabla.head(10)

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(top10.index, top10["puntos"])
ax.set_xlabel("Equipo")
ax.set_ylabel("Puntos")
ax.set_title(f"Top 10 equipos por puntos - {temporada}")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)