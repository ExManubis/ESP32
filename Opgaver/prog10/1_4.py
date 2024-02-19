# IMPORTS
from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin, PWM


# OBJECTS
ultrasonic = HCSR04(15, 34)

lcd = GpioLcd(rs_pin = Pin(27), enable_pin = Pin(25),
              d4_pin = Pin(33), d5_pin = Pin (32),
              d6_pin = Pin(21), d7_pin = Pin(22),
              num_lines = 4, num_columns=20,
              backlight_pin = Pin(23, Pin.OUT))

led1 = Pin(26, Pin.OUT)
pwmled1 = PWM(led1)

pb1 = Pin(4, Pin.IN)

# FUNCTIONS
async def distance():
    while True:
        print(f'distance: {ultrasonic.distance_cm()} CM')
        await asyncio.sleep_ms(300)

async def lcd_distance():
    while True:
        lcd.move_to(0, 0)
        lcd.putstr(f'dist: {ultrasonic.distance_cm():.2f} CM')
        await asyncio.sleep_ms(1000)
        
async def led_brightness():
    while True:
        pwmled1.freq(1000)
        pwmled1.duty(int(ultrasonic.distance_cm()) * 4)
        await asyncio.sleep_ms(300)

async def button_distance():
    while True:
        if pb1.value() == 0:
            if ultrasonic.distance_cm() < 30.0:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr(f'dist: {ultrasonic.distance_cm():.2f} CM')
                lcd.move_to(0,1)
                lcd.putstr('Too close to display')
            elif ultrasonic.distance_cm() > 30.0 and ultrasonic.distance_cm() < 60.0:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr(f'dist: {ultrasonic.distance_cm():.2f} CM')
                lcd.move_to(0,1)
                lcd.putstr('Good distance')
            elif ultrasonic.distance_cm() > 60.0:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr(f'dist: {ultrasonic.distance_cm():.2f} CM')
                lcd.move_to(0,1)
                lcd.putstr('Too far')
        await asyncio.sleep_ms(300)

# PROGRAMME
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.create_task(lcd_distance())
loop.create_task(led_brightness())
loop.create_task(button_distance())
lcd.clear()
loop.run_forever()


