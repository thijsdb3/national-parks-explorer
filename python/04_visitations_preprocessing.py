import pandas as pd

df = pd.read_csv("../data/raw/visitations.csv")

#since the park codes in national_parks.csv are lower letter
df["UnitCode"] = df["UnitCode"].str.strip().str.lower()

#  parks table has seki instead of kica
df["UnitCode"] = df["UnitCode"].replace({
    "kica": "seki"
})

# Keep total recreation visits
df = df[df["Statistic"] == "TRV"]

# keeping last 10 years
df = df[df["Year"].between(2015, 2025)]

# Sum the 12 months to get annual visitation
annual_visitations = (
    df.groupby(["UnitCode", "Year"], as_index=False)["Value"]
      .sum()
)

# Convert Year into columns
annual_visitations = annual_visitations.pivot(
    index="UnitCode",
    columns="Year",
    values="Value"
).reset_index()

# Rename columns
annual_visitations = annual_visitations.rename(columns={
    "UnitCode": "parkCode"
})

annual_visitations.columns = [
    "parkCode" if col == "parkCode" else f"visitors_{int(col)}"
    for col in annual_visitations.columns
]
visitor_columns = [
    col for col in annual_visitations.columns
    if col.startswith("visitors_")
]

annual_visitations[visitor_columns] = (
    annual_visitations[visitor_columns].astype("Int64")
)
parks = pd.read_csv("../data/processed/national_parks.csv")

annual_visitations = annual_visitations[annual_visitations["parkCode"].isin(parks["parkCode"])]
annual_visitations.to_csv("../data/processed/annual_visitations.csv", index=False)

