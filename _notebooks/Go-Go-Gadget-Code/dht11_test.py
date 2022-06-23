# Author: Christina Kampel
# Based on code from "Temperature & Humidity Sensor (DHT11)" section here: https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md

import time
from seeed_dht import DHT

dht11 = DHT("11", 4) # Type, GPIO pin for signal cable

while True:
    humi, temp = dht11.read()
    print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(dht11.dht_type, humi, temp))
    # print(f"Temp: {temp}")
    time.sleep(1)