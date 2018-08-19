#!/usr/bin/env python3 
#see bottom of the code for references
from datetime import datetime 
import sqlite3
from sense_hat import SenseHat
import requests
import json
import os
dbname='/home/pi/A1/sHat.db'

def getUserTemp():
    file = open('/home/pi/A1/temperature.txt', 'r')
    user_temp = file.read(2)
    return(user_temp)

# get data from SenseHat sensor (temperature and humidity)
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    user_temp = getUserTemp()
    logData(temp,humidity)
    displayData(temp,humidity)
    checkTemp(temp, user_temp)
    
# display database data
def displayData(temp,humidity):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()    
    sense = SenseHat()
    #for debugging purposes, run this code to ensure that code is working. 
    sense.show_message('The temperature and humidity are: {}, {} '.format(round(temp,1), round(humidity,1)), scroll_speed= 0.07)

# log sensor data on database into temperature and humidity columns
def logData (temp,humidity):	
    temp = round(temp,1)
    humidity = round(humidity,1)
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now', 'localtime'), (?), (?))",(temp, humidity)) 
                                                                                
    conn.commit()
    conn.close()
    
#check if temperature if below set limit, if so send pushbullet notification
def checkTemp(temp, user_temp):
    #check if temperature parsed from database is below limit, if true send notification
    if temp < int(user_temp):
         send_notification_via_pushbullet("Weather Notification", "It is below " + user_temp +  "C make sure you bring a sweater with you!") 

#pushbullet script for sending weather updates
def send_notification_via_pushbullet(title, body):
    ACCESS_TOKEN="o.KkhwX2awlqqPi6KUdeCtm5dL3SeBMwfV"

    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error: Something wrong')
    else:
        print('Notification was sent!')
   
#main function
def main():
    getSenseHatData()

# Execute program 
main()

#REFERENCE: Parts of this code , such as methods were inspired by demo_prac.py code taken from 
#the TL4 Code Archive. Localtime issue on database  was fixed using the ‘ ‘localtime’ 
#code found on this website: https://stackoverflow.com/questions/381371/sqlite-current-timestamp-is-in-gmt-not-the-timezone-of-the-machine 
    #PUSHBULLET REFERENCE: Parts of this code were inspired by 06_pycurlBullet.py code taken from  the TL4 Code Archive. 