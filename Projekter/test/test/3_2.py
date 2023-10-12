from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 12 # sætter antal pixels
p = 15 # særrer pin

np = NeoPixel(Pin(p, Pin.OUT), n)

# Øvelse 3.2
# laver set_color funktion til at skifte alle farver
def set_color(r, g, b): 
    for pixel in range(n): # n = 12
        np[pixel] = (r, g, b)
        np.write()
        sleep(0.3)

# laver clear funktion til at slukke alle pixels
def clear():
    for pixel in range(n):
        np[pixel] = (0, 0, 0)
        np.write()

while 10:
    set_color(0, 0, 255)
    clear()