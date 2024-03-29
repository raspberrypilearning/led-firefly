## Make your firefly blink

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now you will make your firefly blink on and off, like a real firefly. 
</div>
<div>
![An animation of the firefly LED blinking on and off.](images/firefly-blink.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
A <span style="color: #0faeb0">firefly</span> is a kind of beetle, also called a glow worm or lightning bug. They use bioluminescence to flash to identify themselves to other members of the same species. Different species flash in different patterns. 
</p>

--- task ---

Change your code to make the firefly blink on and off in a `while True:` loop. The timings represent the light patterns of a real firefly. 

Make sure that the code on lines 11–14 are indented. 

**Tip:** In Thonny you can indent code by going to the beginning of the line and tapping the <kbd>Tab</kbd> key — this will insert four spaces. Thonny will automatically indent code based on the previous line when your press <kbd>Enter</kbd> while typing.

--- code ---
---
language: python
filename: firefly.py
line_numbers: true
line_number_start: 8
line_highlights: 9-14
---
firefly = LED(13) # Use GP13

while True:
    firefly.on()
    sleep(0.5)
    firefly.off()
    sleep(2.5)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the firefly slowly blink on and off. 

![An animation of the firefly LED blinking on and off.](images/firefly-blink.gif)

**Debug:**

+ Fix any errors in your code, including indentation 
+ Check that none of the connections to your LED firefly have come loose 

--- /task ---