## Make your firefly blink

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now you will make your firefly blink on and off like a real firefly. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Change your code to make the firefly blink on and off in a `while True` loop. The timings represent the light patterns of a real firefly. 

Make sure that the code on lines 11-14 are indented. 

**Tip:** In Thonny you can indent code by going to the beginning of the line and tapping the tab key, this will insert four spaces. Thonny will automatically indent code based on the previous line.

--- code ---
---
language: python
filename: firefly.py
line_numbers: true
line_number_start: 8
line_highlights: 9-14
---
firefly = LED(13)

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

+ Fix any errors in your code including indentation. 
+ Check that none of the connections to your LED Firefly have come lose. 

--- /task ---

--- save ---