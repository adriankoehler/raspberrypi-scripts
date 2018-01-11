#!/usr/bin/env python
# coding: utf8

#uebergeben 2 parameter-> alte und neue farbe->fade zu neuer farbe
#moegliche parameterwerte white,red,green,blue,cyan

import time
import os
import sys

STEPS = 100
DELAY = float(sys.argv[1])
PINred = 18
PINgreen = 23
PINblue = 24
farbeStart = str(sys.argv[2])
farbeEnd = str(sys.argv[3])
Rs,Gs,Bs = (0.0, 0.0, 0.0)
Re,Ge,Be = (0.0, 0.0, 0.0)

def pwm(r, g, b):
	print "switchFade: r[" + str(r) + "]g[" + str(g) + "]b[" + str(b) + "]"
	#cmd = "echo " + str(PINred) + "=" + str(r) + " > /dev/pi-blaster;" + "echo " + str(PINgreen) + "=" + str(r) + " > /dev/pi-blaster;" + "echo " + str(PINblue) + "=" + str(b) + " > /dev/pi-blaster;"
	cmd = "echo " + str(PINred) + "=" + str(r) + " _ " + str(PINgreen) + "=" + str(g) + " _ " + str(PINblue) + "=" + str(b)
	os.system(cmd)
	time.sleep(DELAY)

#übergebene parameter auslesen und in r,g,b variablen abspeichern/umwandeln
colors = {'white': (1.0, 1.0, 1.0), 'red': (1.0, 0.0, 0.0), 'green': (0.0, 1.0, 0.0), 'blue': (0.0, 1.0, 0.0), 'cyan': (0.0, 1.0, 1.0)}
(Rs, Gs, Bs) = colors.get(farbeStart, (0.0, 0.0, 0.0))
#TODO: add colors; copy into RGBe assignment
colors = {'white': (1.0, 1.0, 1.0), 'red': (1.0, 0.0, 0.0), 'green': (0.0, 1.0, 0.0), 'blue': (0.0, 1.0, 0.0), 'cyan': (0.0, 1.0, 1.0)}
(Re, Ge, Be) = colors.get(farbeEnd, (0.0, 0.0, 0.0))

diffrenceR = Rs - Re
diffrenceG = Gs - Ge
diffrenceB = Bs - Be
currentR = Rs - diffrenceR/STEPS
currentG = Gs - diffrenceG/STEPS
currentB = Bs - diffrenceB/STEPS

print "RGBs: r[" + str(Rs) + "]g[" + str(Gs) + "]b[" + str(Bs) + "]"
print "RGBe: r[" + str(Re) + "]g[" + str(Ge) + "]b[" + str(Be) + "]"
print "current: r[" + str(currentR) + "]g[" + str(currentG) + "]b[" + str(currentB) + "]"

pwm(currentR, currentG, currentB)
#eins von beiden immer gleich
while (currentR!=Re and currentG!=Ge and currentB!=Be) :
	print "test?"
	currentR -= diffrenceR/STEPS
	currentG -= diffrenceG/STEPS
	currentB -= diffrenceB/STEPS
	pwm(currentR, currentG, currentB)
