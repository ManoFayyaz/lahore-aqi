import pandas as pd
from datetime import datetime,timedelta
import time
import requests
import os

api_key="d795e69b955f35e7baecbeee690c6630"
LAT = 31.5497
LON = 74.3436

end_time = int(time.mktime(datetime(2025, 6, 20).timetuple()))
start_time = end_time - (130 * 86400)

url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={LAT}&lon={LON}&start={start_time}&end={end_time}&appid={api_key}"

response = requests.get(url)    

if response.status_code == 200:
    data = response.json()
    aqi_data = data["list"]
    
    records = []
    for entry in aqi_data:
        timestamp = datetime.fromtimestamp(entry["dt"]).strftime("%Y-%m-%d %H:%M:%S")
        aqi = entry["main"]["aqi"]
        components = entry["components"]
        
        record = {
            "timestamp": timestamp,
            "aqi": aqi,
            "pm2_5": components.get("pm2_5", None),
            "pm10": components.get("pm10", None),
            "no2": components.get("no2", None),
            "so2": components.get("so2", None),
            "co": components.get("co", None),
            "no": components.get("no", None),
            "o3": components.get("o3", None),
            "nh3": components.get("nh3", None)
        }
        records.append(record)

  #  Create DataFrame
    new_df = pd.DataFrame(records)

    #  Path to your CSV
    file_path = "lahore_aqi.csv"

    #  Prepend to existing data if exists
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        combined_df = pd.concat([new_df, existing_df], ignore_index=True)
    else:
        combined_df = new_df

    #  Save the combined DataFrame to CSV
    combined_df.to_csv(file_path, index=False)

    print("✅ Historical AQI data saved at the start of the file.")