import pandas as pd 
import sqlite3

weapons = pd.read_csv('Skyrim_Weapons.csv') #pd.read_csv() function is used to read data from CSV files into a Pandas DataFrame
weapons_data = sqlite3.connect('skyrim.db') #connecting to SQlite database with .db file
weapons.to_sql("weapons", weapons_data, if_exists="replace", index=False) #putting panda dataframe into SQL
weapons_data.close()
