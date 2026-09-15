"""
Generate next-day (and multi-day) forecasts for a given zone using
the trained model plus the most recent history for that zone.
"""

import pandas as pd
from src.config import ZONES
from src.feature_engineering import add_date_features, add_lag_features, add_rolling_features, feature_columns
from src.model import load_model


def forecast_zone(df: pd.DataFrame, zone: str, days_ahead: int = 1) -> pd.DataFrame:
    """
    Predict consumption for `zone` for the next `days_ahead` days,
    using an iterative (recursive) forecasting approach: each day's
    prediction is fed back in as history for the next day's lag features.
    """
    if zone not in ZONES:
        raise ValueError(f"Unknown zone '{zone}'. Expected one of {ZONES}")

    model = load_model()
    history = df[df["zone"] == zone].sort_values("date").copy()

    forecasts = []
    last_date = history["date"].max()

    for step in range(1, days_ahead + 1):
        next_date = last_date + pd.Timedelta(days=step)
        working = pd.concat(
            [history, pd.DataFrame([{"date": next_date, "zone": zone, "consumption": None}])],
            ignore_index=True,
        )

        feats = add_date_features(working)
        feats = add_lag_features(feats)
        feats = add_rolling_features(feats)
        row = feats.iloc[[-1]].copy()

        row = pd.get_dummies(row, columns=["zone"], prefix="zone")
        for col in model.feature_names_:
            if col not in row.columns:
                row[col] = 0
        X = row[model.feature_names_]

        pred = float(model.predict(X)[0])
        forecasts.append({"date": next_date, "zone": zone, "predicted_consumption": pred})

        # Append prediction to history so it feeds the next iteration's lags.
        history = pd.concat(
            [history, pd.DataFrame([{"date": next_date, "zone": zone, "consumption": pred}])],
            ignore_index=True,
        )

    return pd.DataFrame(forecasts)


def forecast_all_zones(df: pd.DataFrame, days_ahead: int = 1) -> pd.DataFrame:
    """Run forecast_zone for every zone and combine results."""
    results = [forecast_zone(df, zone, days_ahead) for zone in ZONES]
    return pd.concat(results, ignore_index=True)
