from machine import  I2C
from eeprom_24xx64 import EEPROM_24xx64

# OBJECTS + VARIABLES
i2c = I2C(0, freq= 400000)

eeprom = EEPROM_24xx64(i2c, 0x50)

# PROGRAM
print('EEPROM 24LC64 via I2C H/W 0 test program\n')

eeprom.write_string(0xA7, 'Hello, world!')
eeprom.read_string(0xA7)
eeprom.print(0xA7, 16)