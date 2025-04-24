import pandas as pd


from sqlalchemy import create_engine, text

def load_csv_to_sqlite(csv_path, db_path, table_name="sensor_readings"):
    # 1. Read CSV
    df = pd.read_csv(csv_path, parse_dates=["timestamp"])

    # 2. Create SQLite engine (will create the file if it doesn't exist)
    engine = create_engine(f"sqlite:///{db_path}")

    # 3. Write to SQL (replace any existing table)
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Wrote {len(df)} rows to {db_path} → table `{table_name}`")

    # 4. Example query: get basic stats
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT MIN(temp_c) AS min_temp, MAX(temp_c) AS max_temp, "
            "ROUND(AVG(vibration), 3) AS avg_vib FROM sensor_readings"
        )).mappings()
        stats = result.fetchone()
        print("Stats:", dict(stats))

if __name__ == "__main__":
    load_csv_to_sqlite(
        csv_path="data/sensor_readings.csv",
        db_path="data/sensor_data.db"
    )

