#File created to experiment with the way python interacts with database

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM concerts WHERE Band='Anyma'")
rows = cursor.fetchall()
print(rows)