"""
Utilities to compare historical and forecasted consumption across zones.
"""

import pandas as pd


def historical_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Average, min, and max daily consumption per zone."""
    return (
        df.groupby("zone")["consumption"]
        .agg(avg_consumption="mean", min_consumption="min", max_consumption="max")
        .reset_index()
        .round(1)
    )


def compare_forecasts(forecast_df: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot a multi-zone forecast (from forecast_all_zones) into a
    date x zone table, handy for a comparison chart or table.
    """
    return forecast_df.pivot(index="date", columns="zone", values="predicted_consumption")
