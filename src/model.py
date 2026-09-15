"""
Train and persist the water demand forecasting model.

Run directly to train on the raw (or sample) dataset:
    python -m src.model --train
    python -m src.model --train --sample
"""

import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from src.config import MODEL_FILE, MODELS_DIR, RANDOM_STATE, ZONES
from src.data_loader import load_data
from src.feature_engineering import build_features, feature_columns


def train_model(df: pd.DataFrame) -> RandomForestRegressor:
    features = build_features(df)

    # One-hot encode zone so a single model can serve all zones.
    features = pd.get_dummies(features, columns=["zone"], prefix="zone")
    zone_cols = [f"zone_{z}" for z in ZONES if f"zone_{z}" in features.columns]

    X = features[feature_columns() + zone_cols]
    y = features["consumption"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, shuffle=False
    )

    model = RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"Validation MAE: {mae:.2f} liters")

    # Stash the training columns on the model for consistent inference.
    model.feature_names_ = list(X.columns)
    return model


def save_model(model: RandomForestRegressor, path=MODEL_FILE) -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(path=MODEL_FILE) -> RandomForestRegressor:
    if not path.exists():
        raise FileNotFoundError(
            f"No trained model found at {path}. Run `python -m src.model --train` first."
        )
    return joblib.load(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true", help="Train and save the model")
    parser.add_argument("--sample", action="store_true", help="Use bundled sample data")
    args = parser.parse_args()

    if args.train:
        data = load_data(use_sample=args.sample)
        trained = train_model(data)
        save_model(trained)
