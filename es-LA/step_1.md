## Lo que harás

En este proyecto, usarás una Raspberry Pi Pico para crear una luciérnaga LED que parpadee siguiendo un patrón específico, como las luciérnagas en la naturaleza, y conectarás un interruptor para controlar la luz.

[[[flashing-light-warning]]]

<div style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;display: flex; flex-wrap: wrap'>
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Un <span style="color: #0faeb0">microcontrolador</span> es un dispositivo de cómputo muy pequeño que puede ejecutar código e interactuar con <span style="color: #0faeb0"> componentes electrónicos</span> (como botones y luces). Por lo general, está diseñado para realizar una sola tarea y no tiene un <span style="color: #0faeb0">sistema operativo</span>. 
La Raspberry Pi Pico es un microcontrolador de bajo costo que pueden usar tanto principiantes como personas expertas para desarrollar productos electrónicos.
</div>
<div>
![Un dibujo de una mano sosteniendo una Raspberry Pi Pico.](images/pico-hand.png){:width="300px"}
</div>
</div>

<br/>
Vas a:

+ Conocer el **microcontrolador** Raspberry Pi Pico
+ Conectar un LED y un interruptor hecho con cables puente a los pines de una **Raspberry Pi Pico**
+ Programar la Raspberry Pi Pico con **MicroPython** y Thonny

--- no-print ---

--- task ---

¡Este ejemplo muestra un LED que parpadea para imitar a una luciérnaga real! ¿Puedes identificar el patrón que se repite en los destellos?

![Una animación del LED de la luciérnaga que se enciende y se apaga.](images/firefly-blink.gif){:width="300px"}

--- /task ---

--- /no-print ---

--- print-only ---

--- task ---

Este ejemplo muestra una luciérnaga LED. ¡Tu LED parpadeará para imitar a una luciérnaga real!

![Un LED con cinta adhesiva pegada para formar alas. Hay dos cables puente conectados al LED, uno con una resistencia sujeta con cinta aislante.](images/showcase_static.png)

--- /task ---

--- /print-only ---

Para completar este proyecto necesitarás:

**Hardware**

Puedes comprar todos los componentes físicos necesarios para este proyecto y los demás proyectos de esta ruta de aprendizaje en la [tienda en línea de Kitronik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Una Raspberry Pi Pico con tiras de pines soldadas
+ Un cable USB A a micro USB de **datos**
+ 1× LED amarillo (o del color que prefieras)
+ 1× resistencia de 100Ω (cualquier resistencia de 75Ω a 220Ω servirá)
+ 1× cable puente pin–receptáculo
+ 3× cables puente receptáculo–receptáculo
+ Opcional: Cinta adhesiva, de preferencia cinta invisible

[[[pin-socket-jumper-wires]]]

Puedes [preparar tu LED](https://projects.raspberrypi.org/es-LA/projects/introduction-to-the-pico){:target="_blank"} con anticipación conectándolo a una resistencia y a cables puente antes de comenzar el proyecto.

**Programas**

+ Thonny – puedes completar este proyecto con el editor de Python Thonny, que se puede instalar en una computadora con Linux, Windows o Mac

[[[thonny-install]]]

[[[change-theme-thonny]]]

![](http://code.org/api/hour/begin_rp_ledfirefly.png)
