# data/data_simulator.py

import csv
import random
import datetime

def generate_sensor_data(filename, num_records=1440):
    """
    Generates `num_records` of time-series sensor data at 1-minute intervals.
    Columns: timestamp (ISO), temp_c (°C), vibration (g).
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp","temp_c","vibration"])
        start = datetime.datetime.now() - datetime.timedelta(days=1)
        for i in range(num_records):
            ts = start + datetime.timedelta(minutes=i)
            temp = 50 + random.gauss(0, 2)       # avg 50°C ±2
            vib  = 0.5 + random.gauss(0, 0.1)     # avg 0.5g ±0.1
            writer.writerow([ts.isoformat(), round(temp,2), round(vib,3)])

if __name__ == "__main__":
    generate_sensor_data("data/sensor_readings.csv")
    print("Generated data/sensor_readings.csv")
