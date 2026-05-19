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