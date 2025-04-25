import os
import numpy as np
import pandas as pd

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Parameters
n_samples = 150
np.random.seed(42)

# Feature ranges (realistic synthetic ranges)
temp = np.random.uniform(120, 180, n_samples)              # Drying temp in °C
feed_rate = np.random.uniform(2.0, 5.0, n_samples)          # mL/min
airflow = np.random.uniform(100, 200, n_samples)           # m^3/h
moisture = np.random.uniform(0.01, 0.08, n_samples)        # % final moisture

# Synthetic particle size generation based on inputs (linear + noise model)
# Hypothetical formula: larger temp & feed rate = larger particle; more moisture = smaller
particle_size = (
    0.05 * temp +
    1.2 * feed_rate -
    0.1 * airflow -
    200 * moisture +
    np.random.normal(0, 2, n_samples)  # Add Gaussian noise
)

# Clip to realistic size range
particle_size = np.clip(particle_size, 5, 50)

# Create DataFrame
df = pd.DataFrame({
    "temp": temp,
    "feed_rate": feed_rate,
    "airflow": airflow,
    "moisture": moisture,
    "particle_size": particle_size
})

# Save to CSV
df.to_csv("data/sample_data.csv", index=False)
print("✅ Synthetic data generated and saved to data/sample_data.csv")