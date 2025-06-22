import pandas as pd

df = pd.read_csv("C:/Personal Files/Lahore-AQI/lahore_aqi.csv")

df["timestamp"]=pd.to_datetime(df["timestamp"])

df["hour"]=df["timestamp"].dt.hour
df["day"]=df["timestamp"].dt.day
df["month"]=df["timestamp"].dt.month

df["aqi_change_rate"] = df["aqi"].diff()

df.to_csv("lahore_aqi_features.csv", index=False)

print(df.tail())
