#!/usr/bin/env python

import time
import os

DELAY = 1

cmd = "cd /home/pi/wiringPi;"
os.system(cmd)

for i in range(1, 17):
	print "pin[" + str(i) + "]int[1]"
	cmd = "gpio -g write " + str(i) + " 1"
	os.system(cmd)
	time.sleep(DELAY)

for i in range(21, 30):
	print "pin[" + str(i) + "]int[1]"
	cmd = "gpio -g write " + str(i) + " 1"
	os.system(cmd)
	time.sleep(DELAY)

for i in range(1, 17):
	print "pin[" + str(i) + "]int[0]"
	cmd = "gpio -g write " + str(i) + " 0"
	os.system(cmd)
	time.sleep(DELAY)

for i in range(21, 30):
	print "pin[" + str(i) + "]int[0]"
	cmd = "gpio -g write " + str(i) + " 0"
	os.system(cmd)
	time.sleep(DELAY)

