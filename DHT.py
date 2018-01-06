import Adafruit_DHT as dht
import time
import os
import sys

cmd = "gpio write 6 1"
os.system(cmd)
h,t = dht.read_retry(dht.DHT22, 4)
print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)
time.sleep(0.05)
cmd = "gpio write 6 0"
os.system(cmd)