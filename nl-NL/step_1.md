## Inleiding

In dit project gebruik je een Raspberry Pi Pico om een LED-vuurvlieg te maken die in een bepaald patroon knippert, net zoals vuurvliegen in de natuur, en sluit je een schakelaar aan om het licht te besturen.

[[[flashing-light-warning]]]

<div style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;display: flex; flex-wrap: wrap'>
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Een <span style="color: #0faeb0">microcontroller</span> is een klein computerapparaat dat code kan uitvoeren en kan communiceren met <span style="color: #0faeb0"> elektronische onderdelen</span> (zoals knoppen en lampjes). Het is meestal ontworpen om een enkele taak te voltooien en heeft geen <span style="color: #0faeb0">besturingssysteem</span>. 
De Raspberry Pi Pico is een goedkope microcontroller die door beginners kan worden gebruikt en ook door experts kan worden gebruikt om elektronische producten te ontwikkelen.
</div>
<div>
![Een tekening van een hand met een Raspberry Pi Pico.](images/pico-hand.png){:width="300px"}
</div>
</div>

<br/>
Je gaat:

+ Kennismaken met de Raspberry Pi Pico **microcontroller**
+ Connect an LED and a switch made from jumper wires to the pins on a **Raspberry Pi Pico**
+ Program the Raspberry Pi Pico using **MicroPython** and Thonny

--- no-print ---

--- task ---

This example shows an LED blinking to mimic a real firefly! Can you spot the repeating pattern in the flashes?

![An animation of the firefly LED blinking on and off.](images/firefly-blink.gif){:width="300px"}

--- /task ---

--- /no-print ---

--- print-only ---

--- task ---

This example shows an LED firefly. Your LED will blink to mimic a real firefly!

![An LED with tape stuck to it to form wings. There are two jumper wires connected to the LED, one with a resister held in place by electrical tape.](images/showcase_static.png)

--- /task ---

--- /print-only ---

To complete this project you will need:

**Hardware**

You can purchase all the required hardware for this project and the other projects in this path from the [Pimoroni web store.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

+ A Raspberry Pi Pico with pin headers soldered on
+ A **data** USB A to micro USB cable
+ 1× yellow LED (or any colour you prefer)
+ 1× 100Ω resistor (any resistor from 75Ω to 220Ω will work)
+ 1× pin–socket jumper wire
+ 3× socket–socket jumper wire
+ Optional: Sticky tape, invisible tape works best

[[[pin-socket-jumper-wires]]]

You can [prepare your LED](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} in advance by attaching it to a resistor and jumper wires before starting the project.

**Software**

+ Thonny – this project can be completed using the Thonny Python editor, which can be installed on a Linux, Windows, or Mac computer

[[[thonny-install]]]

[[[change-theme-thonny]]]

