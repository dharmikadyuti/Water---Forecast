"""
Very simple baseline-vs-optimized pumping schedule logic.

The "baseline" schedule assumes pumping matches peak historical demand
every day (i.e. no dynamic adjustment). The "optimized" schedule pumps
to the forecasted demand plus a small safety margin, which is typically
lower than always-pump-to-peak and highlights potential savings.
"""

import pandas as pd

SAFETY_MARGIN = 1.10  # pump 10% above forecast to avoid shortages


def baseline_schedule(historical_df: pd.DataFrame) -> pd.DataFrame:
    """Baseline: pump the historical peak (max) consumption per zone, every day."""
    peaks = historical_df.groupby("zone")["consumption"].max().reset_index()
    peaks = peaks.rename(columns={"consumption": "baseline_pumping"})
    return peaks


def optimized_schedule(forecast_df: pd.DataFrame) -> pd.DataFrame:
    """Optimized: pump to forecasted demand + safety margin, per zone/day."""
    df = forecast_df.copy()
    df["optimized_pumping"] = df["predicted_consumption"] * SAFETY_MARGIN
    return df[["date", "zone", "optimized_pumping"]]


def estimate_savings(historical_df: pd.DataFrame, forecast_df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine baseline and optimized schedules to estimate liters (and %) saved
    per zone by switching from static peak-pumping to demand-based pumping.
    """
    baseline = baseline_schedule(historical_df)
    optimized = optimized_schedule(forecast_df)

    avg_optimized = (
        optimized.groupby("zone")["optimized_pumping"].mean().reset_index()
    )

    merged = baseline.merge(avg_optimized, on="zone")
    merged["estimated_savings"] = merged["baseline_pumping"] - merged["optimized_pumping"]
    merged["savings_pct"] = (
        merged["estimated_savings"] / merged["baseline_pumping"] * 100
    ).round(1)

    return merged.round(1)
