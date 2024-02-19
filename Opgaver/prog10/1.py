# IMPORTS
from hcsr04 import HCSR04
import uasyncio as asyncio

# OBJECTS
ultrasonic = HSCR04(15,34)

# FUNCTIONS
async def distance():
    while True:
        print(f'distance: {ultrasonic.distance_cm()} CM')
        await asyncio.sleep_ms(300)
        
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()