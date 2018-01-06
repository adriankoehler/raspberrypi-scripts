#!/usr/bin/env python
import os

cmd = "sudo killall python"
os.system(cmd)
print cmd

cmd = "echo "+ "18=0" + " > /dev/pi-blaster; echo "+ "23=0" + " > /dev/pi-blaster; echo "+ "24=0" + " > /dev/pi-blaster"
os.system(cmd)
print cmd
