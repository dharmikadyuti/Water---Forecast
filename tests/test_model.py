import pandas as pd
from src.model import train_model


def make_dummy_data(n_days=40):
    dates = pd.date_range("2025-01-01", periods=n_days, freq="D")
    rows = []
    for zone in ["Academic Block", "Hostel", "Garden"]:
        for i, d in enumerate(dates):
            rows.append({"date": d, "zone": zone, "consumption": 1000 + i * 10})
    return pd.DataFrame(rows)


def test_train_model_runs_and_predicts():
    df = make_dummy_data()
    model = train_model(df)
    assert hasattr(model, "predict")
    assert len(model.feature_names_) > 0
