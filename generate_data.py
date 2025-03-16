import pandas as pd
import numpy as np

# Generate dates for the last 30 days
date_range = pd.date_range(end=pd.Timestamp.today(), periods=30)

# Simulate normal daily water usage (between 120-200 liters)
water_usage = np.random.randint(120, 200, size=30)

# Introduce random anomalies (very high usage on some days)
anomaly_indices = np.random.choice(30, size=3, replace=False)  # 3 anomaly days
water_usage[anomaly_indices] = water_usage[anomaly_indices] * np.random.randint(2, 4)  # 2x-4x spike

# Create DataFrame
df = pd.DataFrame({"Date": date_range, "Water_Usage_Liters": water_usage})

# Save to CSV
df.to_csv("water_usage.csv", index=False)

print("Simulated water usage data saved as 'water_usage.csv'")
