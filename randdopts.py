#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, math, threading
from random import randrange

from threading import Thread

numLEDs = 96
client = opc.Client('192.168.1.73:7890')
pixels = [(0, 0, 0, 0)] * numLEDs


def rand():
	a = randrange(0, 92)
	#print(a)
	return a

def pixelblink1(a):
	for i in range(1, 200, 1):
		#print(b)
		pixels[a] = (0, 0, 0, 1 * i)
		pixels[a+1] = (0, 0, 0, 1 * i)
		pixels[a+2] = (0, 0, 0, 1 * i)
		pixels[a+3] = (0, 0, 0, 1 * i)
		pixels[a+4] = (0, 0, 0, 1 * i)
		time.sleep(.01)
		client.put_pixels(pixels)

	for i in range(200, 1, -1):
		pixels[a] = (0, 0, 0, 1 * i)
		pixels[a+1] = (0, 0, 0, 1 * i)
		pixels[a+2] = (0, 0, 0, 1 * i)
		pixels[a+3] = (0, 0, 0, 1 * i)
		pixels[a+4] = (0, 0, 0, 1 * i)
		time.sleep(.01)
		client.put_pixels(pixels)

def pixelblink2(a):
	for i in range(1, 200, 1):
		pixels[a] = (0, 0, 0, 1 * i)
		time.sleep(.01)
		client.put_pixels(pixels)

	for i in range(200, 1, -1):
		pixels[a] = (0, 0, 0, 1 * i)
		time.sleep(.01)
		client.put_pixels(pixels)


while True:
	for i in range(numLEDs):
		b = 255 * math.cos(time.clock()/1)
		b = int(b)
		b = abs(b)
		a=rand()
		Thread(pixelblink1(a)).start()
		a=rand()
		Thread(pixelblink1(a)).start()
		print(pixels)
		time.sleep(.1)
		a=rand()
		b=rand()
		time.sleep(.1)

		client.put_pixels(pixels)




