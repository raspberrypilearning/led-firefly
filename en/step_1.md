## You will make

In this project, you will use a Raspberry Pi Pico to make an LED firefly that flashes in a particular pattern, just like fireflies in nature, and connect a switch to control the light. 

[[[flashing-light-warning]]]

<div style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;display: flex; flex-wrap: wrap'>
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A <span style="color: #0faeb0">microcontroller</span> is a tiny computing device that can run code and interact with <span style="color: #0faeb0"> electronics components</span> (such as buttons and lights). It is usually designed to complete a single task, and doesn't have an <span style="color: #0faeb0">operating system</span>. 
The Raspberry Pi Pico is a low-cost microcontroller that can be used by beginners and can also be used by experts to develop electronic products.
</div>
<div>
![A drawing of a hand holding a Raspberry Pi Pico.](images/pico-hand.png){:width="300px"}
</div>
</div>

<br/>
You will:

+ Meet the Raspberry Pi Pico **microcontroller** 
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

You can purchase all the required hardware for this project and the other projects in this path from the [Kitronik web store.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

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

![](http://code.org/api/hour/begin_rp_ledfirefly.png)
