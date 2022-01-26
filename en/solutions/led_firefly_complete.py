from picozero import pico_led, LED, Switch
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13)
switch = Switch(18)

while True:
    if switch.is_closed:
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.3)
    else:
        firefly.off()
        sleep(0.1)
