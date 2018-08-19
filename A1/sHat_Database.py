#REFERENCE: This code was from the TL4 Code Archive, under 01_create_db.py
#creates a table with timestap,Datetime,temp and humidity
import sqlite3 as lite
import sys
connection = lite.connect('sHat.db')
with connection:
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME,temp NUMBERIC, humidity NUMERIC)")
    
