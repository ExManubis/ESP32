from machine import Pin, PWM, ADC
from time import sleep

# VARIABLES
led_freq = 50
led_duty = 0 # 0-1023

led_duty_red = 512
led_duty_green = 750
led_duty_blue = 345

bvalue = 0

# OBJECTS
led_red = PWM(Pin(18)) # 1.88 VF, 
led_green = PWM(Pin(5)) # 2.54 VF, 
led_blue = PWM(Pin(19)) # 2.64 VF,

potent = ADC(Pin(34, Pin.IN), atten = 3)
potent.atten(ADC.ATTN_11DB)
potent.width(ADC.WIDTH_9BIT)

pb2 = Pin(0, Pin.IN)

# FUNCTIOM
def led_duty_pct(dutypct):
    pct = float(dutypct) / 100.0
    led_duty = int(1023.0 * pct)
    led_red.duty(led_duty)
    led_blue.duty(led_duty)
    led_green.duty(led_duty)

# PROGRAM
led_red.freq(led_freq)
led_green.freq(led_freq)
led_blue.freq(led_freq)

while True:
    potent_val = potent.read()
    duty_clc = int(potent_val) * 2
    if pb2.value() == 0:
        bvalue = bvalue+1
    elif bvalue == 1:
        led_red.duty(duty_clc)
    elif bvalue == 2:
        led_green.duty(duty_clc)
    elif bvalue == 3:
        led_blue.duty(duty_clc)
    elif bvalue == 0:
        led_red.duty(duty_clc)
        led_green.duty(duty_clc)
        led_blue.duty(duty_clc)
    elif bvalue > 3:
        bvalue = 0
    print(potent_val)
    print(bvalue)
    sleep(1)