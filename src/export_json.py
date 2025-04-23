# src/export_json.py

import json
import pandas as pd
from sqlalchemy import create_engine

def export_to_json(
    db_path="data/sensor_data.db",
    table="sensor_hourly",
    json_path="data/sensor_hourly.json"
):
    """
    Reads the hourly-aggregated table from SQLite and writes it to JSON.
    """
    engine = create_engine(f"sqlite:///{db_path}")
    # Load table
    df = pd.read_sql_query(f"SELECT * FROM {table}", con=engine, parse_dates=["timestamp"])
    # Convert to records
    records = df.to_dict(orient="records")
    # Write JSON
    with open(json_path, "w") as f:
        json.dump(records, f, indent=2, default=str)
    print(f"Wrote {len(records)} records to {json_path}")

if __name__ == "__main__":
    export_to_json()
