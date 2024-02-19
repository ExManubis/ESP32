# IMPORTS
from machine import Pin, deepsleep
from time import sleep
import esp32

# OBJECTS
wake_pin = Pin(4, Pin.IN, Pin.PULL_UP)
led1 = Pin(26, Pin.OUT)

# PROGRAMME
print('ESP32 ON!')
for i in range (20):
    led1.value(not led1.value())
    sleep(1)
sleep(4)
esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
deepsleep()