import pandas as pd

files = [
    "data/2020-2021.csv",
    "data/2021-2022.csv",
    "data/2022-2023.csv",
    "data/2023-2024.csv",
    "data/2024-2025.csv",
    "data/2025-2026.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file, encoding="latin1")

    # Seleccionamos columnas importantes
    df = df[[
        "Date", "HomeTeam", "AwayTeam",
        "FTHG", "FTAG",
        "HS", "AS", "HST", "AST",
        "HY", "AY"
    ]]

    # Renombramos
    df.columns = [
        "fecha", "local", "visitante",
        "goles_local", "goles_visitante",
        "tiros_local", "tiros_visitante",
        "tiros_puerta_local", "tiros_puerta_visitante",
        "amarillas_local", "amarillas_visitante"
    ]

    temporada = file.split("/")[-1].replace(".csv", "")
    df["temporada"] = temporada

    dfs.append(df)

final_df = pd.concat(dfs)

final_df.to_csv("data/laliga_clean.csv", index=False)

print("Dataset limpio listo ✅")