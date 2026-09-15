"""
Interactive Forecast page — predict water demand for a selected zone and date range.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st
from src.data_loader import load_data
from src.forecast import forecast_zone
from src.config import RAW_DATA_FILE
from dashboard.components.sidebar import zone_selector, horizon_selector
from dashboard.components.charts import plot_forecast

st.set_page_config(page_title="Forecast - Water Forecast", page_icon="📈", layout="wide")
st.title("📈 Interactive Forecast")

zone = zone_selector()
horizon = horizon_selector()

use_sample = not RAW_DATA_FILE.exists()
df = load_data(use_sample=use_sample)

try:
    forecast_df = forecast_zone(df, zone, days_ahead=horizon)

    st.subheader(f"{zone} — next {horizon} day(s)")
    fig = plot_forecast(df, forecast_df, zone)
    st.pyplot(fig)

    st.dataframe(forecast_df, use_container_width=True)

except FileNotFoundError:
    st.warning("No trained model found yet. Run `python -m src.model --train` first.")
