## Allumer la LED Raspberry Pi Pico

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dans cette étape, tu allumeras la petite LED qui se trouve sur le dessus de ton Raspberry Pi Pico. Cela vérifiera que ton Raspberry Pi Pico est correctement configuré.
</div>
<div>
![Un Raspberry Pi Pico avec la LED intégrée qui s'allume puis s'éteint.](images/led-on-off.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">LED</span> signifie diode électroluminescente. Elle utilise l'électroluminescence, c'est-à-dire qu'un matériau s'illumine lorsqu'un courant électrique le traverse. Une LED a deux pattes : une longue et une courte, et doit être connectée dans le bon sens. La plus longue patte est le pôle positif (+) et la plus courte est le pôle négatif (-). Une autre façon de vérifier si une patte est positive ou négative consiste à utiliser ton doigt pour trouver le côté plat de l'ampoule LED. Le côté plat est du même côté que la patte négative.
</p>

--- task ---

Regarde ton Raspberry Pi Pico et trouve la petite LED à côté du connecteur USB.

![Une photo du Raspberry Pi Pico avec la LED en surbrillance.](images/pico-led.jpg){:width="200px"}

--- /task ---

--- task ---

Crée un nouveau fichier dans Thonny en cliquant sur **Fichier** > **Nouveau** dans la barre de menu supérieure. Un espace de travail vide s'ouvrira.

--- /task ---

Dans la dernière étape, tu as installé la bibliothèque `picozero`. Cette bibliothèque te permet de programmer des composants électroniques qui sont attachés à un Raspberry Pi Pico. En haut de ton code, tu devras importer les éléments dont tu as besoin à partir de la bibliothèque `picozero`.

--- task ---

Tape le code suivant dans le volet principal de l'éditeur dans Thonny :

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---
from picozero import pico_led 

pico_led.on()

--- /code ---

--- /task ---

--- task ---

Choisis **Fichier**->**Enregistrer sous**. Thonny te demandera si tu souhaites enregistrer le fichier sur **Cet ordinateur** ou sur le **Raspberry Pi Pico**. Choisis **Cet ordinateur** pour enregistrer ton code sur ton ordinateur.

Choisis un emplacement sur ton ordinateur tel que ton dossier « Documents ». Nomme ton fichier `luciole.py`.

![Une capture d'écran d'une fenêtre avec deux options. L'utilisateur peut sélectionner l'appareil "Cet ordinateur" ou "Raspberry Pi Pico". "Cet ordinateur" est mis en surbrillance.](images/save-on-computer.png)

--- /task ---

--- task ---

**Test :** Thonny a un bouton de lecture vert avec un petit triangle blanc à l'intérieur. Appuyer sur ce bouton te permet d'exécuter ton code.

+ Appuie sur le bouton de lecture

+ Vérifie que la petite LED du Raspberry Pi Pico s'allume

![Un Raspberry Pi Pico avec la LED intégrée allumée.](images/led-on.jpg){:width="300px"}

--- /task ---

--- task ---

**Déboguer:**

--- collapse ---
---
title: Le bouton exécuter est masqué
---

Si tu ne vois pas de bouton exécuter en vert (il est grisé) :
+ Clique sur le bouton rouge **STOP**
+ Vérifie que ton Raspberry Pi Pico est connecté à ton ordinateur avec un câble USB
+ Clique sur **MicroPython (Raspberry Pi Pico)** dans le coin inférieur droit de Thonny pour te reconnecter
+ Débranche ton câble USB puis rebranche-le

--- /collapse ---

--- collapse ---
---
title: Thonny dit qu'il y a une erreur dans mon code
---

Vérifie très attentivement ton code et assure-toi qu'il correspond à l'exemple.

--- /collapse ---

--- collapse ---
---
title: Il n'y a pas d'erreur dans mon code mais le voyant ne s'allume pas
---

Essaie un autre câble USB, en t'assurant qu'il s'agit d'un câble USB de **données**. En dernier recours, essaie un autre Raspberry Pi Pico (si tu en as un de rechange).

--- /collapse ---

--- /task ---

La LED restera allumée jusqu'à ce que tu écrives un code pour l'éteindre ou que tu débranches le Raspberry Pi Pico.

--- task ---

Importe `sleep` pour te permettre de mettre ton code en pause. Ajoute du code à la fin de ton script pour mettre en veille pendant une seconde, puis éteindre la LED.

--- code ---
---
language: python
filename: luciole.py
line_numbers: true
line_number_start: 1
line_highlights: 2,5-6
---
from picozero import pico_led
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()
--- /code ---

--- /task ---

--- task ---

**Test :** Clique sur le bouton vert **exécuter**. Thonny enregistrera le fichier sur ton Raspberry Pi Pico puis exécutera le nouveau code.

Vérifie que la LED s'allume puis s'éteint à nouveau. La LED ne s'allume que pendant une seconde, alors assure-toi de bien regarder.

Exécute ton code autant de fois que tu le souhaites.

![Un Raspberry Pi Pico avec la LED intégrée qui s'allume puis s'éteint.](images/led-on-off.gif){:width="300px"}

**Déboguer :**

--- collapse ---
---
title: Thonny dit que le sleep n'est pas défini
---

Ajoute la ligne `from time import sleep`.

--- /collapse ---

--- /task ---
