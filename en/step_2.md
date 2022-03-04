## Set up your Raspberry Pi Pico

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Connect your Raspberry Pi Pico and set up MicroPython.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> is a version of the Python programming language for microcontrollers, like your Raspberry Pi Pico. MicroPython lets you use your Python knowledge to write code to interact with electronics components.</p>

--- task ---

**Connect:** the small end of your USB cable to the Raspberry Pi Pico.

![An image of a Raspberry Pi Pico connected to the small end of a USB cable.](images/pico-top-plug.png)

--- /task ---

--- task ---

**Connect:** the other end to your computer, laptop or Raspberry Pi.

![An image of a Raspberry Pi Pico connected to a laptop with a USB cable.](images/plug-in-pico.png)

--- /task ---


--- task ---

Open the Thonny editor. 

--- /task ---

--- task ---

Look at the text in the bottom right of the Thonny editor. It will show you the version of Python that is being used.

If it does not say 'MicroPython (Raspberry Pi Pico)' then click on the text and select 'MicroPython (Raspberry Pi Pico)'.

If you have never used MicroPython on your Raspberry Pi Pico, then Thonny will prompt you to add the MicroPython firmware. Click install. 

![MicroPython installation window with the Install button highlighted.](images/thonny-install-micropython-pico.png)

--- /task ---

--- task ---

**Debug:** 

--- collapse ---
---
title: There was an error installing the firmware
---
If you see an error message during install then:
+ disconnect your Raspberry Pi Pico
+ reconnect your Raspberry Pi Pico
+ try installing the firmware again (you might need to press the stop button first)

![A screenshot of an error message showing that the firmware cannot install correctly.](images/pico-firmware-error.PNG)

--- /collapse ---

--- collapse ---

---
title: I don't know if firmware is installed and cannot connect to my Pico
---

Make sure your Raspberry Pi Pico is connected to your computer with a microUSB cable. Click on the list in the bottom right of your Thonny window. A popup menu will appear listing the available interpreters. 

![A popup menu showing an option saying configure interpreter](images/no-pico-interpreter.png) 

If you cannot see the Pico in the list (like in the picture), you will need to reconnect your Raspberry Pi Pico while holding the BOOTSEL button to mount it as a storage volume and reinstall the firmware by following the instructions in the collapse above.

--- /collapse ---

--- collapse ---

---
title: Firmware is installed but I still cannot connect to my Pico
---

You may be using the wrong kind of microUSB cable. Your current microUSB cable may be damaged, or designed only to carry power to devices and cannot transfer data. Try swapping your cable if nothing else has worked. 

If your Pico still won't connect after trying all these things, it may *itself* be damaged and unable to connect. 

--- /collapse ---

You can find further information in the [Raspberry Pi Pico Guide](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

--- task ---

<mark>Add the Pico Zero library. Tools > Manage Plugins > Pico??? to add it in.</mark>

--- /task ---

--- save ---