import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="LaLiga Analytics",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ LaLiga Analytics")
st.write("Análisis de rendimiento de equipos de La Liga desde la temporada 2020 hasta la actualidad.")

# Cargar datos
df = pd.read_csv("data/laliga_clean.csv")

# Selector de temporada
temporadas = sorted(df["temporada"].unique())
temporada = st.selectbox("Selecciona una temporada", temporadas)

df_temp = df[df["temporada"] == temporada].copy()

# Calcular puntos
df_temp["puntos_local"] = 0
df_temp["puntos_visitante"] = 0

df_temp.loc[df_temp["goles_local"] > df_temp["goles_visitante"], "puntos_local"] = 3
df_temp.loc[df_temp["goles_local"] < df_temp["goles_visitante"], "puntos_visitante"] = 3
df_temp.loc[df_temp["goles_local"] == df_temp["goles_visitante"], "puntos_local"] = 1
df_temp.loc[df_temp["goles_local"] == df_temp["goles_visitante"], "puntos_visitante"] = 1

# Clasificación
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

# Métricas generales
col1, col2, col3 = st.columns(3)
col1.metric("Partidos analizados", len(df_temp))
col2.metric("Goles totales", int(df_temp["goles_local"].sum() + df_temp["goles_visitante"].sum()))
col3.metric("Equipos", len(tabla))

# Tabla
st.subheader(f"🏆 Clasificación {temporada}")
st.dataframe(tabla, use_container_width=True)

# Gráfico puntos
st.subheader("📊 Top 10 equipos por puntos")
top10 = tabla.head(10)

fig, ax = plt.subplots()
ax.bar(top10.index, top10["puntos"])
ax.set_xlabel("Equipo")
ax.set_ylabel("Puntos")
ax.set_title(f"Top 10 equipos - {temporada}")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Gráfico goles
st.subheader("⚽ Top 10 equipos por goles")
top_goles = tabla.sort_values(by="goles_favor", ascending=False).head(10)

fig2, ax2 = plt.subplots()
ax2.bar(top_goles.index, top_goles["goles_favor"])
ax2.set_xlabel("Equipo")
ax2.set_ylabel("Goles")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

# Defensa
st.subheader("🛡️ Equipos más defensivos")
top_defensa = tabla.sort_values(by="goles_contra").head(10)

fig3, ax3 = plt.subplots()
ax3.bar(top_defensa.index, top_defensa["goles_contra"])
ax3.set_xlabel("Equipo")
ax3.set_ylabel("Goles encajados")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

# Comparador individual
st.subheader("📈 Comparador de equipo")
equipos = sorted(tabla.index)
equipo = st.selectbox("Selecciona un equipo", equipos)

datos_equipo = tabla.loc[equipo]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Puntos", int(datos_equipo["puntos"]))
col2.metric("Goles a favor", int(datos_equipo["goles_favor"]))
col3.metric("Goles en contra", int(datos_equipo["goles_contra"]))
col4.metric("Diferencia", int(datos_equipo["diferencia_goles"]))

# Comparador doble
st.subheader("⚔️ Comparador de dos equipos")

equipo1 = st.selectbox("Equipo 1", equipos, key="eq1")
equipo2 = st.selectbox("Equipo 2", equipos, key="eq2")

if equipo1 != equipo2:
    datos1 = tabla.loc[equipo1]
    datos2 = tabla.loc[equipo2]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### {equipo1}")
        st.metric("Puntos", int(datos1["puntos"]))
        st.metric("Goles a favor", int(datos1["goles_favor"]))
        st.metric("Goles en contra", int(datos1["goles_contra"]))
        st.metric("Diferencia", int(datos1["diferencia_goles"]))

    with col2:
        st.markdown(f"### {equipo2}")
        st.metric("Puntos", int(datos2["puntos"]))
        st.metric("Goles a favor", int(datos2["goles_favor"]))
        st.metric("Goles en contra", int(datos2["goles_contra"]))
        st.metric("Diferencia", int(datos2["diferencia_goles"]))

    # Gráfico comparativo
    st.subheader("📊 Comparación visual")

    etiquetas = ["Puntos", "Goles a favor", "Goles en contra"]

    valores1 = [datos1["puntos"], datos1["goles_favor"], datos1["goles_contra"]]
    valores2 = [datos2["puntos"], datos2["goles_favor"], datos2["goles_contra"]]

    x = np.arange(len(etiquetas))
    width = 0.35

    fig4, ax4 = plt.subplots()

    ax4.bar(x - width/2, valores1, width, label=equipo1)
    ax4.bar(x + width/2, valores2, width, label=equipo2)

    ax4.set_xticks(x)
    ax4.set_xticklabels(etiquetas)
    ax4.set_title("Comparación entre equipos")
    ax4.legend()

    st.pyplot(fig4)