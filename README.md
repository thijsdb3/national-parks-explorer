# National Parks Explorer

An interactive data visualization project exploring **U.S. National Park visitation and accessibility from Los Angeles**, with a focus on driving distance, travel time, and nearby airports.

Built using **Python, pandas, OpenRouteService, Microsoft Power BI, and DAX**, combining data processing, geospatial analysis, routing, and interactive visualization.


## Dashboard

![National Parks Explorer Dashboard](powerbi/visualisations.pbix)
<img width="1141" height="658" alt="image" src="https://github.com/user-attachments/assets/839e9641-2a8c-4350-8482-3fc384f78140" />

The Power BI dashboard allows users to:

* Explore the locations of U.S. National Parks
* Compare **2025 visitor numbers**
* Explore changes in visitation from **2015–2025**
* Compare straight-line distance and driving time from Los Angeles
* Compare estimated driving times from Los Angeles
* Explore airports located near national parks
* Filter parks by visitations and distance from LA

## Key Questions

The project focuses on several questions:

* Which National Parks are the most and least visited?
* How has visitation changed between 2015 and 2025?
* Which parks are closest to Los Angeles?
* Which parks are realistically accessible by car from Los Angeles?
* How does driving time compare with straight-line distance?
* Which airports provide access to remote national parks?

## Data

### National Park Service

National Park Service data is used for:

* National park locations
* Park identifiers and names
* Annual visitation statistics

Source: [National Park Service](https://home.nps.gov/subjects/digital/nps-data-api.htm)
Source: [National Park Service](https://irma.nps.gov/Stats/Reports/National)

### Airports

Airport data is used to identify airports near national parks.

The project filters U.S. airports with:

* An IATA airport code
* Scheduled service listed in the source data
* Locations within the United States and U.S. territories

Airport proximity is calculated using geographic coordinates.

Source: [OurAirports](https://ourairports.com/data/)

### Driving Routes

Driving distance and estimated driving time from Los Angeles are calculated using the **OpenRouteService API**.

This provides a more realistic accessibility measure than straight-line distance alone.

Source: [OpenRouteService](https://openrouteservice.org/)

## Methodology

### 1. Data collection

Raw datasets are collected from external sources and stored in:

```text
data/raw/
```

### 2. Data preprocessing

Python scripts clean and transform the raw data before it is used in Power BI.

Processed datasets are stored in:

```text
data/processed/
```

The preprocessing includes:

* Filtering National Park Service records
* Cleaning park identifiers
* Preparing annual visitation data
* Filtering airport records
* Calculating distances between parks and airports

### 3. Accessibility analysis

Two types of distance are used:

**Straight-line distance**

Calculated using geographic coordinates between Los Angeles and each national park.

**Driving distance and time**

Calculated using OpenRouteService's `driving-car` routing profile.

This allows the dashboard to distinguish between geographic proximity and actual road accessibility.

### 4. Visualization

The processed datasets are imported into **Microsoft Power BI**.

The dashboard combines:

* Interactive map
* Visitation trend
* Visitor-based filtering
* Park accessibility information
* Nearby airport information

## Project Structure

```text
national-parks-explorer/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── powerbi/
│   └── national_parks.pbix
│
├── python/
│   ├── 01_get_parks.py
│   ├── 02_parks_preprocessing.py
│   ├── 03_get_driving_time.py
|   ├── 04_visitation_preprocessing.py
|   ├── 05_airports_preprocessing.py
|   ├── 06_derrive_park_airports.py
│   └── methods.py
|
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```


## Power BI Data Model

The main relationships are:

```text
National_Parks
      │
      ├────────────── Visitation
      │
      └────────────── Park_Airports ────────────── Airports
```

`National_Parks` acts as the central table connecting park information, visitation, and nearby airports.

## Reproducing the Project

Clone the repository:

```bash
git clone https://github.com/thijsdb3/national-parks-explorer.git
cd national-parks-explorer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
NPS_API_KEY=your_nps_api_key
ORS_API_KEY=your_openrouteservice_api_key
```

API keys should **not** be committed to GitHub.

Run the Python preprocessing scripts to generate the processed datasets.

The resulting CSV files can then be imported into the Power BI report.

## Limitations

There are several limitations to the analysis:

* Driving routes are not available for every remote national park.
* Coordinates in the National Parks dataset are not always located near a road, so routing may fail even when a park is accessible by road.
* Straight-line distance does not represent actual travel difficulty.
* Airport proximity does not necessarily mean that an airport provides commercial passenger service directly to a park.
* National Park Service visitation figures can involve estimates, particularly for remote parks without entrance stations.
* Weather and seasonal accessibility are not incorporated into the driving analysis.

## Future Improvements

Potential extensions include:

* Incorporating flight routes and travel times
* filling in more driving time data 
* Adding seasonal accessibility
* Comparing park visitation with population centers
* Adding accommodation availability around parks
* Building an interactive web version of the dashboard

## Author

**Thijs De Bock**

