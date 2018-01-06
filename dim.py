#!/usr/bin/env python

import time
import os
import sys

STEP = 1
range2 = 5
DELAY = float(sys.argv[1])
r = 0.0

cmd = "echo 18=0 > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
os.system(cmd)
cmd = "echo '" + (time.strftime("%d.%m.%Y %H:%M:%S")) + ": dim.py' >> /var/www/data/startup.log"
os.system(cmd)

def pwm(r, g):
	print "piblaster: pin[18-23] int[" + str(r) + "-" + str(g) + "] delay[" + str(DELAY) + "]"
	cmd = "echo 18=" + str(r) + " > /dev/pi-blaster;" + "echo 23=" + str(g) + " > /dev/pi-blaster;"
	os.system(cmd)
	time.sleep(DELAY)

while (r<0.04):
    for j in range(0, range2, STEP):
      r=float(j)/100.00
      g=float(j)/500.00
      pwm(r, g)
      DELAY = DELAY / 1.2
      #ease in effekt



