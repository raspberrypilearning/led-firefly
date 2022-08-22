## Ajouter un interrupteur

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il est utile de pouvoir contrôler le moment où ta luciole LED commence à clignoter et de pouvoir l'éteindre depuis l'appareil. 
</div>
<div>
![Les extrémités broche-prise de deux fils de liaison sont connectées ensemble. Cela fait clignoter la luciole.](images/firefly-switch.gif){:width="300px"}
</div>
</div>

Le Raspberry Pi Pico peut détecter lorsqu'une entrée est connectée entre **GND** et l'une des broches GP.

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Un <span style="color: #0faeb0">interrupteur</span> est un composant électrique qui peut être **fermé** pour permettre au courant électrique de circuler et **ouvert** pour empêcher le courant électrique de circuler. Un <span style="color: #0faeb0">bouton</span> est aussi une sorte d'interrupteur qui établit une connexion lorsqu'il est **pressé**.
</p>

Le type d'interrupteur le plus simple est constitué de deux fils de liaison qui peuvent être connectés ensemble pour fermer l'interrupteur ou séparés pour ouvrir l'interrupteur.

[[[pin-socket-jumper-wires]]]

--- task ---

Trouve un fil de liaison broche-prise et un fil de liaison prise-prise, les couleurs n'ont pas d'importance.

![Un fil de liaison broche-prise et un fil de liaison prise-prise.](images/jumper-wires.jpg)

--- /task ---

--- task ---

**Connecte** un fil à **GP18** et l'autre à **GND**. Peu importe quel fil tu connectes à quelle broche.

![Deux fils sont attachés aux broches GP18 et GND du Raspberry Pi Pico.](images/switch-wiring-diagram.png)

--- /task ---

--- task ---

Pour ajouter des interrupteurs, tu dois `import Switch` à partir de la bibliothèque `picozero`.

Ajoute `, Switch` à la fin de la liste d'importation sur la **ligne 1**. Ensuite, mets ton `interrupteur` sur **GP18** :

--- code ---
---
language: python
filename: luciole.py
line_numbers: true
line_number_start: 1
line_highlights: 1, 9
---
from picozero import pico_led, LED, Switch
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

luciole = LED(13) # Utiliser GP13
interrupteur = Switch(18) # Utiliser GP18

--- /code ---

--- /task ---

Lorsque tu connectes les deux fils de liaison ensemble, cela complète un circuit et permet au Raspberry Pi Pico de détecter que l'interrupteur est fermé.

--- task ---

Ajoute du code pour vérifier `if` ton interrupteur `is_closed` (les fils sont connectés) et ne fais clignoter la luciole que si c'est est fermé :

--- code ---
---
language: python
filename: luciole.py
line_numbers: true
line_number_start: 9
line_highlights: 12-19
---
interrupteur = Switch(18) # Utiliser GP18

while True:
    if interrupteur.is_closed: # Les fils sont connectés
        luciole.on()
        sleep(0.5) # Reste allumé une demi-seconde
        luciole.off()
        sleep(2.5) # Reste éteint pendant 2,5 secondes
    else: # Les fils ne sont pas connectés
        luciole.off()
        sleep(0.1) # Petit délai

--- /code ---

--- /task ---

--- no-print ---

--- task ---

**Test :** Assure-toi que les fils sont **non** connectés, puis exécute ton code.

--- collapse ---

---
title: À quoi t'attends-tu lorsque tu exécutes ton code ?
---

Les fils sont **non** fermés, donc le code dans le bloc `else` s'exécutera. Cela signifie que la LED luciole restera **éteinte**.

--- /collapse ---

Connecte maintenant les fils ensemble. La luciole devrait commencer à clignoter.

![Une animation de la luciole LED s'allume lorsque les fils de liaison sont connectés.](images/firefly-switch.gif)

Débranche les fils et la luciole devrait cesser de clignoter.

--- /task ---

--- /no-print ---

--- print-only ---

--- task ---

**Test :** Assure-toi que les fils sont **non** connectés, puis exécute ton code.

--- collapse ---

---
title: À quoi t'attends-tu lorsque tu exécutes ton code ?
---

Les fils sont **non** fermés, donc le code dans le bloc `else` s'exécutera. Cela signifie que la LED luciole restera **éteinte**.

--- /collapse ---

Connecte maintenant les fils ensemble.

![Le fil broche connecté au fil prise.](images/connected-wires.jpg)

La luciole devrait commencer à clignoter.

Débranche les fils et la luciole devrait cesser de clignoter.

--- /task ---

--- /print-only ---

**Remarque :** La déconnexion des fils n'arrêtera pas immédiatement l'alimentation de la LED luciole. La luciole ne s'éteint que lorsque le code `luciole.off()` s'exécute.

--- task ---

**Facultatif :** Si tu es dans un groupe, tu peux essayer de synchroniser tes lucioles en connectant tes interrupteurs de fil de liaison en même temps.

--- /task ---
