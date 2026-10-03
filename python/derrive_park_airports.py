import pandas as pd
from python.methods import haversine_distance

parks = pd.read_csv("../data/processed/national_parks.csv")
airports = pd.read_csv("../data/processed/airports.csv")


# Calculate every park-airport combination
results = []

for _, park in parks.iterrows():

    for _, airport in airports.iterrows():

        distance = haversine_distance(
            park["latitude"],
            park["longitude"],
            airport["latitude"],
            airport["longitude"]
        )

        # Keep airports within 300 miles
        if distance <= 300:

            results.append({
                "parkCode": park["parkCode"],
                "airport_code": airport["airport_code"],
                "airport_name": airport["airport_name"],
                "distance_miles": round(distance, 1)
            })


# Convert to DataFrame
park_airports = pd.DataFrame(results)




# Save
park_airports.to_csv(
    "../data/processed/park_airports.csv",
    index=False
)



