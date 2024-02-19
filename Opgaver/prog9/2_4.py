# IMPORTS
from machine import Pin
from cbhandler import CallbackHandler

# VARIABLES + OBJECTS
rotary_encoder_pushbutton = Pin(14, Pin.IN)
cb_handler = CallbackHandler(rotary_encoder_pushbutton)

# FUNCTIONS
def test_callback_1():
    print('cb1 called')
    
def test_callback_2():
    print('cb2 called')
    
def test_callback_3():
    print('cb3 called')
    
def test_callback_4():
    print('cb4 called')
    
# PROGRAMME
cb_handler.add_menu('test1', test_callback_1)
cb_handler.add_menu('test2', test_callback_2)
cb_handler.add_menu('test3', test_callback_3)
cb_handler.add_menu('test4', test_callback_4)
cb_handler.run()