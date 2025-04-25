import os
import random
from datetime import datetime, timedelta
import csv

# Ensure target directory exists
os.makedirs("data", exist_ok=True)

# Output file path
output_path = "data/weather.csv"

# Config
start_year = 2000
end_year = 2023
records_per_year = 50  # adjustable

# Generate random temperature for a given date range
def generate_weather_data():
    data = []
    for year in range(start_year, end_year + 1):
        for _ in range(records_per_year):
            # Generate random date in the year
            start_date = datetime(year, 1, 1)
            random_days = random.randint(0, 364)
            date = start_date + timedelta(days=random_days)

            # Generate temperature (more cold in early years, more warm recently)
            base_temp = random.uniform(-5, 10) if year < 2010 else random.uniform(10, 35)
            noise = random.uniform(-2, 2)
            temperature = round(base_temp + noise, 1)

            data.append([date.strftime("%Y-%m-%d"), temperature])
    return data

# Write to CSV
with open(output_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    # No header as per mapper.py
    for row in generate_weather_data():
        writer.writerow(row)

print(f"✅ Synthetic weather data written to {output_path}")
