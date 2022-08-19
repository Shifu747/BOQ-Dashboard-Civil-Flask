import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('boqDB.db')

df = pd.read_sql_query("SELECT * FROM boq", cnx)
print(df.head(2))