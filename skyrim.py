import pandas as pd 
import sqlite3

weapons = pd.read_csv('Skyrim_Weapons.csv') #pd.read_csv() function is used to read data from CSV files into a Pandas DataFrame
weapons_data = sqlite3.connect('skyrim.db') #connecting to SQlite database with .db file
weapons.to_sql("weaponsdata" , weapons_data, if_exists="replace", index=False) #putting panda dataframe into SQL
                  #table     #SQlite connection
weapons_sql = weapons_data.cursor() # allows us to execute SQL commands on the database

BEST_DAMAGE_AND_CLASS = """
SELECT damage, type
FROM weaponsdata
WHERE damage > 20
ORDER BY damage DESC
"""

weapons_sql.execute(BEST_DAMAGE_AND_CLASS)
joe_biden = weapons_sql.fetchall()
for damage, type in joe_biden:
        print(f"{damage} damage | {type} CLASS")