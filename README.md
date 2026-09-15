# 💧 Water - Forecast
# 💧 Water Forecast

**AI-Based Water Demand Forecasting for Campus Operations**

Category: Water Management | Difficulty: Intermediate–Advanced

🔗 **Live Demo:** [water-forecast-7fa6.onrender.com](https://water-forecast-7fa6.onrender.com)
> Hosted on Render's free tier — the app may take 30–60 seconds to wake up on first load.

---

## 📖 Project Overview

Campuses often struggle with managing daily water demand across hostels, canteens, academic blocks, and gardens. Suboptimal pumping causes shortages or over-pumping, increasing both water and electricity consumption.

This project provides a **machine learning-powered dashboard** that:

- Predicts **next-day water consumption** per campus zone.
- Compares consumption across **zones** (Academic Blocks, Hostels, Garden).
- Suggests **optimized pumping schedules** to reduce energy use and over-pumping.

---

## ✨ Features

- **Interactive Forecast** — Predict water demand for a selected zone and date range.
- **Zone Comparison** — Visualize predicted consumption across all zones.
- **Professional Dashboard** — Clean, interactive visualizations using Streamlit and Matplotlib.
- **Energy Insights** — Optional metrics for baseline vs. optimized pumping.

---

## 🗂️ Project Structure

```
water-forecast/
├── data/               # raw, processed, and sample datasets
├── notebooks/          # EDA and experimentation notebooks
├── src/                # core data/ML logic (loader, features, model, optimizer)
├── models/             # saved trained model artifacts
├── dashboard/          # Streamlit app and pages
├── tests/              # unit tests
└── docs/               # architecture notes and screenshots
```

See [`docs/architecture.md`](docs/architecture.md) for how the pieces fit together.

---

## 🚀 Getting Started

### 1. Clone and set up environment
```bash
git clone https://github.com/<your-username>/water-forecast.git
cd water-forecast
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add data
Place your consumption data in `data/raw/`, or use the provided sample in `data/sample/` to try the dashboard immediately.

> 📌 **Note on data:** The bundled dataset (`data/sample/sample_water_consumption.csv`) is **synthetic demo data**, generated to resemble realistic campus water usage patterns — it is not real campus data. Drop your own dataset into `data/raw/consumption.csv` (matching the format below) to use real data instead.

### 3. Run the dashboard
```bash
streamlit run dashboard/app.py
```

### 4. (Optional) Train the model
```bash
python -m src.model --train
```

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** — dashboard UI
- **scikit-learn** — forecasting model
- **pandas / numpy** — data processing
- **matplotlib** — visualizations

---

## 📊 Data Format

Expected columns in `data/raw/consumption.csv`:

| column         | description                              |
|----------------|-------------------------------------------|
| `date`         | YYYY-MM-DD                                 |
| `zone`         | one of: Academic Block, Hostel, Garden     |
| `consumption`  | liters consumed that day                   |
| `temperature`  | (optional) avg daily temperature °C        |
| `occupancy`    | (optional) estimated headcount for zone    |

---

## 🗺️ Roadmap

- [x] Baseline forecasting model (Random Forest)
- [x] Streamlit multi-page dashboard
- [x] Zone comparison view
- [x] Pumping schedule optimizer
- [x] Energy savings insights panel
- [x] Deploy to Render
- [ ] Add Prophet/XGBoost as alternative forecasting models
- [ ] Swap in real campus consumption data

---

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss what you'd like to change before submitting a pull request.

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
