#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, math, sys
from random import randrange, uniform

numLEDs = 80
Longrange = 256
per = 8
count=0

client = opc.Client('192.168.1.73:7890')


while True:
    for i in range(numLEDs):
        bri = 40*(math.sin(time.clock()))
        bri = int(bri)
        bri = abs(bri)+1;
        anna = 255 * math.cos(time.clock()/bri);
        anna = int(anna)
        anna = abs(anna)
        print(bri)
        print(anna)
        pixels = [ (1*bri,1*anna,0*anna,0*bri) ] * numLEDs
        client.put_pixels(pixels)
        print("")
        time.sleep(0.001)


        if bri<10:
                print("change")
                count = count+1
                per = (randrange(3, 10))
                print(per)
        else:
            print("")
        #if count % 2 == 0:
        #else:


print(time.time())