from models import LaLigaAnalyzer, LaLigaDataManager


def main():
    data_manager = LaLigaDataManager("data/laliga_clean.csv")
    df = data_manager.load_data()
    df = data_manager.clean_data()

    analyzer = LaLigaAnalyzer(df)
    classification = analyzer.get_classification()

    print("Top 10 equipos por puntos:")
    print(classification.head(10))


if __name__ == "__main__":
    main()