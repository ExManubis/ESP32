def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Batcave-24', 'Thermopylae480')
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig()[0]) # return IP
    if wlan.isconnected():
        print('network config:', wlan.ifconfig()[0]) # return IP
        
do_connect()