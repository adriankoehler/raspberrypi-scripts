# -*- coding: utf-8 -*-
#!/usr/bin/env python

import Adafruit_DHT as dht
import time
import os
import sys

#cmd = "gpio write 6 1"
#os.system(cmd)
h,t = dht.read_retry(dht.DHT22, 4)
print '{1:0.1f}%'.format(t,h)
#cmd = "gpio write 6 0"
#os.system(cmd)