## Steek je vuurvlieg aan

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap gebruik je jumperdraden om een LED met een weerstand aan te sluiten op je Raspberry Pi Pico en code te schrijven om het te verlichten. 
</div>
<div>
![De Raspberry Pi Pico met twee aangesloten jumperdraden die verbinden met een gele LED.](Images/firefly-on.jpg){:width="300px"}
</div>
</div>

--- task ---

Zorg ervoor dat er een LED is aangesloten op een weerstand en twee pin-pin jumperdraden. De kleur van de jumperdraden maakt niet uit, ze doen allemaal hetzelfde.

Vuurvliegjes zijn meestal geel, oranje of groen, maar je kunt elke gewenste kleur kiezen.

![Een LED die is aangesloten op jumperdraden met een weerstand op het lange, positieve been.](images/led-resistor.jpeg)

Een **weerstand** regelt de stroom die door een circuit loopt. Dit beschermt de LED tegen doorbranden en zorgt ervoor dat deze langer meegaat.

Als je LED geen jumperdraden en een weerstand heeft, dan kun je ze toevoegen:

[[[led-resistor-electrical-tape]]]

[[[led-resistor-solder-heat-shrink]]]

--- /task ---

Een Raspberry Pi Pico heeft **40 pinnen** op zijn bord. **Pinnen** stellen je in staat om externe componenten aan te sluiten op de Raspberry Pi Pico.

--- task ---

Bekijk je Raspberry Pi Pico goed en zoek de pin met het label **GP13**. Je zult zien dat er labels zijn voor elke pin aan de **onderkant** kant van de Raspberry Pi Pico.

![Foto van de Raspberry Pi Pico van onderen met GP13 gemarkeerd.](images/gp13-pico.png)

--- /task ---

--- task ---

**Sluit de jumperdraad aan** die is bevestigd aan de positieve poot van de LED (die met de weerstand) om **GP13** vast te zetten. Druk erop totdat het zwarte plastic de onderkant van de kop raakt.

**Verbind** de jumperdraad die is bevestigd aan de negatieve poot met de **GND** (aarde), onder **GP13**. Dit voltooit het circuit, waardoor elektrische stroom kan stromen wanneer dit wordt aangegeven door de code.

![Een diagram van de Raspberry Pi Pico met een gele LED die is aangesloten op GND en op GP13 via een weerstand.](images/pico_led_13_bb.png)

--- /task ---

--- task ---

In de laatste stap heb je `pico_led` gebruikt om de LED op de Raspberry Pi Pico te laten branden. Om je eigen LED's toe te voegen, moet je `LED` `importeren` van `picozero`.

Voeg `, LED` toe aan het einde van de importlijst op **regel 1**. Stel vervolgens je vuurvlieg-LED in op **GP13** en voer de code in om deze in te schakelen.

Voer de code in om je vuurvlieg te verlichten:

--- code ---
---
language: python
filename: firefly.py
line_numbers: true
line_number_start: 1
line_highlights: 1,8-9
---
from picozero import pico_led, LED
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

vuurvlieg = LED(13) # Gebruik GP13
vuurvlieg.on()
--- /code ---

**Tip:** om meerdere items te importeren, scheid ze dan met komma's `,`.

--- /task ---

--- task ---

**Test:** Voer je code uit om te zien dat de LED-vuurvlieg gaat branden.

![De gele LED is aangesloten op de GP13 en brandt.](images/firefly-on.jpg)

**Fouten oplossen**:

--- collapse ---
---
title: Mijn code wordt niet uitgevoerd
---

Als je code niet wordt uitgevoerd:
+ Los eventuele fouten in de code op. De LED op de Raspberry Pi Pico zal knipperen als je code succesvol wordt uitgevoerd.

--- /collapse ---

--- collapse ---
---
title: Mijn LED-vuurvlieg brandt niet
---

Als je LED-vuurvlieg niet oplicht:
+ Controleer of de negatieve (kortere, vlakke) zijde van de LED is bevestigd aan **GND** en de positieve (langere, met weerstand) zijde is bevestigd aan **GP13**
+ Zorg ervoor dat alle verbindingen goed contact maken
+ Probeer een andere LED

--- /collapse ---

--- /task ---

--- task ---

**Optioneel:** Snijd enkele vleugels uit omgevouwen plakband en plak ze aan je LED. Onzichtbare tape werkt goed.

![LED-vuurvlieg met plakbandvleugels.](images/firefly-wings.jpg)

--- /task ---
