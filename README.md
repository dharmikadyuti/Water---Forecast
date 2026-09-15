# 💧 Water Forecast

**AI-Based Water Demand Forecasting for Campus Operations**

Category: Water Management | Difficulty: Intermediate–Advanced

[![Tests](https://github.com/dharmikadyuti/Water---Forecast/actions/workflows/tests.yml/badge.svg)](https://github.com/dharmikadyuti/Water---Forecast/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)

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
├── .github/workflows/  # CI pipeline (automated testing)
├── data/               # raw, processed, and sample datasets
├── notebooks/          # EDA and experimentation notebooks
├── src/                # core data/ML logic (loader, features, model, optimizer)
├── models/             # saved trained model artifacts
├── dashboard/          # Streamlit app and pages
├── tests/              # unit tests
├── docs/               # architecture notes and screenshots
└── render.yaml         # infra-as-code deployment config for Render
```

See [`docs/architecture.md`](docs/architecture.md) for how the pieces fit together.

---

## 🚀 Getting Started

### 1. Clone and set up environment
```bash
git clone https://github.com/dharmikadyuti/Water---Forecast.git
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

### 5. Run tests locally
```bash
pytest tests/ -v
```

---

## 🧠 Tech Stack

- **Python 3.11+**
- **Streamlit** — dashboard UI
- **scikit-learn** — forecasting model
- **pandas / numpy** — data processing
- **matplotlib** — visualizations
- **GitHub Actions** — CI (automated testing on every push)
- **Render** — hosting/deployment

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

## ⚙️ CI/CD

This repo uses **GitHub Actions** (`.github/workflows/tests.yml`) to automatically:

- Run the full `pytest` suite on every push and pull request to `main`.
- Test against both Python 3.11 and 3.12 in parallel (matrix build).
- Verify the model can train end-to-end on the sample dataset, catching pipeline-breaking changes before they merge.

Deployment to **Render** is configured as infra-as-code via [`render.yaml`](render.yaml) — the build command, start command, and Python version are version-controlled alongside the app, so the deployment environment is reproducible rather than manually configured through Render's dashboard. `autoDeploy: true` means every push to `main` automatically redeploys the live demo.

---

## 🔧 Git Workflow

Commands used to initialize, version, and push this project to GitHub:

```bash
# Initialize a local git repository
git init
git --version
git status

# Stage and commit all project files
git add .
git commit -m "Initial commit"

# Rename default branch to main
git branch -M main

# Connect to the remote GitHub repository
git remote add origin https://github.com/dharmikadyuti/Water---Forecast.git
git remote -v

# Push local commits to GitHub
git push -u origin main

# Sync with remote changes (e.g. README created on GitHub) before pushing again
git pull origin main --allow-unrelated-histories

# Resolve merge conflicts, then commit and push
git add README.md
git commit -m "Resolve README conflict"
git push -u origin main
```

---

## 🗺️ Roadmap

- [x] Baseline forecasting model (Random Forest)
- [x] Streamlit multi-page dashboard
- [x] Zone comparison view
- [x] Pumping schedule optimizer
- [x] Energy savings insights panel
- [x] Deploy to Render
- [x] CI pipeline for automated testing
- [ ] Add Prophet/XGBoost as alternative forecasting models
- [ ] Swap in real campus consumption data

---

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss what you'd like to change before submitting a pull request.

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
