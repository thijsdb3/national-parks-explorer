import os

import openrouteservice
import pandas as pd
from dotenv import load_dotenv

from methods import LA_LAT, LA_LON

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

if not ORS_API_KEY:
    raise ValueError("ORS_API_KEY not found in .env")

client = openrouteservice.Client(key=ORS_API_KEY)

parks = pd.read_csv("../data/processed/national_parks.csv")


coordinates = [
    (LA_LON, LA_LAT)
]

coordinates.extend(
    zip(
        parks["longitude"],
        parks["latitude"]
    )
)

matrix = client.distance_matrix(
    locations=coordinates,
    profile="driving-car",
    metrics=["distance", "duration"],
    sources=[0],
    destinations=list(range(1, len(coordinates))),
    units="m"
)



distances = matrix["distances"][0]
durations = matrix["durations"][0]

parks["driving_distance_from_la_miles"] = [
    round(d / 1609.344, 1)
    if d is not None else None
    for d in distances
]

parks["driving_time_from_la_hours"] = [
    round(t / 3600, 2)
    if t is not None else None
    for t in durations
]

parks["driving_route_found"] = [
    d is not None
    for d in distances
]


parks.to_csv(
    "../data/processed/national_parks.csv",
    index=False
)

print(
    f"Routes found: "
    f"{parks['driving_route_found'].sum()} / {len(parks)}"
)

print("\nResults:")

print(
    parks[
        [
            "Park Name",
            "driving_distance_from_la_miles",
            "driving_time_from_la_hours",
            "driving_route_found"
        ]
    ]
    .sort_values("driving_time_from_la_hours")
    .to_string(index=False)
)