import pandas as pd
import pytest
from src.forecast import forecast_zone


def test_forecast_zone_rejects_unknown_zone():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01"]),
        "zone": ["Hostel"],
        "consumption": [100],
    })
    with pytest.raises(ValueError):
        forecast_zone(df, "Not A Real Zone")
