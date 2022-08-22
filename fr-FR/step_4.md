## Allumer ta luciole

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dans cette étape, tu utiliseras des fils de liaison pour connecter une LED avec une résistance à ton Raspberry Pi Pico et écrire du code pour l'allumer. 
</div>
<div>
![Le Raspberry Pi Pico avec deux fils de liaison reliés à une LED jaune.](images/firefly-on.jpg){:width="300px"}
</div>
</div>

--- task ---

Assure-toi que tu as une LED connectée à une résistance et deux fils de liaison prise-prise. La couleur des fils de liaison n'a pas d'importance, ils font tous la même chose.

Les lucioles sont généralement jaunes, orange ou vertes, mais tu peux choisir la couleur de ton choix.

![Une LED connectée à des fils de liaison avec une résistance sur la longue branche positive.](images/led-resistor.jpeg)

Une **résistance** contrôle le courant qui circule dans un circuit. Cela permet d'éviter que la LED ne s'éteigne et de la faire durer plus longtemps.

Si ta LED n'a pas de fils de liaison ni de résistance, tu peux les ajouter :

[[[led-resistor-electrical-tape]]]

[[[led-resistor-solder-heat-shrink]]]

--- /task ---

Un Raspberry Pi Pico a **40 broches** sur sa carte. **Pins** te permettent de connecter des composants externes au Raspberry Pi Pico.

--- task ---

Explore ton Raspberry Pi Pico et trouve la broche étiquetée **GP13**. Tu remarqueras qu'il y a des étiquettes pour chaque broche sur la face **inférieure** du Raspberry Pi Pico.

![Photo du Raspberry Pi Pico de dessous avec GP13 en surbrillance.](images/gp13-pico.png)

--- /task ---

--- task ---

**Connecte** le fil de liaison qui est attaché à la patte positive de la LED (celle avec la résistance) à la broche **GP13**. Pousse-le jusqu'à ce que le plastique noir rencontre la base de l'en-tête.

**Connecte** le fil de liaison qui est attaché à la patte négative au **GND** (masse), en dessous de **GP13**. Cela complète le circuit, permettant au courant électrique de circuler lorsque ton code te l'indique.

![Un schéma du Raspberry Pi Pico avec une LED jaune connectée à GND et à GP13 via une résistance.](images/pico_led_13_bb.png)

--- /task ---

--- task ---

Dans la dernière étape, tu as utilisé `pico_led` pour allumer la LED sur le Raspberry Pi Pico. Pour ajouter tes propres LED, tu dois `import` `LED` from `picozero`.

Ajoute `, LED` à la fin de la liste d'importation sur la **ligne 1**. Ensuite, mets ta luciole LED sur **GP13** et entre le code pour l'allumer.

Entre le code pour allumer ta luciole :

--- code ---
---
language: python
filename: luciole.py
line_numbers: true
line_number_start: 1
line_highlights: 1,8-9
---
from picozero import pico_led, LED
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

luciole = LED(13) # Utiliser GP13
luciole.on()
--- /code ---

**Astuce :** Pour importer plusieurs éléments, sépare-les par des virgules `,`.

--- /task ---

--- task ---

**Test :** exécute ton code pour voir ta luciole LED s'allumer.

![LED jaune attachée au GP13 et allumée.](images/firefly-on.jpg)

**Déboguer** :

--- collapse ---
---
title: Mon code ne s'exécute pas
---

Si ton code ne s'exécute pas :
+ Corrige toutes les erreurs dans ton code. La LED sur le Raspberry Pi Pico clignotera si ton code s'exécute avec succès.

--- /collapse ---

--- collapse ---
---
title: Ma luciole LED ne s'allume pas
---

Si ta luciole LED ne s'allume pas :
+ Vérifie que ta LED a le côté négatif (plus court, plat) attaché à **GND** et le côté positif (plus long, avec résistance) attaché à **GP13**
+ Assure-toi que tous les joints font une bonne connexion
+ Essaie une autre LED

--- /collapse ---

--- /task ---

--- task ---

**Facultatif :** Découpe des ailes dans du ruban adhésif plié et colle-les sur ta LED. Le ruban invisible fonctionne bien.

![Luciole LED avec ailes en ruban adhésif.](images/firefly-wings.jpg)

--- /task ---
