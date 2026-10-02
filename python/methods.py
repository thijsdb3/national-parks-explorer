import numpy as np

# the df needs "latitude" and "longitude" column
def calculate_distance_from_la(df):
    LA_LAT = 34.0522
    LA_LON = -118.2437

    lat1 = np.radians(LA_LAT)
    lon1 = np.radians(LA_LON)

    lat2 = np.radians(df["latitude"])
    lon2 = np.radians(df["longitude"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return 3958.8 * c