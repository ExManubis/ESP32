# IMPORTS
from time import sleep
from machine import Pin

# CLASSES
class CallbackHandler:
    def __init__(self, encoder_button):
        self.encoder_button = encoder_button # pin objekt til button
        self.menu_items = [] # liste til at holde dictionaries med tekst og cb
        self.encoder_last_state = None # gem sidste encoder state
        self.encode_button_pressed = False # flag til at tracke knaptryk
        self.callback_count = 0 # tæller igennem listen
        self.initialize_button()
        
    def initialize_button(self):
        self.encoder_button.irq(handler=self.encoder_button_callback, trigger = Pin.IRQ_FALLING)
        
    def encoder_button_callback(self, pin):
        if self.encode_button_pressed == False:
            self.encode_button_pressed = True
    
    def add_menu(self, text, callback): # funktion til at tilføje menu tekst + cb
        self.menu_items.append({'text':text, 'callback':callback})
        
    def run(self):
        print('loop started')
        while True:
            if self.encode_button_pressed:
                print('BTN pressed')
                callback = self.menu_items[self.callback_count]['callback']
                if callback:
                    callback()
                    self.encode_button_pressed = False
                    self.callback_count +=1
                    sleep(0.05)