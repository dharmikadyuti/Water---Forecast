"""
Energy Insights page — baseline vs. optimized pumping metrics.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st
from src.data_loader import load_data
from src.forecast import forecast_all_zones
from src.pumping_optimizer import estimate_savings
from src.config import RAW_DATA_FILE
from dashboard.components.sidebar import horizon_selector
from dashboard.components.charts import plot_savings_bar

st.set_page_config(page_title="Energy Insights — Water Forecast", page_icon="⚡", layout="wide")
st.title("⚡ Energy Insights")

st.caption(
    "Compares a static 'always pump to historical peak' baseline against "
    "a demand-based optimized schedule using the forecast model."
)

horizon = horizon_selector()

use_sample = not RAW_DATA_FILE.exists()
df = load_data(use_sample=use_sample)

try:
    forecast_df = forecast_all_zones(df, days_ahead=horizon)
    savings_df = estimate_savings(df, forecast_df)

    st.subheader("Estimated savings by zone")
    fig = plot_savings_bar(savings_df)
    st.pyplot(fig)

    st.dataframe(savings_df, use_container_width=True)

    total_savings_pct = savings_df["savings_pct"].mean()
    st.metric("Average estimated savings", f"{total_savings_pct:.1f}%")

except FileNotFoundError:
    st.warning("No trained model found yet. Run `python -m src.model --train` first.")
