
--- question ---

---
legend: Question 3 of 3
---

You code an LED to blink, turn on, turn off, then toggle. What state would the LED be in after the code has run?

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
from picozero import LED

led = LED(15)

led.blink()

led.on()
led.off()

led.toggle()

--- /code ---
--- choices ---

- (x) On


  --- feedback ---
Yes! Since the last thing the LED did was turn off and then 'toggle' it would turn back on.  
  --- /feedback ---

- ( ) Off


  --- feedback ---
No. 'Toggle' means 'flip the switch' or to change state from the current one. Since the light bulb was off before it toggled... what would it be now?
  --- /feedback ---

- (x) There's no way to tell
'Toggle' means 'flip the switch' or to change state from the current one. Since the light bulb was off before it toggled... what would it be now?

  --- feedback ---

  --- /feedback ---

- ( ) 


  --- feedback ---

  --- /feedback ---

--- /choices ---

--- /question ---
