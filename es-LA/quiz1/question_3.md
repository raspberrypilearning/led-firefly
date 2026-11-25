
--- question ---
---
legend: Pregunta 3 de 3
---

En tu proyecto, programaste un LED que representa una luciérnaga y un interruptor hecho con dos cables puente.

¿Qué pasa cuando se conectan los cables puente para cerrar el interruptor?

--- code ---
---
language: python
filename: firefly.py
line_numbers: false
---
firefly = LED(13)
switch = Switch(18)

while True:
    if switch.is_closed:
        firefly.on()
        sleep(0.5)
        firefly.off()
        sleep(2.5)
    else:
        firefly.off()
        sleep(0.1)
--- /code ---
--- choices ---

- ( ) La luciérnaga LED parpadeará una vez y luego se apagará hasta que vuelvas a conectar el interruptor.

  --- feedback ---

No exactamente, el código que hace parpadear el LED está dentro de un bucle while que comprueba una y otra vez si el interruptor está cerrado.

  --- /feedback ---

- ( ) La luciérnaga LED permanecerá apagada.


  --- feedback ---

Inténtalo de nuevo. Si el interruptor está cerrado, la condición `switch.is_closed` será verdadera. Esto ejecutará el bloque de código que hace parpadear la luciérnaga.

  --- /feedback ---

- (x) La luciérnaga LED se encenderá y apagará repetidamente hasta que desconectes el interruptor.


  --- feedback ---

¡Bien hecho! Tu luciérnaga LED seguirá parpadeando mientras el interruptor esté cerrado.

  --- /feedback ---

--- /choices ---

--- /question ---
