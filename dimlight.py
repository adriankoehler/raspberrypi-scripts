#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster


import time
import os
import sys
import random

j2=0.0
STEP = 1
range2 = 10
DELAY = 0.1
r = 0.60 #0.95
g = 0.50 #0.85
b = 0.30 #0.65

cmd = "echo 18=0.90 > /dev/pi-blaster; echo 23=0.80 > /dev/pi-blaster; echo 24=0.60 > /dev/pi-blaster"
#cmd = "echo 18=0 > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
os.system(cmd)

def pwm(pin, angle):
	if pin == 1:
		pin = 18
	elif pin == 2:
		pin = 23
	elif pin == 3:
		pin = 24
	print "piblaster: pin[" + str(pin) + "]int[" + str(angle) + "]delay[" + str(DELAY) + "]"
	cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/pi-blaster"
	os.system(cmd)
	time.sleep(DELAY)

#r -> +-0.5
while True:
  for h in range(1, 3, 1):
    for j in range(0, range2, STEP):
            j2=float(j)/100.00
            if h == 1:
                pwm(h,(j2+r))
            elif h == 2:
                pwm(h,(j2+g))
            elif h == 3:
                pwm(h,(j2+b))
    for j in range(range2, 0, (STEP*-1)):
            j2=float(j)/100.00
            if h == 1:
                pwm(h,(j2+r))
            elif h == 2:
                pwm(h,(j2+g))
            elif h == 3:
                pwm(h,(j2+b))
    DELAY=(random.randint(1,3))/20.0
            
			
