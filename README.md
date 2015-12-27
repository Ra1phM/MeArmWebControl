# MeArm WebControl Alpha v0.1 - For Raspberry Pi

[MeArm][], a little robotic arm, is controlled via a web interface on a Raspberry Pi.

## 0. How it works

A Python ([Flask][]) web server runs in a [Docker][] container on the Raspberry Pi. The Raspberry should preferably have [HypriotOS][]. The arm's servos are directly connected to the 5V, Ground (GND) and GPIO pins of the Raspberry board.

## 1. Setup

The next sections go over the details on how the [MeArm][], Raspberry and software must be configured.

### 1.1. Pins

First, we must wire up MeArm's servos with the Raspberry Pi. There exists different ways to do it, but here we will simply wire everything directly on the Raspberry Pi.

The control pin of the servos goes to the following respective GPIO pins ([Reference here][RPIPins]):

- Grip     => GPIO 17
- Elbow    => GPIO 27
- Shoulder => GPIO 22
- Hip      => GPIO 23

The Power and Ground pins from all motors can go onto a breadboard and then to the 5V pin and a Ground pin of the Raspberry. (To be validated) Alternatively, you can use a secondary power source to only power up the motors. Just make sure it's 5-6V at 2A.

### 1.2. Software

- requires Docker
- Install Servos
- commands
- TODO: Make a script that install it automatically



[MeArm]:	http://mearm.com			"MeArm Official Website"
[Flask]:	http://flask.pocoo.org		"Flask Official Webiste"
[Docker]:	http://www.docker.com		"Docker Official Website"
[Hypriot]:	http://blog.hypriot.com		"Hypriot Blog"
[RPIPins]:	http://www.element14.com/community/servlet/JiveServlet/previewBody/68203-102-6-294412/GPIO.png "Raspberry Pi B+ Pins Reference"

