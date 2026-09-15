"""
Campus Water Dashboard — main entry point.

Run with:
    streamlit run dashboard/app.py
"""

import sys
from pathlib import Path

# Make `src` importable when Streamlit runs this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.data_loader import load_data
from src.config import SAMPLE_DATA_FILE, RAW_DATA_FILE

st.set_page_config(
    page_title="Water Forecast",
    page_icon="💧",
    layout="wide",
)

st.title("💧 Water Forecast")
st.markdown("**AI-Based Water Demand Forecasting for Campus Operations**")

st.markdown(
    """
    Use the sidebar to navigate between pages:

    - **Forecast** — predict next-day water demand for a selected zone.
    - **Zone Comparison** — compare predicted consumption across all zones.
    - **Energy Insights** — baseline vs. optimized pumping metrics.
    """
)

use_sample = not RAW_DATA_FILE.exists()
if use_sample:
    st.info(
        f"No raw data found at `data/raw/consumption.csv` — using the bundled "
        f"sample dataset (`{SAMPLE_DATA_FILE.name}`) for this demo."
    )

try:
    df = load_data(use_sample=use_sample)
    st.session_state["data"] = df
    st.success(f"Loaded {len(df):,} rows across {df['zone'].nunique()} zones.")
    st.dataframe(df.tail(10), use_container_width=True)
except FileNotFoundError as e:
    st.error(str(e))
