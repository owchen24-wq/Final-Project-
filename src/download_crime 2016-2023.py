# downloads the csv via requests, double check if inside requirements

import requests
import pandas as pd
URL = (
    "https://data.wprdc.org/datastore/dump/044f2016-1dfd-4ab0-bc1e-065da05fca2e"


)
OUT = "data/raw/neighborhood_crime_2016_2023.csv"


#downloaded first file
a = requests.get(URL, timeout=60)
a.raise_for_status()
with open(OUT, "wb") as f:
    f.write(a.content)



df = pd.read_csv(OUT)
print(df.shape)
print(df.columns.tolist())
print(df.head())