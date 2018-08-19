#!/usr/bin/env python3
#Reference are below
from crontab import CronTab
    
#initialise cron job with pi user
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job to run DataLog file
job  = cron.new(command='/home/pi/A1/DataLog.py')

#set job to run every 1 minute
job.minute.every(1)
cron.write()

#The code used above was taken from the 05_cron.py file from the Week 3 Code Archive. 