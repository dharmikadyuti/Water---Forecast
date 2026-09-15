"""
Reusable matplotlib chart builders for the dashboard.
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_forecast(history: pd.DataFrame, forecast: pd.DataFrame, zone: str):
    fig, ax = plt.subplots(figsize=(10, 4))

    hist_zone = history[history["zone"] == zone]
    ax.plot(hist_zone["date"], hist_zone["consumption"], label="Historical", color="#1f77b4")
    ax.plot(
        forecast["date"],
        forecast["predicted_consumption"],
        label="Forecast",
        color="#ff7f0e",
        linestyle="--",
        marker="o",
    )

    ax.set_title(f"Water Consumption Forecast — {zone}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Consumption (liters)")
    ax.legend()
    fig.autofmt_xdate()
    return fig


def plot_zone_comparison(comparison_df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 4))
    comparison_df.plot(ax=ax, marker="o")

    ax.set_title("Predicted Consumption by Zone")
    ax.set_xlabel("Date")
    ax.set_ylabel("Consumption (liters)")
    ax.legend(title="Zone")
    fig.autofmt_xdate()
    return fig


def plot_savings_bar(savings_df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(savings_df["zone"], savings_df["estimated_savings"], color="#2ca02c")

    ax.set_title("Estimated Daily Water Savings by Zone")
    ax.set_xlabel("Zone")
    ax.set_ylabel("Estimated savings (liters/day)")
    return fig
