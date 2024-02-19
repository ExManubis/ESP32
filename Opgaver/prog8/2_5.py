# IMPORTS
from time import sleep

# CLASSES
class OhmsLov:
    
    def measure_current(U, R):
        current = U/R
        print(U, '/', R, '=', current, 'ampere')
        return current
    
    def measure_voltage(R, I):
        voltage = R*I
        print(R, '*', I, '=', voltage, 'volt')
        return voltage
    
    def measure_resistance(U, I):
        resistance = U/I
        print(U, '/', I, '=', resistance, 'ohm')
        return resistance
    
    def measure_power(U, I):
        power = U*I
        print(U, '*', I, '=', power, 'watt')
        return power
    
# PROGRAMME
while True:
    print('Please choose: \n (C)urrent \n (V)oltage \n (R)esistance \n (P)ower') 
    path = input('\nEnter C, V, R or P: ')
    if path == 'C' or path == 'c':
        U = float(input('Enter voltage: '))
        R = float(input('Enter resistance: '))
        print('============================')
        OhmsLov.measure_current(U, R)
        print('============================')
        sleep(3)
    
    elif path == 'V' or path == 'v':
        R = float(input('Enter resistance: '))
        I = float(input('Enter current: '))
        print('============================')
        OhmsLov.measure_voltage(R, I)
        print('============================')
        sleep(3)
    
    elif path == 'R' or path =='r':
        U = float(input('Enter voltage: '))
        I = float(input('Enter current: '))
        print('============================')
        OhmsLov.measure_resistance(U, I)
        print('============================')
        sleep(3)
    
    elif path == 'P' or path == 'p':
        U = float(input('Enter voltage: '))
        I = float(input('Enter current: '))
        print('============================')
        OhmsLov.measure_power(U, I)
        print('============================')
        sleep(3)
    else :
        print('Please enter C, V, R or P....')
        sleep(2)

        