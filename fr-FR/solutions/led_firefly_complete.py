from picozero import pico_led, LED, Switch
from time import sleep

# Turn the LED on the Pico board on and off
pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13) # Use GP13
switch = Switch(18) # Use GP18

while True:
    if switch.is_closed: # Switch is connected
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.3)
    else: # Switch is not connected
        firefly.off()
        sleep(0.1)
