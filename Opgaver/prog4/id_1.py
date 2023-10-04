import neopixel, machine
from machine import Pin
from time import sleep
import umqtt_robust2 as mqtt

#### OBJEKTER OG VARIABLER

# neopixel object
p = 15

n = 12

np = neopixel.NeoPixel(machine.Pin(15), 12)

#### FUNKTIONER

# ens farve
def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
        np.write()
    color.clear()
    color.append(r)
    color.append(g)
    color.append(b)
    return (r, g, b)

# set color but dont overwrite values
def set_color_2(a, c, d):
    for i in range(n):
        np[i] = (a, c, d)
        np.write()

# farve intensitet
def col_str():
    if mqtt.besked == '0':
        set_color_2(0, 0, 0)
    
    elif mqtt.besked == '25':
        set_color_2((color[0] // 4), (color[1] // 4), (color[2] // 4))
    
    elif mqtt.besked == '50':
        set_color_2((color[0] // 2), (color[1] // 2), (color[2] // 2))
        
    elif mqtt.besked == '75':
        c1 = int(float(color[0]) // 1.3)
        c2 = int(float(color[1]) // 1.3)
        c3 = int(float(color[2]) // 1.3)
        set_color_2(c1, c2, c3)

# hex til RGB func
def hex_to_rgb(hex_color):
    hex_color = hex_color.strip('#') # fjern # fra string
    rgb_list = [] # opret liste
    for i in range (0, 6, 2): # for loop med range (fra, til, step)
        # Konverterer hvert par tegn i string til base 16
        # Derefter returneres integer værdien som tilføjes til listen
        rgb_list.append(int(hex_color[i:i + 2], 16))
    return tuple(rgb_list) # returnerer en tuple

#### PROGRAM
color = []
set_color(255, 0, 0)
while True:
    
    try:
        if '#' in mqtt.besked and len(mqtt.besked) == 7:
            try:
                rgb_tuple = hex_to_rgb(mqtt.besked) #indsætter besked som arg i func
                print(f'RGB tuple: {rgb_tuple}')
                set_color(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
            except:
                print('Wrong hex value!')
        
        elif mqtt.besked == '0':
            set_color_2(0, 0, 0)
    
        elif mqtt.besked == '25':
            set_color_2((color[0] // 4), (color[1] // 4), (color[2] // 4))
    
        elif mqtt.besked == '50':
            set_color_2((color[0] // 2), (color[1] // 2), (color[2] // 2))
        
        elif mqtt.besked == '75':
            c1 = int(float(color[0]) // 1.3)
            c2 = int(float(color[1]) // 1.3)
            c3 = int(float(color[2]) // 1.3)
            set_color_2(c1, c2, c3)
        
        elif mqtt.besked == '100':
            set_color_2(color[0], color[1], color[2])
        
        elif len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""

        mqtt.sync_with_adafruitIO() # sync med Adafruit

    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()