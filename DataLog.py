#!/usr/bin/env python3 
from datetime import datetime 
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/A1/sHat.db'
#sampleFreq = 1 # time in seconds

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    time = datetime.now().strftime("%H:%M")
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
	
#    if temp is not None:
#        temp = round(temp, 1)
    logData (temp,humidity)
        
        

# log sensor data on database
def logData (temp,humidity):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now', 'localtime'), (?), (?))",(temp, humidity)) 
                                                                                
    conn.commit()
    conn.close()

    displayData(temp)

# display database data
def displayData(temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()

    sense = SenseHat()
    # for debugging purposes, run this code to ensure that code is working. 
#    sense.show_message('The temperature and humidity are: {} '.format(temp), scroll_speed= 0.07)

# main function
def main():
#    for i in range (0,3):
    getSenseHatData()
#        time.sleep(sampleFreq)
    

# Execute program 
main()
