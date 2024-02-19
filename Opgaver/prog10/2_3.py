# IMPORTS
from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin, PWM, deepsleep
import esp32
from time import sleep


# OBJECTS
ultrasonic = HCSR04(15, 34)

lcd = GpioLcd(rs_pin = Pin(27), enable_pin = Pin(25),
              d4_pin = Pin(33), d5_pin = Pin (32),
              d6_pin = Pin(21), d7_pin = Pin(22),
              num_lines = 4, num_columns=20,
              backlight_pin = Pin(23, Pin.OUT))

pb1 = Pin(4, Pin.IN)

wake_pin = Pin(4, Pin.IN, Pin.PULL_UP)

esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
# FUNCTIONS
async def lcd_distance():
    while True:
        if ultrasonic.distance_cm() > 100.0:
            lcd.move_to(0, 0)
            lcd.putstr('Human gone. Going to sleep...')
            deepsleep()
            await asyncio.sleep_ms(1000)
        else:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(f'dist: {ultrasonic.distance_cm():.2f} CM')
            await asyncio.sleep_ms(1000)

        

# PROGRAMME
loop = asyncio.get_event_loop()
loop.create_task(lcd_distance())
lcd.clear()
loop.run_forever()