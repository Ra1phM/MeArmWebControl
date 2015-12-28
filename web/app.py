#!/usr/bin/env python
from flask import Flask, render_template, Response
import servo

app = Flask(__name__)

GRIP 		= 1 # GPIO 17
SHOULDER 	= 2 # GPIO 22
ELBOW 		= 4 # GPIO 18
HIP			= 5 # GPIO 23

# Routes

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<arm_command>")
def perform_arm_command(arm_command):
	# Choose the direction of the request
	if arm_command == 'gripopen':
		servoController.setAngle(GRIP, -90)
        
	elif arm_command == 'gripclose':
		servoController.setAngle(GRIP, 10)

	elif arm_command == 'elbowup':
		servoController.incAngle(ELBOW, -10)

	elif arm_command == 'elbowdown':
		servoController.incAngle(ELBOW, 10)

	elif arm_command == 'shoulderback':
		servoController.incAngle(SHOULDER, -10)

	elif arm_command == 'shoulderforward':
		servoController.incAngle(SHOULDER, 10)

	elif arm_command == 'hipleft':
		servoController.incAngle(HIP, 10)

	elif arm_command == 'hipright':
		servoController.incAngle(HIP, -10)

	return arm_command

if __name__ == '__main__':
	servoController = servo.ServoController()

	servoController.setAngle(GRIP, -90)
	servoController.setAngle(ELBOW, -20)
	servoController.setAngle(SHOULDER, -40)
	servoController.setAngle(HIP, -25)

	app.run(host='0.0.0.0', debug=True)


