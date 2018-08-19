#!/usr/bin/env python3
#Please see the bottom of the code for references
import bluetooth
import os
import time
from sense_hat import SenseHat

# Search for device based on device's name
def search_for_phone(user_name, device_name):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {} Searching for {}'s device...".format(dt,user_name))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()
        #loop through mac_address in order to match with inputed device value
        for mac_address in nearby_devices:
            if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                device_address = mac_address
                break
        #once device is discovered display message to pi and temperature
        if device_address is not None:
            sense = SenseHat()
            sense.show_message("Found " + user_name + "'s device", scroll_speed=0.04)
            temp = round(sense.get_temperature(), 1)
            sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
        else:
            print("Could not find target device nearby...")

# Main function
def main():
    user_name = input("Enter your name: ")
    device_name = input("Enter the name of your phone: ")
    search_for_phone(user_name, device_name)

#Execute program
main()

#REFERENCE: Parts of this code , such as methods were inspired by findmyphone_prac.py code taken from  the TL4 Code Archive.