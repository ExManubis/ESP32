from dht import DHT11
from machine import Pin

dht11 = DHT11(Pin(0, Pin.IN))
dht11.measure()

temperature = dht11.temperature()
humidity = dht11.humidity()

print('temp', temperature)
print('humidity', humidity)