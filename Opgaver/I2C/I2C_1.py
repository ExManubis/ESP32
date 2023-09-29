#####################################
#          ESPROM TESTER            #
#####################################


####### IMPORT CLASSES + FUNCTIONS ##
from machine import I2C, Pin, SoftI2C
from time import sleep

####### OBJECTS + VARIABLES #########

i2c = I2C(0)

print('Running I2C scanner\n')

while True:
    # Scan for connected devices
    devices_identified = i2c.scan()
    
    # Print result
    devices_count = len(devices_identified)
    print('Total number of devices: %d' % devices_count)
    
    if devices_count == 112: # 16 reserves addresses
        print('Looks like the I2C bus pull-up resistors are missing')
        
        else:
            for i in range(devices_count):
                print('Device found at address: 0x%02X' % devices_identified[i])
                
                print() # blank line before next scan
                
                sleep(1)