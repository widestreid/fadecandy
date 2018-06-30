#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 100
client = opc.Client('192.168.1.73:7890')

black = [ (0,0,0,0) ] * numLEDs
white = [ (255,255,25,25) ] * numLEDs


# Fade to white
client.put_pixels(black)
client.put_pixels(white)
time.sleep(.5)
client.put_pixels(white)
