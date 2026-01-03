import pandas as pd 
import sqlite3

weapons = pd.read_csv('Skyrim_Weapons.csv') #pd.read_csv() function is used to read data from CSV files into a Pandas DataFrame
weapons_data = sqlite3.connect('skyrim.db') #connecting to SQlite database with .db file
weapons.to_sql("weaponsdata" , weapons_data, if_exists="replace", index=False) #putting panda dataframe into SQL
                  #table     #SQlite connection
weapons_sql = weapons_data.cursor() # allows us to execute SQL commands on the database

weapons_sql.execute("""
SELECT AVG(damage)
FROM weaponsdata
WHERE type = 'Dagger'
""")
dagger_damage = weapons_sql.fetchall()

weapons_sql.execute("""
SELECT AVG(damage)
FROM weaponsdata
WHERE type = 'Battleaxe'
""")
battleaxe_damage = weapons_sql.fetchall()

def average_function(query, label): #function to simplify SQL outputs 
	for damage in query:
	    print(f"AVG {damage[0]} DAMAGE | {label}")

average_function(dagger_damage, 'Dagger')
average_function(battleaxe_damage, 'Battleaxe')
