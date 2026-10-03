import pandas as pd
from python.methods import calculate_distance_from_la

np_data = pd.read_csv("../data/raw/parks_raw.csv")

#filtering to only National Parks instead of National Historic , National Recreation,....
# some manual checking was unfortunately required for this step
np_data = np_data[
    np_data["designation"].isin([
        "National Park",
        "National Park & Preserve",
        "National Parks"
    ])
    | np_data["parkCode"].isin(["redw","npsa"])
]

np_data = np_data.drop_duplicates("parkCode")

# 62 entities instead of 63 National Parks:
# Since many of the visualizations in this project rely on latitude/longitude and mapping,
# I decided not to split  these records.
print(np_data.shape)

np_data["state"] = np_data["states"].str.strip()
park_states = np_data.drop(columns="states")
np_data.rename(columns={"name": "Park Name"}, inplace=True)
keep_columns = [
    "parkCode",
    "Park Name",
    "latitude",
    "longitude",
    "state"
]
np_data["latitude"] = pd.to_numeric(np_data["latitude"])
np_data["longitude"] = pd.to_numeric(np_data["longitude"])

np_data = np_data[keep_columns]

np_data["distance_from_la_miles"] = calculate_distance_from_la(np_data)


# Save processed data
np_data.to_csv("../data/processed/national_parks.csv", index=False)

