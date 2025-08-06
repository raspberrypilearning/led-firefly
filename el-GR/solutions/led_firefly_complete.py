from picozero import pico_led, LED, Switch
from time import sleep

# Ανάβει και σβήνει το LED στην πλακέτα Pico
pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13) # Χρησιμοποίησε το GP13
switch = Switch(18) # Χρησιμοποίησε το GP18

while True:
    if switch.is_closed: # Ο διακόπτης είναι συνδεδεμένος
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.3)
    else: # Ο διακόπτης δεν είναι συνδεδεμένος
        firefly.off()
        sleep(0.1)
