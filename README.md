# Drive-Train-Dash

[![ETL Pipeline](https://github.com/Aminshr/drive-train-dash/actions/workflows/etl.yml/badge.svg)](https://github.com/Aminshr/drive-train-dash/actions/workflows/etl.yml)
[![Pages Build & Deployment](https://github.com/Aminshr/drive-train-dash/actions/workflows/pages-build-deployment.yml/badge.svg)](https://github.com/Aminshr/drive-train-dash/actions/workflows/pages-build-deployment.yml)

A **Predictive Maintenance & Logistics Dashboard** for drive-train components, showcasing end-to-end data engineering skills: data ingestion, ETL, automation, aggregation, JSON export, and interactive visualization.

---

## 📋 Table of Contents
1. [Overview](#-overview)
2. [Live Demo](#-live-demo)
3. [Key Features](#-key-features)
4. [Project Structure](#-project-structure)
5. [Tech Stack](#-tech-stack)
6. [Getting Started](#-getting-started)
7. [Usage](#-usage)
8. [Automation & CI/CD](#-automation--cicd)
9. [Contributing](#-contributing)
10. [License](#-license)

---

## 🔍 Overview

## 🏆 Skills Demonstrated

- **Python 3.10**: pandas & SQLAlchemy for data ingestion, ETL, and aggregation
- **SQL (SQLite)**: designing tables, writing SQL queries for stats and resampling
- **JavaScript (ES6)**: data fetching, KPI computations, and Chart.js visualizations
- **HTML5 & CSS3**: structuring and styling a responsive dashboard
- **JSON**: exporting and consuming data for front-end integration
- **CI/CD**: GitHub Actions for automated ETL, testing, and GitHub Pages deployment


This repository simulates drive-train sensor data and demonstrates a full data engineering workflow:

- **Simulate** time-series temperature & vibration data
- **ETL**: load CSV into SQLite, compute statistics
- **Aggregate**: hourly resampling & storage
- **Export**: output JSON for front-end
- **CI/CD**: automated daily ETL & aggregation via GitHub Actions
- **Visualize**: interactive dashboard with KPIs & charts via Chart.js

Perfect for showcasing Python, SQL (SQLite), GitHub Actions, JSON pipelines, and front-end visualization skills.

---

## 🚀 Live Demo

View the hosted dashboard on GitHub Pages:

[https://aminshr.github.io/drive-train-dash/dashboard/index.html](https://aminshr.github.io/drive-train-dash/dashboard/index.html)

---

## ⭐ Key Features

- **Data Simulation**: realistic sensor readings at 1-minute intervals
- **Data Pipeline**: modular Python scripts (`etl.py`, `aggregate.py`, `export_json.py`)
- **Automation**: daily scheduled ETL & aggregation with GitHub Actions
- **Interactive Dashboard**: KPI cards, line charts, tooltips, responsive design
- **Clean Project Layout**: `.github` workflows, `data/`, `src/`, and `dashboard/`

---

## 🗂️ Project Structure

```
drive-train-dash/
├── .github/            # CI/CD workflows
│   └── workflows/
│       ├── etl.yml
│       └── pages-build-deployment.yml
├── data/               # raw & aggregated data
│   ├── sensor_readings.csv
│   └── sensor_hourly.json
├── dashboard/          # static front-end
│   └── index.html      # interactive Chart.js dashboard
├── src/                # Python pipeline scripts
│   ├── etl.py          # load CSV → SQLite + stats
│   ├── aggregate.py    # hourly resample → SQLite
│   └── export_json.py  # JSON export of hourly data
├── requirements.txt    # Python dependencies
└── README.md           # this file
```

---

## 🛠️ Tech Stack

- **Python 3.10**: pandas, SQLAlchemy
- **SQLite**: lightweight relational store for ETL & aggregation
- **GitHub Actions**: CI/CD for ETL pipeline and Pages deployment
- **Chart.js**: interactive, responsive charts in the browser
- **JSON**: data interchange between back-end and front-end

---

## ⚙️ Getting Started

1. **Clone the repo**
   ```bash
   git clone git@github.com:Aminshr/drive-train-dash.git
   cd drive-train-dash
   ```
2. **Set up Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run locally**
   ```bash
   # simulate data
   python src/data_simulator.py
   # run ETL
   python src/etl.py
   # aggregate hourly
   python src/aggregate.py
   # export JSON
   python src/export_json.py
   # open dashboard in browser
   open dashboard/index.html
   ```

---

## 🔄 Automation & CI/CD

- **ETL Pipeline**: scheduled nightly at UTC midnight (`.github/workflows/etl.yml`)
- **Dashboard Deployment**: GitHub Pages build on every push (`.github/workflows/pages-build-deployment.yml`)

Badges at the top of this README reflect real-time status.

---

## 🤝 Contributing

Contributions welcome! Feel free to open issues or pull requests for:
- Adding new visualization types (histogram, scatter)
- Integrating with a real cloud data store (AWS RDS, S3)
- Enhancing ETL with error handling & logging

---

## 📄 License

This project is released under the **MIT License**. See [LICENSE](./LICENSE) for details.

