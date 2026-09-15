"""
Central configuration: file paths, zone definitions, and model constants.
"""

from pathlib import Path

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
DATA_SAMPLE_DIR = BASE_DIR / "data" / "sample"
MODELS_DIR = BASE_DIR / "models"

RAW_DATA_FILE = DATA_RAW_DIR / "consumption.csv"
SAMPLE_DATA_FILE = DATA_SAMPLE_DIR / "sample_water_consumption.csv"
MODEL_FILE = MODELS_DIR / "saved_model.pkl"

# --- Domain constants ---
ZONES = ["Academic Block", "Hostel", "Garden"]

# --- Model constants ---
LAG_DAYS = [1, 2, 3, 7]
ROLLING_WINDOWS = [3, 7]
RANDOM_STATE = 42
