#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster


import time
import os
import sys

j2=0.0
STEP = 1
range2 = 100
DELAY = float(sys.argv[1])
pin = 18

def rgb(r,g,b):
	cmd = "echo 18=" + str(r) + " > /dev/pi-blaster; echo 23=" + str(g) + " > /dev/pi-blaster; echo 24=" + str(b) + " > /dev/pi-blaster"
	os.system(cmd)

if sys.argv[2] == "rot":
	rgb(1,0,0)
elif sys.argv[2] == "gruen":
	rgb(0,1,0)
elif sys.argv[2] == "blau":
	rgb(0,0,1)
if sys.argv[3] == "orange":
	range2 = 50
	pin = 23
elif sys.argv[3] == "tuerkis":
	range2 = 50
	pin = 24
elif sys.argv[3] == "lila":
	range2 = 50
	pin = 18
elif sys.argv[3] == "pink":
	range2 = 100
	if sys.argv[2] == "rot":
		pin = 24
	else:
		pin = 18
elif sys.argv[3] == "gelb":
	range2 = 100
	if sys.argv[2] == "gruen":
		pin = 18
	else:
		pin = 23
elif sys.argv[3] == "cyan":
	range2 = 100
	if sys.argv[2] == "gruen":
		pin = 24
	else:
		pin = 23

def pwm(angle):
	print "piblaster: pin[" + str(pin) + "]int[" + str(angle) + "]"
	cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/pi-blaster"
	os.system(cmd)
	time.sleep(DELAY)

while True:
    for j in range(0, range2, STEP):
            j2=float(j)/100.00
            pwm(j2)
    for j in range(range2, 0, (STEP*-1)):
            j2=float(j)/100.00
            pwm(j2)
            
			