import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class DataManager:
    def __init__(self, data_path):
        self._data_path = data_path
        self._df = None

    def load_data(self):
        try:
            self._df = pd.read_csv(self._data_path)
            return self._df
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"No se ha encontrado el archivo: {self._data_path}"
            ) from error
        except pd.errors.EmptyDataError as error:
            raise ValueError("El archivo CSV está vacío.") from error

    def save_data(self, output_path):
        if self._df is None:
            raise ValueError("No hay datos cargados para guardar.")

        self._df.to_csv(output_path, index=False)

    def get_data(self):
        return self._df

    class LaLigaDataManager(DataManager):
    REQUIRED_COLUMNS = [
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

    def validate_columns(self):
        if self._df is None:
            raise ValueError("No hay datos cargados.")

        missing_columns = [
            column for column in self.REQUIRED_COLUMNS if column not in self._df.columns
        ]

        if missing_columns:
            raise ValueError(f"Faltan columnas obligatorias: {missing_columns}")

        return True

    def clean_data(self):
        if self._df is None:
            raise ValueError("No hay datos cargados.")

        self.validate_columns()

        self._df["fecha"] = pd.to_datetime(
            self._df["fecha"], dayfirst=True, errors="coerce"
        )

        self._df = self._df.dropna(subset=["fecha", "local", "visitante"])

        return self._df
        class BaseAnalyzer:
    def __init__(self, df):
        self._df = df.copy()


class LaLigaAnalyzer(BaseAnalyzer):
    def calculate_points(self):
        self._df["puntos_local"] = 0
        self._df["puntos_visitante"] = 0

        self._df.loc[
            self._df["goles_local"] > self._df["goles_visitante"],
            "puntos_local"
        ] = 3

        self._df.loc[
            self._df["goles_local"] < self._df["goles_visitante"],
            "puntos_visitante"
        ] = 3

        self._df.loc[
            self._df["goles_local"] == self._df["goles_visitante"],
            "puntos_local"
        ] = 1

        self._df.loc[
            self._df["goles_local"] == self._df["goles_visitante"],
            "puntos_visitante"
        ] = 1

        return self._df

    def get_classification(self):
        df = self.calculate_points()

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

    def get_top_attack(self, n=10):
        tabla = self.get_classification()
        return tabla.sort_values(by="goles_favor", ascending=False).head(n)

    def get_top_defense(self, n=10):
        tabla = self.get_classification()
        return tabla.sort_values(by="goles_contra", ascending=True).head(n)