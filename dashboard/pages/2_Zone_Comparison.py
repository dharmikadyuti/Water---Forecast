"""
Zone Comparison page — visualize predicted consumption across all zones.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st
from src.data_loader import load_data
from src.forecast import forecast_all_zones
from src.zone_comparison import historical_summary, compare_forecasts
from src.config import RAW_DATA_FILE
from dashboard.components.sidebar import horizon_selector
from dashboard.components.charts import plot_zone_comparison

st.set_page_config(page_title="Zone Comparison — Water Forecast", page_icon="🏫", layout="wide")
st.title("🏫 Zone Comparison")

horizon = horizon_selector()

use_sample = not RAW_DATA_FILE.exists()
df = load_data(use_sample=use_sample)

st.subheader("Historical summary")
st.dataframe(historical_summary(df), use_container_width=True)

try:
    forecast_df = forecast_all_zones(df, days_ahead=horizon)
    comparison = compare_forecasts(forecast_df)

    st.subheader(f"Forecast comparison — next {horizon} day(s)")
    fig = plot_zone_comparison(comparison)
    st.pyplot(fig)

    st.dataframe(comparison, use_container_width=True)

except FileNotFoundError:
    st.warning("No trained model found yet. Run `python -m src.model --train` first.")
