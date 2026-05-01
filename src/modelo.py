from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def preparar_datos_modelo(df):
    df = df.copy()

    df["resultado"] = 0
    df.loc[df["goles_local"] > df["goles_visitante"], "resultado"] = 1
    df.loc[df["goles_local"] < df["goles_visitante"], "resultado"] = 2

    X = df[[
        "tiros_local",
        "tiros_visitante",
        "tiros_puerta_local",
        "tiros_puerta_visitante",
        "amarillas_local",
        "amarillas_visitante"
    ]]

    y = df["resultado"]

    return X, y


def entrenar_modelo(df):
    X, y = preparar_datos_modelo(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    modelo = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, predicciones)

    return modelo, accuracy


def predecir(modelo, datos):
    return modelo.predict([datos])