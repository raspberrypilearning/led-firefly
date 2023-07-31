from picozero import pico_led, LED, Switch
from time import sleep

# Allumer et éteindre la LED sur la carte Pico
pico_led.on()
sleep(1)
pico_led.off()

luciole = LED(13) # Utiliser GP13
interrupteur = Switch(18) # Utiliser GP18

while True:
    if interrupteur.is_closed: # L'interrupteur est connecté
        luciole.on()
        sleep(0.5)
        luciole.off()
        sleep(2.3)
    else: # L'interrupteur n'est pas connecté
        luciole.off()
        sleep(0.1)
