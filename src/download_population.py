# downloads the csv via requests, double check if inside requirements

import requests
import pandas as pd
URL = (
    "https://data.wprdc.org/dataset/95af9f2c-61c8-446b-ae72-852e195684f3"
    "/resource/a8414ed5-c50f-417e-bb67-82b734660da6/download/"
    "preliminarycitypittsburghneighborhood_pl94171summary-2.csv"
)
OUT = "data/raw/neighborhood_pop_2020.csv"


#downloaded first file
a = requests.get(URL, timeout=60)
a.raise_for_status()
with open(OUT, "wb") as f:
    f.write(a.content)



df = pd.read_csv(OUT)
print(df.shape)
print(df.columns.tolist())
print(df.head())