## Faire clignoter ta luciole

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maintenant, tu vas faire clignoter ta luciole, comme une vraie luciole. 
</div>
<div>
![Une animation de la LED luciole qui clignote.](images/firefly-blink.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Une <span style="color: #0faeb0">luciole</span> est une sorte de coléoptère, également appelé ver luisant ou insecte lumineux. Elles utilisent la bioluminescence pour clignoter et s'identifier aux autres membres de la même espèce. Différentes espèces clignotent dans différents modèles. 
</p>

--- task ---

Modifie ton code pour faire clignoter la luciole dans une boucle `while True:`. Les minutages représentent les motifs lumineux d'une vraie luciole.

Assure-toi que le code des lignes 11 à 14 est indenté.

**Astuce :** Dans Thonny, tu peux indenter le code en allant au début de la ligne et en appuyant sur la touche <kbd>Tab</kbd> — cela insérera quatre espaces. Thonny indentera automatiquement le code en fonction de la ligne précédente lorsque tu appuies sur <kbd>Entrée</kbd> lors de la saisie.

--- code ---
---
language: python filename: firefly.py line_numbers: true line_number_start: 8
line_highlights: 9-14
---
firefly = LED(13) # Use GP13

while True: firefly.on() sleep(0.5) firefly.off() sleep(2.5) --- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir la luciole clignoter lentement.

![Une animation de la LED luciole clignotante allumée et éteinte.](images/firefly-blink.gif)

**Déboguer :**

+ Corrige toutes les erreurs dans ton code, y compris l'indentation
+ Vérifie qu'aucune des connexions à ta luciole LED ne s'est desserrée

--- /task ---