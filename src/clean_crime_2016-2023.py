from calendar import error

import pandas as pd
import sqlite3
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_colwidth", 100)

# read the file
df = pd.read_csv("data/raw/neighborhood_crime_2016_2023.csv")









# dates: convert, then keep 2016-2022 (2023 is partial, ends early Nov)
df["INCIDENTTIME"] = pd.to_datetime(df["INCIDENTTIME"], errors="coerce")
df = df.dropna(subset=["INCIDENTTIME"])
df["year"] = df["INCIDENTTIME"].dt.year
df = df[df["year"].between(2016, 2022)]#inclusive

print("rows in 2016-2022:", len(df))

#manual checks
''''
# shape, duplicates, missing values
print("shape:", df.shape)
print("duplicate rows:", df.drop(columns=["_id", "PK"]).duplicated().sum())
print("duplicate CCR:", df["CCR"].duplicated().sum())
print(df.isna().sum())

# look at all offense types
print("distinct offense strings:", df["OFFENSES"].nunique())
print(df["OFFENSES"].value_counts().head(60))
'''


# keep only the part violent crimes
# part I violent = murder/nonnegligent manslaughter, rape, robbery, aggravated assault etc
# Source:FBI UCR offense definitions https://ucr.fbi.gov/crime-in-the-u.s/2014/crime-in-the-u.s.-2014/resource-pages/offense-definitions.pdf
# Statute numbers below are my own mapping to the PA Crimes Code, note toe self to verify
#   3701 robbery, 2702 aggravated assault, 2501-2503 homicide.
# incecent  is Part I too, but those rows have no neighborhood, so they drop out anyway.

# groups then finds where start
pattern = r"(?:^|/ )(?:3701|2702|2501|2502|2503)"
violent = df[df["OFFENSES"].str.contains(pattern, na=False, regex=True)].copy()

# 6. drop rows with no neighborhood (reported by police zone only)
before = len(violent)
violent = violent.dropna(subset=["INCIDENTNEIGHBORHOOD"])
print("dropped for no neighborhood:", before - len(violent))

# 7. checks
print("violent incidents kept:", len(violent))
print(violent["year"].value_counts().sort_index())
print(violent["OFFENSES"].value_counts().head(20))


clean = violent[["INCIDENTNEIGHBORHOOD", "year","OFFENSES"]].copy()

clean.to_csv("data/clean/crime_2016-2022.csv", index=False)
con = sqlite3.connect("project.db")
clean.to_sql("crime_16_22", con, if_exists="replace", index=False)
con.close()

print("saved", clean.shape)