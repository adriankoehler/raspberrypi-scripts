#!/usr/bin/env python

#übergeben 2 parameter-> alte und neue farbe->fade zu neuer farbe

import time
import os
import sys

j2=0.0
STEP = 1
DELAY = float(sys.argv[1])
farbeStart = str(sys.argv[2])
farbeEnd = str(sys.argv[3])
r = 0.0
g = 0.0
b = 0.0

def pwm(r, g, b):
	print "switchFade: r[" + str(r) + "]g[" + str(g) + "]b[" + str(b)
	cmd = "echo " + str(18) + "=" + str(r) + " > /dev/pi-blaster;" + "echo " + str(23) + "=" + str(r) + " > /dev/pi-blaster;" + "echo " + str(24) + "=" + str(b) + " > /dev/pi-blaster;"
	os.system(cmd)
	time.sleep(DELAY)

colors = {'white': (1.0, 1.0, 1.0), 'red': (1.0, 0.0, 0.0), 'green': (0.0, 1.0, 0.0), 'blue': (0.0, 1.0, 0.0), 'cyan': (0.0, 1.0, 1.0)}
(r, g, b) = colors.get(key, (0.0, 0.0, 0.0))
