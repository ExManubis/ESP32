# IMPORTS
from gpio_lcd import GpioLcd
from machine import Pin

# OBJECTS
lcd = GpioLcd(rs_pin = Pin(27), enable_pin = Pin(25),
              d4_pin = Pin(33), d5_pin = Pin (32),
              d6_pin = Pin(21), d7_pin = Pin(22),
              num_lines = 4, num_columns=20,
              backlight_pin = Pin(23, Pin.OUT))

# VARIABLES
custom_character = bytearray([0x04, 0x04,
                              0x04, 0x04,
                              0x04, 0x1F,
                              0x04, 0x04])

# PROGRAMME
lcd.clear()
lcd.move_to(1, 0)
lcd.putstr('Mikkel')
lcd.move_to(7,0)
lcd.custom_char(0, custom_character)
lcd.putchar(chr(0))
lcd.move_to(0,0)
lcd.custom_char(0, custom_character)
lcd.putchar(chr(0))