# IMPORTS
from machine import  Pin, deepsleep
from time import sleep
from neopixel import NeoPixel
import random

# OBJECTS + VARIABLES
sleep_time_ms = 4000
np = NeoPixel(Pin(15, Pin.OUT), 12)

# FUNCTIONS
def set_color(r, g, b): 
    for pixel in range(12): # n = 12
        np[pixel] = (r, g, b)
        np.write()
        #sleep(0.3)

print(f'ESP32 will now sleep for {sleep_time_ms/1000} seconds')
r = random.randrange(0, 25)
b = random.randrange(0, 25)
g = random.randrange(0, 25)
set_color(r, b, g)
deepsleep(4000)