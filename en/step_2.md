## Set up MicroPython

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Set up MicroPython so that you can program your Raspberry Pi Pico.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> is a version of the Python programming language for microcontrollers, like your Raspberry Pi Pico. MicroPython lets you use your Python knowledge to write code to interact with electronics components.</p>

If you have never used MicroPython on your Raspberry Pi Pico, you will need to add the MicroPython firmware.

[[[add-micropython-firmware]]] 

--- task ---

**Debug:** 

--- collapse ---

---
title: I don't know if firmware is installed and cannot connect to my Pico
---

Make sure your Raspberry Pi Pico is connected to your computer with a microUSB cable. Click on the list in the bottom right of your Thonny window. A popup menu will appear listing the available interpreters. 

[A popup menu showing an option saying configure interpreter](images/no-pico-interpreter.png) 

If you cannot see the Pico in the list (like in the picture), you will need to reconnect your Raspberry Pi Pico while holding the BOOTSEL button to mount it as a storage volume and reinstall the firmware by following the instructions in the collapse above.

--- /collapse ---

--- collapse ---

---
title: Firmware is installed but I still cannot connect to my Pico
---

You may be using the wrong kind of microUSB cable. Your current microUSB cable may be damaged, or designed only to carry power to devices and cannot transfer data. Try swapping your cable if nothing else has worked. 

If your Pico still won't connect after trying all these things, it may *itself* be damaged and unable to connect. 

--- /collapse ---

--- /task ---

--- task ---

<mark>Add the Pico Zero library. Tools > Manage Plugins > Pico??? to add it in.</mark>

--- /task ---

--- save ---