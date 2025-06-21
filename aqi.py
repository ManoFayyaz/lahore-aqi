import requests
import pandas as pd
from datetime import datetime
import os

# Config
API_KEY = "d795e69b955f35e7baecbeee690c6630"  # Replace with your real key
LAT = "31.5497"
LON = "74.3436"

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(url)
data = response.json()

aqi_data = data["list"][0]
aqi = aqi_data["main"]["aqi"]
components = aqi_data["components"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create DataFrame
df = pd.DataFrame([{
    "timestamp": timestamp,
    "aqi": aqi,
    "pm2_5": components["pm2_5"],
    "pm10": components["pm10"],
    "no2": components["no2"],
    "so2": components["so2"],
    "co": components["co"],
    "no": components["no"],
    "o3": components["o3"],
    "nh3": components["nh3"]
}])

# Save to CSV (append if exists)
filename = "lahore_aqi.csv"
file_exists = os.path.isfile(filename)
df.to_csv(filename, mode='a', index=False, header=not file_exists)

print("✅ Lahore AQI data saved.")
print(df.head())  