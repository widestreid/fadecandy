#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, math
from random import randrange

numLEDs = 93
client = opc.Client('192.168.1.73:7890')

while True:
	for i in range(numLEDs):
		a = randrange(0,80)
		b = 255 * math.cos(time.clock()/1)
		b = int(b)
		b = abs(b)
		pixels = [ (0,0,0,0) ] * numLEDs
		pixels[a] = (0, 0, 255, 25)
		pixels[a+1] = (0, 0, 255, 25)
		pixels[a+2] = (0, 0, 255, 25)
		pixels[a+3] = (0, 0, 255, 25)
		pixels[a+4] = (0, 0, 255, 25)

		client.put_pixels(pixels)
		time.sleep(1.005)
