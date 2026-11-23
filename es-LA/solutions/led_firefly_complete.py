from picozero import pico_led, LED, Switch
from time import sleep

# Enciende y apaga el LED de la placa Pico
pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13) # Usa GP13
switch = Switch(18) # Usa GP18

while True:
    if switch.is_closed: # El interruptor está conectado
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.3)
    else: # El interruptor no está conectado
        firefly.off()
        sleep(0.1)
