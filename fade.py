#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster


import time
import os
import sys

j2=0.0
STEP = 1
DELAY = float(sys.argv[1])
try:
	BRIGHTNESS = int(sys.argv[2])
	BRIGHTNESS2 = float(sys.argv[2])
except:
	BRIGHTNESS = 100
	BRIGHTNESS2 = 100.0

cmd = "echo 18=" + str(BRIGHTNESS2/100) + " > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
os.system(cmd)
print str(cmd)

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
    for a in range(0, (BRIGHTNESS), (STEP)):
        j2=float(a)/100.00
        print "gruen hoch: " + str(j2)
        pwm(2,j2)
    for b in range((BRIGHTNESS), 0, (STEP*-1)):
        j2=float(b)/100.00
        print "rot runter: " + str(j2)
        pwm(1,j2)
    for c in range(0, (BRIGHTNESS), (STEP)):
        j2=float(c)/100.00
        print "blau hoch: " + str(j2)
        pwm(3,j2)
    for d in range((BRIGHTNESS), 0, (STEP*-1)):
        j2=float(d)/100.00
        print "gruen runter: " + str(j2)
        pwm(2,j2)
    for e in range(0, (BRIGHTNESS), (STEP)):
        j2=float(e)/100.00
        print "rot hoch: " + str(j2)
        pwm(1,j2)
    for f in range((BRIGHTNESS), 0, (STEP*-1)):
        j2=float(f)/100.00
        print "blau runter: " + str(j2)
        pwm(3,j2)

