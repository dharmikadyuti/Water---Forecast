# Architecture

## Data flow

```
data/raw/consumption.csv
        │
        ▼
  src/data_loader.py   (load + clean)
        │
        ▼
src/feature_engineering.py  (date parts, lags, rolling means)
        │
        ▼
     src/model.py       (train RandomForestRegressor → models/saved_model.pkl)
        │
        ▼
    src/forecast.py     (recursive next-day / N-day forecasting)
        │
   ┌────┴─────┐
   ▼          ▼
src/zone_comparison.py   src/pumping_optimizer.py
   │                          │
   ▼                          ▼
        dashboard/app.py + dashboard/pages/*.py
                (Streamlit UI)
```

## Design decisions

- **Single model, multiple zones**: rather than training one model per zone,
  `zone` is one-hot encoded as a feature. This keeps the pipeline simple and
  lets the model learn shared seasonal/weekly patterns across zones. If zones
  behave very differently, consider per-zone models instead.

- **Recursive forecasting**: multi-day forecasts feed each day's prediction
  back in as "history" so lag features stay valid further into the future.
  Accuracy naturally degrades the further out you forecast.

- **Baseline vs. optimized pumping**: the baseline assumes a naive
  "always pump to historical peak" policy. The optimized policy pumps to
  forecasted demand plus a safety margin (`SAFETY_MARGIN` in
  `src/pumping_optimizer.py`). The delta between the two is used as an
  estimated savings metric — this is illustrative, not a hydraulic simulation.

## Extending this project

- Swap `RandomForestRegressor` for `Prophet` or `XGBoost` in `src/model.py`.
- Add weather/occupancy as live features instead of static columns.
- Add a proper backtesting harness in `tests/` or `notebooks/`.
- Persist forecasts to a database for historical accuracy tracking.
