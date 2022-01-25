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


--- /task ---

--- task ---

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 8
line_highlights: 9-14
---
firefly = LED(13)

while True:
    firefly.on()
    sleep(0.5)
    firefly.off()
    sleep(2.3)
--- /code ---

--- /task ---

--- save ---