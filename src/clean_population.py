import pandas as pd
import sqlite3

df = pd.read_csv("data/raw/neighborhood_pop_2020.csv")

# data check
'''
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
df = pd.read_csv("data/raw/neighborhood_pop_2020.csv")


print("shape( rows,colums): ", df.shape)
# 89 not 90 becuz 2 of them are combined
print("missing values per collum ", df.isna().sum())

print("Duplicate rows:", df.duplicated().sum())
print("2020 sum:", df["2020_Total_Population"].sum())


## select only needed ones
'''

#check passed

clean = df[["Neighborhood", "2020_Total_Population"]].copy()

clean.to_csv("data/clean/population.csv", index=False)
con = sqlite3.connect("project.db")
clean.to_sql("population", con, if_exists="replace", index=False)
con.close()

print("saved", clean.shape)