user_temp = input("Please input threshold for weather notification: ")
file = open('/home/pi/A1/temperature.txt', 'w')
file.write(user_temp)
file.close