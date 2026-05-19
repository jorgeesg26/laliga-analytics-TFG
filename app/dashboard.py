import sys
import os

import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analisis import (
    cargar_datos,
    calcular_clasificacion,
    obtener_metricas_generales
)

from src.graficos import (
    grafico_top_puntos,
    grafico_top_goles,
    grafico_top_defensa,
    grafico_comparacion_equipos
)

from src.modelo import entrenar_modelo, predecir


st.set_page_config(
    page_title="LaLiga Analytics",
    page_icon="⚽",
    layout="wide"
)


@st.cache_data
def cargar_datos_cache():
    return cargar_datos()


@st.cache_resource
def entrenar_modelo_cache(df):
    return entrenar_modelo(df)


st.title("⚽ LaLiga Analytics")

st.write(
    "Dashboard interactivo para el análisis de rendimiento de equipos de La Liga "
    "desde la temporada 2020 hasta la actualidad."
)

try:
    df = cargar_datos_cache()
except Exception as error:
    st.error(f"Error al cargar los datos: {error}")
    st.stop()

try:
    modelo, accuracy = entrenar_modelo_cache(df)
except Exception as error:
    st.error(f"Error al entrenar el modelo de IA: {error}")
    st.stop()

temporadas = sorted(df["temporada"].unique())
temporada = st.selectbox("Selecciona una temporada", temporadas)

df_temp = df[df["temporada"] == temporada].copy()
tabla = calcular_clasificacion(df_temp)

partidos, goles_totales, equipos_totales = obtener_metricas_generales(df_temp)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Partidos analizados", partidos)
col2.metric("Goles totales", goles_totales)
col3.metric("Equipos", equipos_totales)
col4.metric("Precisión IA", f"{accuracy:.2%}")

st.subheader(f"🏆 Clasificación {temporada}")
st.dataframe(tabla, use_container_width=True)

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📊 Top 10 equipos por puntos")
    st.pyplot(grafico_top_puntos(tabla, temporada), use_container_width=False)

with col_graf2:
    st.subheader("⚽ Top 10 equipos por goles")
    st.pyplot(grafico_top_goles(tabla, temporada), use_container_width=False)

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.subheader("🛡️ Equipos más defensivos")
    st.pyplot(grafico_top_defensa(tabla, temporada), use_container_width=False)

st.subheader("📈 Comparador de equipo")

equipos = sorted(tabla.index)
equipo = st.selectbox("Selecciona un equipo", equipos)

datos_equipo = tabla.loc[equipo]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Puntos", int(datos_equipo["puntos"]))
col2.metric("Goles a favor", int(datos_equipo["goles_favor"]))
col3.metric("Goles en contra", int(datos_equipo["goles_contra"]))
col4.metric("Diferencia", int(datos_equipo["diferencia_goles"]))

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

    st.subheader("📊 Comparación visual")
    st.pyplot(grafico_comparacion_equipos(equipo1, equipo2, datos1, datos2))
else:
    st.warning("Selecciona dos equipos diferentes para compararlos.")

st.subheader("🤖 Predicción de resultado con IA")

st.write(
    "El modelo utiliza Random Forest para predecir el resultado de un partido "
    "a partir de estadísticas como tiros, tiros a puerta y tarjetas amarillas."
)

col1, col2 = st.columns(2)

with col1:
    tiros_local = st.slider("Tiros del equipo local", 0, 35, 12)
    tiros_puerta_local = st.slider("Tiros a puerta del equipo local", 0, 20, 5)
    amarillas_local = st.slider("Tarjetas amarillas local", 0, 10, 2)

with col2:
    tiros_visitante = st.slider("Tiros del equipo visitante", 0, 35, 10)
    tiros_puerta_visitante = st.slider("Tiros a puerta del equipo visitante", 0, 20, 4)
    amarillas_visitante = st.slider("Tarjetas amarillas visitante", 0, 10, 2)

datos_prediccion = [
    tiros_local,
    tiros_visitante,
    tiros_puerta_local,
    tiros_puerta_visitante,
    amarillas_local,
    amarillas_visitante
]

if st.button("Predecir resultado"):
    resultado = predecir(modelo, datos_prediccion)[0]

    if resultado == 1:
        st.success("Predicción: gana el equipo local")
    elif resultado == 2:
        st.success("Predicción: gana el equipo visitante")
    else:
        st.warning("Predicción: empate")