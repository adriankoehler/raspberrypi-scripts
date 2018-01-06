#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster
#time.strftime(%M)
#blau reduzieren; sunset abfrage

import time
import os
import sys

datetime = time.localtime(time.time())

j2=0.0
STEP = 1
range2 = 100
DELAY = 30


#if len(sys.argv[1]) > 1:
#    timeSUNSET = int(sys.argv[1])
#else:
timeSUNSET = 21
#if len(sys.argv[2]) > 1:
#    timeNIGHT = int(sys.argv[2])
#else:
timeNIGHT = 23
#night+4 = 3uhr -> r-

r = 1.0
g = 1.0
b = 1.0

def rgb(r,g,b):
	print "time: " + str(datetime.tm_hour) + "." + str(datetime.tm_min) + " rgb: R[" + str(r) + "] G[" + str(g) + "] B[" + str(b) + "]"
	cmd = "echo 18=" + str(r) + " > /dev/pi-blaster; echo 23=" + str(g) + " > /dev/pi-blaster; echo 24=" + str(b) + " > /dev/pi-blaster"
	os.system(cmd)

print "sunset: " + str(timeSUNSET) + " night:" + str(timeNIGHT)

if int(datetime.tm_hour)>=8 and int(datetime.tm_hour)<=timeSUNSET:
    rgb(1,1,1)
elif int(datetime.tm_hour)>=timeSUNSET and int(datetime.tm_hour)<=timeNIGHT:
    rgb(0,1,1)
else:
    rgb(0,0,1)

def pwm(pin, angle):
	print "piblaster: pin[" + str(pin) + "]int[" + str(angle) + "]"
	cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/pi-blaster"
	os.system(cmd)
	time.sleep(DELAY)

while True:
    datetime = time.localtime(time.time())
    if datetime.tm_hour == timeSUNSET:
        r = 1-(datetime.tm_min*1.667 / 100)
        rgb(r,1,1)
    elif datetime.tm_hour == timeNIGHT:
        g = 1-(datetime.tm_min*1.667 / 100)
        rgb(0,g,1)
    elif datetime.tm_hour == timeNIGHT + 4:
        b = 1.5-(float(datetime.tm_min*1.667 / 100))
        rgb(0,0,b)
    else: 
        print  "time: " + str(datetime.tm_hour) + "." + str(datetime.tm_min) + " //waiting"
    time.sleep(DELAY)
			