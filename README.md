# MeArm WebControl Alpha v0.1 - For Raspberry Pi

**Disclaimer:** This is currently an active work in progress. There can be some tuning done with the ServoBlaster values.

[MeArm][], a little robotic arm, is controlled via a web interface on a Raspberry Pi.

## 0. How it works

A Python ([Flask][]) web server runs in a [Docker][] container on the Raspberry Pi. The Raspberry should preferably have [HypriotOS][Hypriot]. The arm's servos are directly connected to the 5V, Ground (GND) and GPIO pins of the Raspberry board.

## 1. Setup

The next sections go over the details on how the [MeArm][], Raspberry and software must be configured. I assume you know already the basics of the Raspberry and [Docker][].

### 1.1. Pins

First, we must wire up MeArm's servos with the Raspberry Pi. There exists different ways to do it, but here we will simply wire everything directly on the Raspberry Pi.

The control pin of the servos goes to the following respective GPIO pins ([Reference here][RPIPins]):

- Grip     => GPIO 17
- Elbow    => GPIO 18
- Shoulder => GPIO 22
- Hip      => GPIO 23

The Power and Ground pins from all motors can go onto a breadboard and then to the 5V pin and a Ground pin of the Raspberry. (To be validated) Alternatively, you can use a secondary power source to only power up the motors. Just make sure it's 5-6V at 2A.

### 1.2. Software

**Note:** You can connect to your Hypriot powered Raspberry Pi using `pi` user instead of `root`.
**Requirement:** You will need your Pi to have an Internet connection to be able to pull the repository and images for docker.

[Hypriot OS][Hypriot] comes already with `git` installed, so just clone this repository in your home folder:

	git clone https://github.com/Ra1phM/MeArmWebControl.git

Then, change directory and build the image (It will take a few minutes, relax and stretch your legs):

	cd MeArmWebControl
	docker build -t rpi-mearm-wb .

To start the container:

	docker run --device /dev/mem:/dev/mem --privileged -p 80:5000 -ti rpi-mearm-wb /bin/bash

We launched a docker container from the image we create previously. The port 5000 from the Flask app is forwarded to port 80. `-ti` sends us directly in an interactive terminal inside the running container. It is very important to map `/dev/mem` to the container with privileged access, otherwise the container won't be able to control the pins.

Now you are in the container, to run the python app type:

	python app.py

And you are done! You can access the web interface at `http://<IP OF RASPBERRY PI>`



[MeArm]:	http://mearm.com			"MeArm Official Website"
[Flask]:	http://flask.pocoo.org		"Flask Official Webiste"
[Docker]:	http://www.docker.com		"Docker Official Website"
[Hypriot]:	http://blog.hypriot.com		"Hypriot Blog"
[RPIPins]:	http://www.element14.com/community/servlet/JiveServlet/previewBody/68203-102-6-294412/GPIO.png "Raspberry Pi B+ Pins Reference"

