import os

import pandas as pd


def test_laliga_clean_exists():
    assert os.path.exists("data/laliga_clean.csv")


def test_laliga_clean_has_required_columns():
    df = pd.read_csv("data/laliga_clean.csv")

    required_columns = [
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

    for column in required_columns:
        assert column in df.columns