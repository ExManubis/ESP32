# IMPORTS
from gpio_lcd import GpioLcd
from machine import Pin
from time import sleep

# OBJECTS
lcd = GpioLcd(rs_pin = Pin(27), enable_pin = Pin(25),
              d4_pin = Pin(33), d5_pin = Pin (32),
              d6_pin = Pin(21), d7_pin = Pin(22),
              num_lines = 4, num_columns=20,
              backlight_pin = Pin(23, Pin.OUT))

# PROGRAMME
lcd.clear()
lcd.move_to(1, 0)
lcd.putstr('LINJE 1')

lcd.move_to(1, 1)
lcd.putstr('LINJE 2')

lcd.move_to(1, 2)
lcd.putstr('LINJE 3')

lcd.move_to(1, 3)
lcd.putstr('LINJE 4')

lcd.move_to(0, 0)
lcd.blink_cursor_on() 