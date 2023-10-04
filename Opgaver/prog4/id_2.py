import neopixel, machine
from machine import Pin
from time import sleep


#### OBJEKTER
pb1 = Pin(4, Pin.IN) # sætter knap til Input

# neopixel object
p = 15

n = 12

np = neopixel.NeoPixel(machine.Pin(15), 12)

#### FUNKTIONER

# clear funktion
def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()


#### PROGRAM
pixel = 0

while True:
    first = pb1.value()
    sleep(0.1)
    second = pb1.value()
    if first == 1 and second == 0:
        clear()
        if pixel == 0 or pixel == 12:
            np[0] = (255, 0, 0)
            pixel = 0
            pixel = pixel + 1
            np.write()
        else: 
            np[pixel] = (255, 0, 0)
            pixel = pixel + 1
            np.write()
