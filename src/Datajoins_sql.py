import sqlite3
import pandas as pd


pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)   # show the full CREATE TABLE text

con = sqlite3.connect("project.db")

### preforms checks by lefjoining and seeihng any lost tables
'''
query = """
SELECT crime_16_22.INCIDENTNEIGHBORHOOD,    population.Neighborhood


FROM crime_16_22


LEFT JOIN population ON crime_16_22.INCIDENTNEIGHBORHOOD = population.Neighborhood
where population.Neighborhood IS NULL

Group by INCIDENTNEIGHBORHOOD,    population.Neighborhood



"""

query1 = """
SELECT p.Neighborhood AS population_name
FROM population AS p
LEFT JOIN crime_16_22 AS c
       ON p.Neighborhood = c.INCIDENTNEIGHBORHOOD
WHERE c.INCIDENTNEIGHBORHOOD IS NULL
GROUP BY p.Neighborhood
"""
'''


### querry pulling and grouping to find total incidents and total crimes along with the populations
query2 = """
SELECT p.Neighborhood                AS neighborhood,

       p."2020_Total_Population"     AS pop_2020,
       
       COUNT(c.year)                 AS total_incidents,
       
       COUNT(CASE WHEN c.year = 2016 THEN 1 END) AS y2016,
       COUNT(CASE WHEN c.year = 2017 THEN 1 END) AS y2017,
       COUNT(CASE WHEN c.year = 2018 THEN 1 END) AS y2018,
       COUNT(CASE WHEN c.year = 2019 THEN 1 END) AS y2019,
       COUNT(CASE WHEN c.year = 2020 THEN 1 END) AS y2020,
       COUNT(CASE WHEN c.year = 2021 THEN 1 END) AS y2021,
       COUNT(CASE WHEN c.year = 2022 THEN 1 END) AS y2022
FROM population AS p
LEFT JOIN crime_16_22 AS c
       ON c.INCIDENTNEIGHBORHOOD = p.Neighborhood
GROUP BY p.Neighborhood, p."2020_Total_Population"
"""



result1 =  pd.read_sql(query2, con)


print(  result1 )



con.close()