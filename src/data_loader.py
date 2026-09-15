"""
Load and clean raw water consumption data.
"""

import pandas as pd
from src.config import RAW_DATA_FILE, SAMPLE_DATA_FILE


def load_data(use_sample: bool = False) -> pd.DataFrame:
    """
    Load consumption data from disk.

    Args:
        use_sample: if True, load the bundled sample dataset instead of
                    the (gitignored) raw data file.

    Returns:
        DataFrame with columns: date, zone, consumption, [temperature, occupancy]
    """
    path = SAMPLE_DATA_FILE if use_sample else RAW_DATA_FILE

    if not path.exists():
        raise FileNotFoundError(
            f"No data file found at {path}. "
            f"Add your data to data/raw/consumption.csv, "
            f"or pass use_sample=True to use the bundled sample."
        )

    df = pd.read_csv(path, parse_dates=["date"])
    return clean_data(df)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop duplicates, sort, handle missing values."""
    df = df.drop_duplicates(subset=["date", "zone"])
    df = df.sort_values(["zone", "date"]).reset_index(drop=True)

    # Forward-fill small gaps in consumption per zone, then drop any
    # remaining rows that still have no target value.
    df["consumption"] = df.groupby("zone")["consumption"].transform(
        lambda s: s.ffill().bfill()
    )
    df = df.dropna(subset=["consumption"])

    return df
