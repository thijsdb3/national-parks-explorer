import pandas as pd

airport_data = pd.read_csv("../data/raw/airports.csv")

US_CODES = [
    "US",
    "AS",  # American Samoa
    "VI",  # U.S. Virgin Islands
    "PR",  # Puerto Rico
    "GU",  # Guam
    "MP"   # Northern Mariana Islands
]
# selecting scheduled commercial US airports
airport_data = airport_data[
    (airport_data["iso_country"].isin(US_CODES)) &
    (airport_data["scheduled_service"] == "yes") &
    (airport_data["iata_code"].notna())
]
# only want the distance from national parks and enough data to identify the airport
airport_data = airport_data[
    [
        "iata_code",
        "name",
        "latitude_deg",
        "longitude_deg",
        "iso_country",
        "type"
    ]
]

airport_data = airport_data.rename(columns={
    "iata_code": "airport_code",
    "name": "airport_name",
    "latitude_deg": "latitude",
    "longitude_deg": "longitude",
    "iso_country": "country_code",
})

airport_data["latitude"] = pd.to_numeric(airport_data["latitude"])
airport_data["longitude"] = pd.to_numeric(airport_data["longitude"])

airport_data = airport_data.drop_duplicates("airport_code")
airport_data.to_csv(
    "../data/processed/airports.csv",
    index=False
)
