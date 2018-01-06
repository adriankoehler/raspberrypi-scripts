#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster


import time
import os
import sys

j2=0.0
STEP = 1
DELAY = float(sys.argv[1])

cmd = "echo 18=0 > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
os.system(cmd)

def pwm(pin, angle):
	if pin == 1:
		pin = 18
	elif pin == 2:
		pin = 23
	elif pin == 3:
		pin = 24
	else:
		print 'such error much wow'
		
	print "piblaster: pin[" + str(pin) + "]int[" + str(angle) + "]"
	cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/pi-blaster"
	os.system(cmd)
	time.sleep(DELAY)

	#0,10,1 ->> dann durch 10 // no float
while True:
    for i in range(1, 4):
        for j in range(0, 100, STEP):
            j2=float(j)/100.00
            print "j: "+ str(j) +" / j2: " + str(j2)
            pwm(i,j2)   
    for i in range(1, 4):
        for j in range(100, 0, (STEP*-1)):
            j2=float(j)/100.00
            print "j: "+ str(j) +" / j2: " + str(j2)
            pwm(i,j2)
            

			