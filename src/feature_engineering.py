"""
Build model-ready features from cleaned consumption data:
date parts, lag features, and rolling statistics.
"""

import pandas as pd
from src.config import LAG_DAYS, ROLLING_WINDOWS


def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
    return df


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for lag in LAG_DAYS:
        df[f"lag_{lag}"] = df.groupby("zone")["consumption"].shift(lag)
    return df


def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for window in ROLLING_WINDOWS:
        df[f"rolling_mean_{window}"] = (
            df.groupby("zone")["consumption"]
            .shift(1)
            .rolling(window)
            .mean()
            .reset_index(level=0, drop=True)
        )
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Full feature pipeline. Drops rows with NaNs introduced by lag/rolling."""
    df = add_date_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df = df.dropna().reset_index(drop=True)
    return df


def feature_columns() -> list:
    cols = ["day_of_week", "month", "is_weekend"]
    cols += [f"lag_{lag}" for lag in LAG_DAYS]
    cols += [f"rolling_mean_{w}" for w in ROLLING_WINDOWS]
    return cols
