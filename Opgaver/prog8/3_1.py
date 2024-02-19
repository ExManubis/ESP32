# IMPORTS
from machine import TouchPad, Pin
from time import sleep_ms, ticks_ms

# OBJECTS
touch1 = TouchPad(Pin(0, Pin.IN))

led1 = Pin(26, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(13, Pin.OUT)

# VARIABLES
start_time = ticks_ms()
treshold_miliseconds = 500

# PROGRAMME
while True:
    print(touch1.read())
    t_value = touch1.read()
    sleep_ms(500)
    if t_value < 130:
        if ticks_ms() - start_time > treshold_miliseconds:
            led1.value(not led1.value())
            led2.value(not led2.value())
            led3.value(not led3.value())
            start_time = ticks_ms()
    else:
        led1.off()
        led2.on()
        led3.off()