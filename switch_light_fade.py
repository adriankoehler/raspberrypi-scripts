#!/usr/bin/env python
# coding: utf8

#uebergeben 3 parameter [delay zw steps, alte und neue farbe] -> fade zu neuer farbe
#moegliche parameterwerte white,red,green,blue,cyan, orange, turqouise, purple, yellow, pink

import time
import os
import sys
import math

STEPS = 20
DELAY = float(sys.argv[1])
PINred = 18
PINgreen = 23
PINblue = 24
farbeStart = str(sys.argv[2])
farbeEnd = str(sys.argv[3])
Rs,Gs,Bs = (0.0, 0.0, 0.0)
Re,Ge,Be = (0.0, 0.0, 0.0)

def pwm(r, g, b):
	#print "switchFade: r[" + str(r) + "]g[" + str(g) + "]b[" + str(b) + "]"
	cmd = "echo " + str(PINred) + "=" + str(r) + " > /dev/pi-blaster;" + "echo " + str(PINgreen) + "=" + str(g) + " > /dev/pi-blaster;" + "echo " + str(PINblue) + "=" + str(b) + " > /dev/pi-blaster;"
	os.system(cmd)
	time.sleep(DELAY)

#übergebene parameter auslesen und in r,g,b variablen abspeichern/umwandeln
colors = {'off': (0.0, 0.0, 0.0), 'white': (1.0, 1.0, 1.0), 'red': (1.0, 0.0, 0.0), 'green': (0.0, 1.0, 0.0), 'blue': (0.0, 0.0, 1.0), 'cyan': (0.0, 1.0, 1.0), 'orange': (1.0, 0.6, 0.25), 'turquoise': (0.0, 1.0, 0.5), 'purple': (0.5, 0.0, 1.0), 'yellow': (1.0, 0.82, 0.47), 'pink': (1.0, 0.0, 1.0)}
(Rs, Gs, Bs) = colors.get(farbeStart, (0.0, 0.0, 0.0))
(Re, Ge, Be) = colors.get(farbeEnd, (0.0, 0.0, 0.0))

diffrenceR, diffrenceG, diffrenceB = (Rs - Re, Gs - Ge, Bs - Be)
currentR,currentG,currentB = (Rs - diffrenceR/STEPS, Gs - diffrenceG/STEPS, Bs - diffrenceB/STEPS)

print "RGBs: r[" + str(Rs) + "]g[" + str(Gs) + "]b[" + str(Bs) + "]"
print "RGBe: r[" + str(Re) + "]g[" + str(Ge) + "]b[" + str(Be) + "]"
print "current: r[" + str(currentR) + "]g[" + str(currentG) + "]b[" + str(currentB) + "]"

pwm(currentR, currentG, currentB)

for i in xrange(1, STEPS-1):
	currentR -= diffrenceR/STEPS
	currentG -= diffrenceG/STEPS
	currentB -= diffrenceB/STEPS
	pwm(currentR, currentG, currentB)

pwm(Re, Ge, Be)
