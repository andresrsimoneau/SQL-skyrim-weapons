import pandas as pd 
import sqlite3

weapons = pd.read_csv('Skyrim_Weapons.csv')
weapons_data = sqlite3.connect('skyrim.db')
weapons.to_sql("weapons", weapons_data, if_exists="replace", index=False)
