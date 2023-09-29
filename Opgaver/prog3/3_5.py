import machine, neopixel, time
import umqtt_robust2 as mqtt
from machine import Pin, PWM
from time import sleep

BUZZ_PIN = 14 # sets buzzer to pin 14
buzzer_pin  = Pin(BUZZ_PIN, Pin.OUT) #laver variabel
pwm_buzz = PWM(buzzer_pin, duty=0) # slukker ved start

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
        
# buzzer funktion
def buzzer(buzzer_PWM_object, frequency, sound_duration, silence_duration):
    buzzer_PWM_object.duty(512)
    buzzer_PWM_object.freq(frequency)
    sleep(sound_duration)
    buzzer_PWM_object.duty(0)
    sleep(silence_duration)
    
# fade funktion
def fade_in_out(color, wait):
    for i in range(0, 4 * 256, 8):
        for j in range (n): # nested loop, runs for every top loop
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
                if color == 'red':
                    np[j] = (val, 0, 0)
                elif color == 'green':
                    np[j] = (0, val, 0)
                elif color == 'blue':
                    np[j] = (0 ,0, val)
                elif color == 'purple':
                    np[j] = (val, 0, val)
                elif color == 'yellow':
                    np[j] = (val, val, 0)
                elif color == 'teal':
                    np[j] = (0, val, val)
                elif color == 'white':
                    np[j] = (val, val, val)
            np.write()
        time.sleep_ms(wait)

def animate():
    set_color(255, 0, 0)
    buzzer(pwm_buzz, 329, 0.2, 0.5)
    clear()
    set_color(255, 0, 0)
    buzzer(pwm_buzz, 329, 0.2, 0.5)
    clear()
    set_color(255, 0, 0)
    buzzer(pwm_buzz, 329, 0.2, 0.5)
    clear()
    set_color(255, 0, 255)
    buzzer(pwm_buzz, 261, 0.2, 0.2)
    clear()
    set_color(0, 0, 255)
    buzzer(pwm_buzz, 392, 0.2, 0.2)
    clear()
    set_color(255, 0, 0)
    buzzer(pwm_buzz, 329, 0.2, 0.5)
    clear()
    set_color(255, 0, 255)
    buzzer(pwm_buzz, 261, 0.2, 0.2)
    clear()
    set_color(0, 0, 255)
    buzzer(pwm_buzz, 392, 0.2, 0.2)
    clear()
    set_color(255, 0, 0)
    buzzer(pwm_buzz, 329, 0.2, 1.0)
    clear()

################################################
while True:
    try:
        if mqtt.besked == 'animate':
            animate()
        
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO()
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()