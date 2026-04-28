#File created to experiment with the way python interacts with database

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#query al data
cursor.execute('SELECT * FROM concerts WHERE Venue="Climate Pledge Arena"')
rows = cursor.fetchall()
print(rows)

#query certain columns
cursor.execute('SELECT Band, Venue FROM concerts')
rows = cursor.fetchall()
print(rows)

#Insert new rows
new_rows = [("Hozier", "August 20th", "Gorge"),
            ("Tame Impala", "May 9th", "Lumen Field")]

cursor.executemany("INSERT INTO concerts VALUES (?,?,?)", new_rows)
connection.commit()