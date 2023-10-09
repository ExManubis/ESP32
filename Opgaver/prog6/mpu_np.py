# IMPORT LIBRARIES
from machine import Pin, I2C
from neopixel import NeoPixel
from time import sleep
from mpu6050 import MPU6050
import sys

# INIT OBJECTS
i2c = IC2(0) # set IC2 to pin 18,19
mpu = MPU6050(i2c) # create mpu object

# VARIABLES


# FUNCTIONS


# APPLICATION
while True:
    try:
        print(imu.get_values()) # prints complete output string
        sleep(0.05)
    except KeyboardInterrupt:
        print('CTRL + C')
        sys.exit()