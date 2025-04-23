# src/aggregate.py

import pandas as pd
from sqlalchemy import create_engine, text

def aggregate_hourly(db_path, input_table="sensor_readings", output_table="sensor_hourly"):
    """
    Reads raw sensor data from SQLite, computes hourly averages,
    and writes results to a new table.
    """
    engine = create_engine(f"sqlite:///{db_path}")

    # Load raw data
    df = pd.read_sql_table(input_table, con=engine, parse_dates=["timestamp"])
    df.set_index("timestamp", inplace=True)

    # Resample hourly and compute means
    hourly = df.resample("H").mean().reset_index()
    hourly["hour"] = hourly["timestamp"].dt.strftime("%Y-%m-%d %H:00:00")

    # Write hourly table
    hourly.to_sql(output_table, con=engine, if_exists="replace", index=False)
    print(f"Wrote {len(hourly)} rows to `{output_table}` in {db_path}")

    # Print a preview
    print(hourly.head())

if __name__ == "__main__":
    aggregate_hourly(db_path="data/sensor_data.db")
