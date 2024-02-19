# IMPORTS
from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin

# OBJECTS
ultrasonic = HCSR04(15, 34)

lcd = GpioLcd(rs_pin = Pin(27), enable_pin = Pin(25),
              d4_pin = Pin(33), d5_pin = Pin (32),
              d6_pin = Pin(21), d7_pin = Pin(22),
              num_lines = 4, num_columns=20,
              backlight_pin = Pin(23, Pin.OUT))

# FUNCTIONS
async def distance():
    while True:
        print(f'distance: {ultrasonic.distance_cm()} CM')
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(f'dist: {ultrasonic.distance_cm()} CM')
        await asyncio.sleep_ms(1000)
        
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()
