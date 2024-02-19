# IMPORTS
from machine import ADC, Pin
from time import sleep

# CLASSES
class LMT84:
    
    def __init__(self, pin_number = 35, ADC2_mV = 2048.0 / 4095.0,
                 alpha = -4.7, beta = 1035, average = 128):
        self.pin_number = pin_number
        self.lmt84_ADC = ADC(Pin(pin_number))
        self.lmt84_ADC.atten(ADC.ATTN_6DB)
        self.ADC2_mV = ADC2_mV
        self.alpha = alpha
        self.beta = beta
        self.average = average
        # Set variables to None
        self.temperature_celsius = None
        self.temperature_fahrenheit = None
        self.temperature_kelvin = None
        
    def measure_celsius(self):
        ADC_value = 0
        if self.average > 1:
            for i in range (self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)
        
        mV = self.ADC2_mV * ADC_value
        temp_c = (mV - self.beta) / self.alpha
        return temp_c
    
    def measure_fahrenheit(self): # 2.4
        ADC_value = 0
        if self.average > 1:
            for i in range (self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)
        
        mV = self.ADC2_mV * ADC_value
        temp_c = (mV - self.beta) / self.alpha
        temp_f = temp_c * 9/5 + 32
        return temp_f
    
    def measure_kelvin(self): # 2.5
        ADC_value = 0
        if self.average > 1:
            for i in range (self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)
        
        mV = self.ADC2_mV * ADC_value
        temp_c = (mV - self.beta) / self.alpha
        temp_k = temp_c + 273.15
        return temp_k

# VARIABLES
lmt84 = LMT84()
tc = lmt84.measure_celsius()
tf = lmt84.measure_fahrenheit()
tk = lmt84.measure_kelvin()

# PROGRAMME
print('Celcius: ', tc, '\nFahrenheit: ', tf, '\nKelvin: ', tk) 