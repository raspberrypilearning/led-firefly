
--- question ---
---
legend: Question 3 sur 3
---

Dans ton projet, tu as codé une LED luciole et un interrupteur constitué de deux fils.

Que se passe-t-il lorsque les fils sont connectés pour fermer l'interrupteur ?

--- code ---
---
language: python filename: firefly.py
line_numbers: false
---
firefly = LED(13) switch = Switch(18)

while True: if switch.is_closed: firefly.on() sleep(0.5) firefly.off() sleep(2.5) else: firefly.off() sleep(0.1) --- /code --- --- choices ---

- ( ) La luciole LED clignotera une fois puis s'éteindra jusqu'à ce que tu reconnectes l'interrupteur.

  --- feedback ---

Pas tout à fait, le code pour faire clignoter la LED est dans une boucle while qui vérifie en permanence si l'interrupteur est fermé.

  --- /feedback ---

- ( ) La luciole LED restera éteinte.


  --- feedback ---

Réessaie. Si l'interrupteur est fermé, la condition `switch.is_closed` sera vraie. Cela exécutera le bloc de code pour faire clignoter la luciole.

  --- /feedback ---

- (x) La luciole LED clignotera jusqu'à ce que tu déconnectes l'interrupteur.


  --- feedback ---

Bien joué ! Ta luciole LED continuera à clignoter tant que l'interrupteur est fermé.

  --- /feedback ---

--- /choices ---

--- /question ---
