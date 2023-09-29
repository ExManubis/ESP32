import machine, neopixel, time
import umqtt_robust2 as mqtt
from machine import Pin, PWM
from time import sleep

# antal pixels
n = 12

# pin den er tilkoblet
p = 15

# neopixel objekt
np = neopixel.NeoPixel(machine.Pin(p), n)

###########################################
#                funktioner               #
###########################################

# ens farve funktion
def set_color(r, g, b):
    for i in range(n): 
        np[i] = (r, g, b)
        np.write()
        
# clear funktion
def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

# hex til RGB func
def hex_to_rgb(hex_color):
    hex_color = hex_color.strip('#') # fjern # fra string
    rgb_list = [] # opret liste
    for i in range (0, 6, 2): # for loop med range (fra, til, step)
        # Konverterer hvert par tegn i string til base 16
        # Derefter returneres integer værdien som tilføjes til listen
        rgb_list.append(int(hex_color[i:i + 2], 16))
    return tuple(rgb_list) # returnerer en tuple

###########################################
while True:
    try:
        if '#' in mqtt.besked and len(mqtt.besked) == 7:
            try:
                rgb_tuple = hex_to_rgb(mqtt.besked) #indsætter besked som arg i func
                print(f'RGB tuple: {rgb_tuple}')
                set_color(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
            except:
                print('Wrong hex value!')
        
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO()
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
        