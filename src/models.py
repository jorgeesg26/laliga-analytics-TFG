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