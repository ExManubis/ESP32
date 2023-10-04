from machine import Pin, ADC
import neopixel, machine
from time import sleep_ms
import umqtt_robust2 as mqtt

####  OBJEKTER

# neopixel object
p = 15

n = 12

np = neopixel.NeoPixel(machine.Pin(15), 12)

# potentiometer
pot = ADC(Pin(34, Pin.IN))
pot.width(10)

#### FUNKTIONER
# cycle
def cycle(r, g, b, wait):
    for i in range (4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (r, g, b)
        np.write()
        sleep_ms(wait)


#### STATES

class states:
    # klasse til at opbevare variabler om states.
    test_state = False
    
#### PROGRAM
    
while True:
    try:
        if mqtt.besked == 'start state':
            print('starter nuclear bomb test state')
            states.test_state = True
                
        elif mqtt.besked == 'stop state':
            print('stopper nuclear bomb test state')
            states.test_state = False
        
        if states.test_state == True:
            if pot.read() <= 500:
                cycle(255, 0, 255, 10)
            elif pot.read() > 500 and pot.read() < 1500:
                cycle(255, 0, 255, 50)
                
            elif pot.read() >= 1500 and pot.read() <= 3000:
                cycle(255, 0, 255, 100)
        
            elif pot.read() >= 3000:
                cycle(255, 0, 255, 200)
        
        
        elif len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""

        mqtt.sync_with_adafruitIO() # sync med Adafruit

    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()