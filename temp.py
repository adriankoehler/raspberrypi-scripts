# -*- coding: utf-8 -*-
#!/usr/bin/env python

import Adafruit_DHT as dht
import time
import os
import sys

#cmd = "gpio write 6 1"
#os.system(cmd)
h,t = dht.read_retry(dht.DHT22, 4)
print '{0:0.1f}°C'.format(t)
#cmd = "gpio write 6 0"
#os.system(cmd)