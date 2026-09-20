# Notes from 2026-09 rebuild
davs2rt

### Pixel controller
* **Reset means factory reset.** 
* * All configuration is lost. 
* * If connector to channel assignment is lost, .fseq files on the SD card will may not work because they use channels that are no longer assigned.
* Use Reboot instead.
* Each factory reset changes the hostname. It assigns new hexadecimal digits in the last 4 spaces. e.g. Falcon_F16V5_5005 becomes Falcon_F16V5_9cf3
* The Wi-Fi configuration is, by design, not saved when you save and reload the configuration.
* Therefore, expect to need to use the wired Ethernet to reload the JSON configuration file. On this float this means climbing into the wheel itself.

### Details

1. Port and starboard are used in the documentation.  If you are in the float, facing the front (where the tow bar is) starboard is to your right, and port is to the left.  

1. Sometimes the pixel controller connections to the light strings are called ports. Where it can cause confusion, call them connectors 

1. The sequence file does not light all the lights on the port face of the wheel.  The current configuration duplicates the starboard channel number to the drive connector that handles the port side of the float.

1. The wheel channels start at 1531, not because they have to in player mode, but because the model combined the base and wheel.

1. The "gift" boxes are numbered. They are numbered in order of the way the Ferris Wheel rotates, which is: top to the rear. It's easy to remember because it helps pass tree branches over the top.  The saved JSON configuration is the definitive mapping of connector to light string. Just know that it is not in a logical order. The web user interface has reasonable names on each port (connector).

1. A very handy test mode is called 'number'.  It lights as many lights as the connector number on the pixel controller.  E.g. connector 9 lights 9 lights.

