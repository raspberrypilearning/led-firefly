
--- question ---
---
legend: Vraag 3 van 3
---

In je project heb je een vuurvlieg-LED gecodeerd en een schakelaar gemaakt van twee jumperdraden.

Wat gebeurt er als de jumperdraden zijn aangesloten om de schakelaar te sluiten?

--- code ---
---
language: python
filename: firefly.py
line_numbers: false
---
vuurvlieg = LED(13)
schakelaar = Switch(18)

while True:
    if schakelaar.is_closed:
        vuurvlieg.on()
        sleep(0.5)
        vuurvlieg.off()
        sleep(2.5)
    else:
        vuurvlieg.off()
        sleep(0.1)

--- /code ---
--- choices ---

- ( ) de LED-vuurvlieg knippert één keer en gaat dan uit totdat je de schakelaar weer aansluit.

  --- feedback ---

Niet helemaal, de code om de LED te laten knipperen is in een while-lus die blijft controleren of de schakelaar gesloten is.

  --- /feedback ---

- ( ) de LED-vuurvlieg blijft uit.


  --- feedback ---

Probeer het nog eens. Als de schakelaar gesloten is dan zal de `schakelaar.is_closed` voorwaarde waar zijn. Hierdoor wordt het codeblok uitgevoerd om de vuurvlieg te laten knipperen.

  --- /feedback ---

- ( ) de LED-vuurvlieg knippert aan en uit totdat je de schakelaar loskoppelt.


  --- feedback ---

Goed gedaan! Je LED-vuurvlieg blijft knipperen zolang de schakelaar gesloten is.

  --- /feedback ---

--- /choices ---

--- /question ---
