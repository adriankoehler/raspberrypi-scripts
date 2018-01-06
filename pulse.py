#!/usr/bin/env python

#echo 3=120 > /dev/servoblaster
#echo 24=1 > /dev/pi-blaster


import time
import os
import sys

j2=0.0
farbe = sys.argv[1]
breath = sys.argv[2]
print breath
STEP = 1

if breath == "1":
    STEP2 = 2
    print "breath"
else:
    STEP2 = 1
    print "normal"

DELAY = 0.02
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
        for j in range(0, 100, STEP2):
            j2=float(j)/100.00
            if farbe == "weiss":
                valR=j2
                valG=j2
                valB=j2
            elif farbe == "rot":
                valR=j2
                valG=0
                valB=0
            elif farbe == "gruen":
                valR=0
                valG=j2
                valB=0
            elif farbe == "blau":
                valR=0
                valG=0
                valB=j2
            elif farbe == "gelb":
                valR=j2
                valG=j2
                valB=0
            elif farbe == "cyan":
                valR=0
                valG=j2
                valB=j2
            elif farbe == "pink":
                valR=j2
                valG=0
                valB=j2
            elif farbe == "orange":
                valR=j2
                valG=j2/2.0
                valB=0
            elif farbe == "tuerkis":
                valR=0
                valG=j2
                valB=j2/2.0
            elif farbe == "lila":
                valR=j2/2.0
                valG=0
                valB=j2
            else:
                print "error, arg existiert nicht"
                sys.exit(0)
            
            pwm(valR, valG, valB)
            
            if breath == "1" and j==0:
                time.sleep(0.05)
                print "SLEEP"
            
        
        for j in range(100, 0, (STEP*-1)):
            j2=float(j)/100.00
            if farbe == "weiss":
                valR=j2
                valG=j2
                valB=j2
            elif farbe == "rot":
                valR=j2
                valG=0
                valB=0
            elif farbe == "gruen":
                valR=0
                valG=j2
                valB=0
            elif farbe == "blau":
                valR=0
                valG=0
                valB=j2
            elif farbe == "gelb":
                valR=j2
                valG=j2
                valB=0
            elif farbe == "cyan":
                valR=0
                valG=j2
                valB=j2
            elif farbe == "pink":
                valR=j2
                valG=0
                valB=j2
            elif farbe == "orange":
                valR=j2
                valG=j2/2.0
                valB=0
            elif farbe == "tuerkis":
                valR=0
                valG=j2
                valB=j2/2.0
            elif farbe == "lila":
                valR=j2/2.0
                valG=0
                valB=j2
            
            pwm(valR, valG, valB)
            
