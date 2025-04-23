[![ETL Pipeline](https://github.com/Aminshr/drive-train-dash/actions/workflows/etl.yml/badge.svg)](https://github.com/Aminshr/drive-train-dash/actions)
[![GitHub Pages](https://github.com/Aminshr/drive-train-dash/actions/workflows/pages/pages-build-deployment/badge.svg)](https://aminshr.github.io/drive-train-dash/dashboard/index.html)


# drive-train-dash

A predictive-maintenance & logistics dashboard for drive-train components.

## Project Structure

- **data/**
  - `data_simulator.py` – generates fake sensor data CSV  
  - `sensor_readings.csv` – sample output  
- **src/**
  - `etl.py` – loads CSV into SQLite and prints summary stats  
- **venv/** – Python virtual environment  
- `requirements.txt` – project dependencies  
- `.gitignore` – files & folders to ignore (optional)  
- `README.md` – this file

## Live Demo
🔗 https://aminshr.github.io/drive-train-dash/dashboard/index.html

## Getting Started

1. **Clone** the repo  
   ```bash
   git clone git@github.com:Aminshr/drive-train-dash.git
   cd drive-train-dash


