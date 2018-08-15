import sqlite3 as lite
import sys
connection = lite.connect('sHat.db')
with connection:
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME,temp NUMBERIC, humidity NUMERIC)")
    
