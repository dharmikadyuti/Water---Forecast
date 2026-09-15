import pandas as pd
from src.data_loader import clean_data


def test_clean_data_drops_duplicates():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-01", "2025-01-02"]),
        "zone": ["Hostel", "Hostel", "Hostel"],
        "consumption": [100, 100, 110],
    })
    cleaned = clean_data(df)
    assert len(cleaned) == 2


def test_clean_data_fills_missing_values():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]),
        "zone": ["Hostel", "Hostel", "Hostel"],
        "consumption": [100, None, 120],
    })
    cleaned = clean_data(df)
    assert cleaned["consumption"].isna().sum() == 0
