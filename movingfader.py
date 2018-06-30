#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, math, sys
from random import randrange, uniform

numLEDs = 80
Longrange = 256
per = 8
count=0
client = opc.Client('192.168.1.73:7890')
r=5

while True:
    for i in range(numLEDs):

        bri = 255*(math.sin(time.clock()))
        bri = int(bri)
        bri = abs(bri)+1;
        #print(bri)
        pixels = [(0, 0, 0, 50)] * numLEDs
        pixels[r] =  (1*bri,1,1,0*bri)
        pixels[r+1] =  (1*bri,1,1,0*bri)
        pixels[r+2] =  (1*bri,1,1,0*bri)
        pixels[r+3] =  (1*bri,1,1,0*bri)

        client.put_pixels(pixels)
        print("")
        time.sleep(0.001)
        print(r)
        print (bri)

        if bri<5:
            r = randrange(0,60)
            print("NEW")
        else:
            print("existing")
""""
        if bri<10:
                print("change")
                count = count+1
                per = (randrange(3, 10))
                print(per)
        else:
            print("")
        #if count % 2 == 0:
        #else:
"""

#print(time.time())