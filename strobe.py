#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import time
from opc import Client

numLEDs = 47
client = Client('192.168.1.73:7890')

black = [ (0,0,0,0) ] * numLEDs
white = [ (255,0,0,0) ] * numLEDs

while True:
    client.put_pixels(white)
    time.sleep(3.05)
    client.put_pixels(black)
    time.sleep(3.05)
