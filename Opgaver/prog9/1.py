# IMPORTS
from machine import Pin

# OBJECTS
rotary_button = Pin(14, Pin.IN) # rotary knap, sæt GP4 til SCK
led1 = Pin(26, Pin.OUT)

# FUNCTIONS
def isr_handler_function(pin_object):
    led1.value(not led1.value())
    print('Pressed!')

# PROGRAMME
print(rotary_button.value())
rotary_button.irq(handler = isr_handler_function, trigger = Pin.IRQ_FALLING)
