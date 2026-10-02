
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NPS_API_KEY")

if not API_KEY:
    raise ValueError("NPS_API_KEY was not loaded from .env")

url = "https://developer.nps.gov/api/v1/parks"

params = {
    "limit": 500,
    "start": 0
}

headers = {
    "X-Api-Key": API_KEY
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    "../data/raw/parks_raw.csv",
    index=False
)

print(f"Saved {len(df)} parks to parks_raw.csv")
