from time import ticks_ms

start_1 = ticks_ms()
time_period_1 = 2000

start_2 = ticks_ms()
time_period_2 = 200

while True:
    if ticks_ms() - start_1 > time_period_1:
        print('Times up!')
        start_1 = ticks_ms()
        
    if ticks_ms() - start_2 > time_period_2:
        print(