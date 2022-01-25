## Light an external LED

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Connect an LED and a resistor to your Raspberry Pi Pico using jumper wires. Add a button to switch it on and off.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">LED</span> stands for light emitting diode. It uses electroluminescence, which is where a material lights up when an electrical current passes through it. An LED has two legs, a long one and a short one and must be connected the right way around. The long leg is positive (+) leg and the short one is the negative (-). Another way to check if a leg is positive or negative is to use your finger to find the flat side of the LED bulb. The flat side is on the same side as the negative leg.
</p>

--- task ---

Make sure that you have an LED connected to a resistor and two socket-socket jumper wires.  

[[[led-resistor-electrical-tape]]]

[led-resistor-heatshrink]

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
A <span style="color: #0faeb0">resistor</span> controls the current that flows through a circuit. This protects the LED from burning out and will make it last longer. </p>

A Raspberry Pi Pico has 40 pins on its board. Pins allow you to connect external components to the Raspberry Pi Pico.  

--- task ---

Explore your Raspberry Pi Pico and find the pin that is labelled **GP13**. You will notice that there are labels for each pin on the underneath side of the Raspberry Pi Pico. 

![Photo of the Raspberry Pi Pico from underneath with GP 13 highlighted](images/gp13-pico.png)

--- /task ---

--- task ---

![A diagram of the Raspberry Pi Pico with a yellow LED connected to GND and to GP14 through a resistor.](images/pico_led_14_bb.svg)

Connect the jumper wire that is attached to the positive leg of the LED (the one with the resistor) to pin **GP14**. Push it until the black plastic meets the base of the header and that it is secure. 

--- /task ---

--- task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
A <span style="color: #0faeb0">firefly</span> is a kind of beetle, also called a glowworm or lightning bug, which flashes using bioluminescence to identify themselves to other members of the same species. Different species flash in different patterns. 
</p>

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 1
line_highlights: 1,8-9
---
from picozero import pico_led, LED
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

firefly = LED(14)
firefly.on()

--- /code ---

--- /task ---

--- task ---
**Test** Run your code and your LED firefly should light up. 

**Debug**:

+ Check that your LED has the negative (shorter, flat) side attached to GND and the positive (longer )
--- /task ---

--- save ---