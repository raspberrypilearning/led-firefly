## Laat je vuurvlieg knipperen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu zul je je vuurvlieg aan en uit laten knipperen, als een echte vuurvlieg. 
</div>
<div>
![Een animatie van de vuurvlieg-LED die aan en uit knippert.](images/firefly-blink.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Een <span style="color: #0faeb0">vuurvlieg</span> is een soort kever, ook wel een gloeiworm of bliksembeestje genoemd. Ze gebruiken bioluminescentie om te flitsen om zich te identificeren met andere leden van dezelfde soort. Verschillende soorten flitsen in verschillende patronen. 
</p>

--- task ---

Wijzig je code om de vuurvlieg in een `while True:` lus te laten knipperen. De tijden vertegenwoordigen de lichtpatronen van een echte vuurvlieg.

Zorg ervoor dat de code op regel 11–14 inspringt.

**Tip:** in Thonny kun je code inspringen door naar het begin van de regel te gaan en op de <kbd>Tab</kbd> toets te tikken — dit voegt vier spaties in. Thonny zal automatisch code inspringen op basis van de vorige regel wanneer je op <kbd>Enter</kbd> drukt tijdens het typen.

--- code ---
---
language: python filename: firefly.py line_numbers: true line_number_start: 8
line_highlights: 9-14
---
firefly = LED(13) # Use GP13

while True: firefly.on() sleep(0.5) firefly.off() sleep(2.5) --- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om te zien dat het vuur langzaam aan en uit knippert.

![Een animatie van de vuurvlieg-LED die aan en uit knippert.](images/firefly-blink.gif)

**Fouten oplossen:**

+ Los eventuele fouten in je code op, inclusief inspringing
+ Controleer of geen van de aansluitingen naar de LED-vuurvlieg is losgeraakt

--- /task ---