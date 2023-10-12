############################################################## IMPORT BLOCK #####################################################################
from neopixel import NeoPixel
from machine import Pin
import re
import time

#################################################################################################################################################
#Objects:      #from:   https://wokwi.com/projects/375655543217348609

n = 16 # number of pixel in neopixel ring
p = 26 # Pinnumber to controll NeoPixel
neo_p = NeoPixel(Pin(p, Pin.OUT), n) #NeoPixel object neo_p

#################################################################################################################################################
#Functions:

#clear the LEDs
def clear():
    for i in range(n):
        neo_p[i] = (0, 0, 0)
        neo_p.write()


#fade
def fade_in_out(colour, wait):
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            if colour == 'red':
                neo_p[j] = (val, 0, 0)
            elif colour == 'green':
                neo_p[j] = (0, val, 0)
            elif colour == 'blue':
                neo_p[j] = (0, 0, val)
            elif colour == 'purple':
                neo_p[j] = (val, 0, val)
            elif colour == 'yellow':
                neo_p[j] = (val, val, 0)
            elif colour == 'teal':
                neo_p[j] = (0, val, val)
            elif colour == 'white':
                neo_p[j] = (val, val, val)
            neo_p.write()
        time.sleep_ms(wait)


#################################################################################################################################################
# 3.3 - Find koden fra Micropython grundbogen og prøv funktionen til at fade farverne
# i neopixels ringen (MODULE 6 - Control an Addressable RGB LED Str
#################################################################################################################################################

fade_in_out('red', 15)
fade_in_out('green', 10)
fade_in_out('blue', 25)
fade_in_out('purple', 10)
fade_in_out('yellow', 10)
fade_in_out('teal', 10)
fade_in_out('white', 10)
clear()