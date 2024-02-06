import sqlite3
import datetime


conn = sqlite3.connect('database.db',
                        detect_types=sqlite3.PARSE_DECLTYPES |
                        sqlite3.PARSE_COLNAMES)
print("Connected to database successfully")

conn.execute('CREATE TABLE pacients (name TEXT, number TEXT, date TIMESTAMP, city TEXT)')
print("Created table successfully!")

conn.close()

