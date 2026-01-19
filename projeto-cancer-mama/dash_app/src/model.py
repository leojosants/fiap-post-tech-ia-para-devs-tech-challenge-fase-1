import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_breast_cancer


MODEL_PATH = Path(__file__).resolve().parent / "artifacts" / "best_model.joblib"


def train_and_save_model():
    """
    Treina o modelo final e salva para uso no Dash.
    """
    data = load_breast_cancer(as_frame=True)
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(
            n_estimators=300,
            random_state=42
        ))
    ])

    pipeline.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    return pipeline


def load_model():
    """
    Carrega o modelo treinado.
    Se não existir, treina automaticamente.
    """
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)

    # fallback seguro e automático
    return train_and_save_model()


def predict_proba(model, X):
    """
    Retorna a probabilidade da classe positiva (maligna).
    """
    proba = model.predict_proba(X)
    return float(proba[:, 1][0])
