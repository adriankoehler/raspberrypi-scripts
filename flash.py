#!/usr/bin/env python

import time
import os
import sys

j2=0.0
STEP = 1

DELAY = 0.01
valR=0.0
valG=0.0
valB=0.0

cmd = "echo 18=0 > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
os.system(cmd)

def pwm(valR, valG, valB):	
	print "piblaster: valR[" + str(valR) + "]valG[" + str(valG) + "]valB[" + str(valB)
	cmd = "echo 18=" + str(valR) + " > /dev/pi-blaster;" + "echo 23=" + str(valG) + " > /dev/pi-blaster;" + "echo 24=" + str(valB) + " > /dev/pi-blaster;"
	os.system(cmd)
	time.sleep(DELAY)

while True:
    for i in range(1, 7, 1):
        for j in range(0, 100, STEP):
            j2=float(j)/100.00
            if i == 1:
                valR=j2
                valG=0
                valB=0
            #elif i == 2:
                #valR=j2
                #valG=j2/2.0
                #valB=0
            elif i == 2:
                valR=j2
                valG=j2
                valB=0
            elif i == 3:
                valR=0
                valG=j2
                valB=0
            elif i == 4:
                valR=0
                valG=j2
                valB=j2
            #elif i == 6:
                #valR=0
                #valG=j2
                #valB=j2/2.0
            elif i == 5:
                valR=0
                valG=0
                valB=j2
            #elif i == 8:
                #valR=j2/2.0
                #valG=0
                #valB=j2
            elif i == 6:
                valR=j2
                valG=0
                valB=j2
            pwm(valR, valG, valB)
            
        for j in range(100, 0, (STEP*-1)):
            j2=float(j)/100.00
            if i == 1:
                valR=j2
                valG=0
                valB=0
            elif i == 2:
                valR=j2
                valG=j2
                valB=0
            elif i == 3:
                valR=0
                valG=j2
                valB=0
            elif i == 4:
                valR=0
                valG=j2
                valB=j2
            elif i == 5:
                valR=0
                valG=0
                valB=j2
            elif i == 6:
                valR=j2
                valG=0
                valB=j2
            pwm(valR, valG, valB)
            
