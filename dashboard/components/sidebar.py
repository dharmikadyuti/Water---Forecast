"""
Reusable sidebar controls (zone selector, date range/horizon picker).
"""

import streamlit as st
from src.config import ZONES


def zone_selector(key: str = "zone_select") -> str:
    return st.sidebar.selectbox("Select zone", ZONES, key=key)


def horizon_selector(key: str = "horizon_select") -> int:
    return st.sidebar.slider(
        "Forecast horizon (days)", min_value=1, max_value=14, value=7, key=key
    )
