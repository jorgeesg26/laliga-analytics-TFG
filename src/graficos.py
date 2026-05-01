import matplotlib.pyplot as plt
import numpy as np


def grafico_top_puntos(tabla, temporada):
    top10 = tabla.head(10)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(top10.index, top10["puntos"])
    ax.set_xlabel("Equipo")
    ax.set_ylabel("Puntos")
    ax.set_title(f"Top 10 equipos por puntos - {temporada}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def grafico_top_goles(tabla, temporada):
    top_goles = tabla.sort_values(by="goles_favor", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(top_goles.index, top_goles["goles_favor"])
    ax.set_xlabel("Equipo")
    ax.set_ylabel("Goles a favor")
    ax.set_title(f"Top 10 equipos por goles - {temporada}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def grafico_top_defensa(tabla, temporada):
    top_defensa = tabla.sort_values(by="goles_contra", ascending=True).head(10)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(top_defensa.index, top_defensa["goles_contra"])
    ax.set_xlabel("Equipo")
    ax.set_ylabel("Goles encajados")
    ax.set_title(f"Equipos con menos goles encajados - {temporada}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def grafico_comparacion_equipos(equipo1, equipo2, datos1, datos2):
    etiquetas = ["Puntos", "Goles a favor", "Goles en contra"]

    valores1 = [
        datos1["puntos"],
        datos1["goles_favor"],
        datos1["goles_contra"]
    ]

    valores2 = [
        datos2["puntos"],
        datos2["goles_favor"],
        datos2["goles_contra"]
    ]

    x = np.arange(len(etiquetas))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6, 3.5))

    ax.bar(x - width / 2, valores1, width, label=equipo1)
    ax.bar(x + width / 2, valores2, width, label=equipo2)

    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    ax.set_title("Comparación entre equipos")
    ax.legend()

    plt.tight_layout()

    return fig