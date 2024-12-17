
--- question ---
---
legend: Question 3 of 3
---

In your project, you coded a firefly LED and a switch made from two jumper wires.

What happens when the jumper wires are connected to close the switch?

--- code ---
---
language: python filename: firefly.py
line_numbers: false
---
firefly = LED(13) switch = Switch(18)

while True: if switch.is_closed: firefly.on() sleep(0.5) firefly.off() sleep(2.5) else: firefly.off() sleep(0.1) --- /code --- --- choices ---

- ( ) The LED firefly will blink once and then turn off until you connect the switch again.

  --- feedback ---

Not quite, the code to blink the LED is in a while loop that keeps checking whether the switch is closed.

  --- /feedback ---

- ( ) The LED firefly will remain off.


  --- feedback ---

Try again. If the switch is closed then the `switch.is_closed` condition will be true. This will run the block of code to blink the firefly.

  --- /feedback ---

- (x) The LED firefly will blink on and off until you disconnect the switch.


  --- feedback ---

Well done! Your LED firefly will continue to blink for as long as the switch is closed.

  --- /feedback ---

--- /choices ---

--- /question ---
