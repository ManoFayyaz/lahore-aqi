import hopsworks
import pandas as pd

# Load your features
df = pd.read_csv("lahore_aqi_features.csv")

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Login to Hopsworks
project = hopsworks.login(api_key_value="HOPSWORKS_API_KEY")
fs = project.get_feature_store()

feature_group = fs.get_or_create_feature_group(
    name="lahore_aqi_data",
    version=1,
    description="AQI features from Lahore",
    primary_key=["timestamp"],          # must exist in df
    event_time="timestamp"              # must exist and be datetime type
)

# Step 2: Ensure 'timestamp' is datetime type
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Step 3: Insert data into the feature group
feature_group.insert(df)
