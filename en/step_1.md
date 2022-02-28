## Introduction

Use a Raspberry Pi Pico to make an LED firefly that flashes in a particular pattern, just like fireflies in nature. Connect a switch to control the light. 

[[[flashing-light-warning]]]

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A <span style="color: #0faeb0">microcontroller</span> is a tiny computing device that can run code and interact with<span style="color: #0faeb0"> electronics components</span> (such as buttons and lights). It is usually designed to complete a single task, and doesn't have an <span style="color: #0faeb0">operating system</span>. 
The Raspberry Pi Pico is a low cost microcontroller that can be used by beginners and can also be used by experts to develop electronic products. 
</div>
<div>
![A drawing of a hand holding a Raspberry Pi Pico.](images/pico-hand.png){:width="300px"}
</div>
</div>
</p>

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

![An LED with tape stuck to it to form wings. There ae two jumper wires connected to the LED, one with a resister held in place by electrical tape.](images/showcase_static.png)

--- /task ---

--- /print-only ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
An <span style="color: #0faeb0">embedded device</span> often contains a microcontroller and is designed for a specific task. You might have used one in a games controller, microwave oven, mood light, electronic game or toy, pedometer, voice controlled home assistant, medical device or electronic calculator. Can you think of embedded devices that you use?</p> 

To complete this project you will need:

**Hardware**

+ A Raspberry Pi Pico with pin headers soldered on
+ A **data** USB A to micro USB cable
+ 1 x yellow LED (or any colour you prefer)
+ 1 x 100Ω resistor (any resistor from 75Ω-220Ω will work)
+ 1 x pin-socket jumper wire
+ 3 x socket-socket jumper wire
 
+ Optional: Sticky tape, invisible tape works best

[[[pin-socket-jumper-wires]]]

You can [prepare your LED](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/1){:target="_blank"} in advance by attaching it to a resistor and jumper wires before starting the project. 

**Software**

+ Thonny - this project can be completed using the Thonny Python editor which can be installed on a Linux, Windows or Mac computer.

[[[thonny-install]]]

[[[change-theme-thonny]]]

