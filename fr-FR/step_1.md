## You will make

Dans ce projet, tu utiliseras un Raspberry Pi Pico pour créer une luciole LED qui clignote selon un motif particulier, tout comme les lucioles dans la nature, et tu connecteras un interrupteur pour contrôler la lumière.

[[[flashing-light-warning]]]

<div style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;display: flex; flex-wrap: wrap'>
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Un <span style="color: #0faeb0">microcontrôleur</span> est un petit dispositif informatique qui peut exécuter du code et interagir avec des <span style="color: #0faeb0">composants électroniques</span> (tels que des boutons et des voyants). Il est généralement conçu pour effectuer une seule tâche et n'a pas de <span style="color: #0faeb0">système d'exploitation</span>. 
Le Raspberry Pi Pico est un microcontrôleur à faible coût qui peut être utilisé par les débutants et peut également être utilisé par des experts pour développer des produits électroniques.
</div>
<div>
![Un dessin d'une main tenant un Raspberry Pi Pico.](images/pico-hand.png){:width="300px"}
</div>
</div>

<br/>
Tu vas :

+ Découvrir le **microcontrôleur** Raspberry Pi Pico
+ Connecter une LED et un interrupteur constitué de fils de liaison aux broches d'un **Raspberry Pi Pico**
+ Programmer le Raspberry Pi Pico en utilisant **MicroPython** et Thonny

--- no-print ---

--- task ---

Cet exemple montre une LED qui clignote pour imiter une vraie luciole ! Peux-tu repérer le motif répétitif dans les clignotements ?

![Une animation de la LED luciole clignotante allumée et éteinte.](images/firefly-blink.gif){:width="300px"}

--- /task ---

--- /no-print ---

--- print-only ---

--- task ---

Cet exemple montre une luciole LED. Ta LED clignotera pour imiter une vraie luciole !

![Une LED avec du ruban adhésif collé dessus pour former des ailes. Il y a deux fils de liaison connectés à la LED, l'un avec une résistance maintenue en place par du ruban électrique.](images/showcase_static.png)

--- /task ---

--- /print-only ---

Pour mener à bien ce projet, tu auras besoin de :

**Matériel informatique**

Tu peux acheter tout le matériel requis pour ce projet et les autres projets du parcours à partir de la [boutique en ligne Pimoroni.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

If you already have a Raspberry Pi Pico, you can purchase the electronic components you need for this project and the other projects in the path from [The Kitronik web store.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack)

+ Un Raspberry Pi Pico avec des broches soudées dessus
+ Un câble de **données** USB A vers micro USB
+ 1 × LED jaune (ou n'importe quelle couleur que tu préfères)
+ 1 × résistance 100Ω (toute résistance de 75Ω à 220Ω fonctionnera)
+ 1 × fil de liaison broche-prise
+ 3 x fils de liaison prise-prise
+ Facultatif : ruban adhésif, le ruban invisible fonctionne mieux

[[[pin-socket-jumper-wires]]]

You can [prepare your LED](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} in advance by attaching it to a resistor and jumper wires before starting the project.

**Software**

+ Thonny : ce projet peut être réalisé à l'aide de l'éditeur Thonny Python, qui peut être installé sur un ordinateur Linux, Windows ou Mac

[[[thonny-install]]]

[[[change-theme-thonny]]]

![](http://code.org/api/hour/begin_rp_ledfirefly.png)
