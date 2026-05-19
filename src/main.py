from src.analytics import cargar_datos, limpiar_dataset
from src.analisis import calcular_clasificacion


def main():
    df = cargar_datos("data/laliga_clean.csv")
    df = limpiar_dataset(df)

    tabla = calcular_clasificacion(df)

    print("Top 10 equipos por puntos:")
    print(tabla.head(10))


if __name__ == "__main__":
    main()