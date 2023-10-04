from socket import socket, timeout
from time import sleep
from socket import AF_INET
from socket import SOCK_DGRAM
from machine import Pin, ADC
from gpio_lcd import GpioLcd
from sys import exit

#### OBJEKTER
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
#s.settimeout(10)

pot = ADC(Pin(34, Pin.IN),atten=3)
pot.width(10)

#### STATES
class States:
    UdpState = False

#### PROGRAM
while True:

    if pot.read() == 1023 and States.UdpState == False:
        print('UDP ON')
        print(pot.read())
        States.UdpState = True
        
    elif pot.read() == 0 and States.UdpState == True:
        print('UDP OFF')
        print(pot.read())
        States.UdpState = False
    
    if States.UdpState == True:
        print('Running...')
        sleep(1)
        pot.read()
        try:
            message, client_address = server_socket.recvfrom(2048)
            modified_message = message.decode()
            server_socket.sendto(modified_message.encode(), client_address)
            if modified_message != '':
                print(modified_message)
                modified_message + ''
        except:
            server_socket.close()
            exit()
    
    elif States.UdpState == False:
        print('UDP Stopped')
        sleep(1)
        