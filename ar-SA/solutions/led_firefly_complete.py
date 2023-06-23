from picozero import pico_led, LED, Switch
from time import sleep

# قم بتشغيل و إطفاء LED على لوحة Pico
pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(13) # استخدام منفذ GP13
switch = Switch(18) # استخدام منفذ GP18

while True:
    if switch.is_closed: # المفتاح متصل
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.3)
    else: # المفتاح غير متصل
        firefly.off()
        sleep(0.1)
