from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from machine import Pin
from gpio_lcd import GpioLcd
from sys import exit
import umqtt_robust2 as mqtt

#### OBJEKTER
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))


#### STATES
class States:
    UdpState = True
    
#### PROGRAM
while True:
    try:
        if mqtt.besked == 'start state':
            print('starter UDP state')
            states.UdpState = True
                
        elif mqtt.besked == 'stop state':
            print('stopper UDP state')
            states.UdpState = False
        
        if states.UdpState == True:
            print('server is ready to recieve')
            message, client_address = server_socket.recvfrom(2048)
            modified_message = message.decode()
            server_socket.sendto(modified_message.encode(), client_address)
            if modified_message != '':
                print(modified_message)
                lcd.clear()
                lcd.putstr(modified_message)
                modified_message + ''
    except KeyboardInterrupt:
        print('CTRL-C pressed, closing down!')
        server_socket.clode()
        exit()
            