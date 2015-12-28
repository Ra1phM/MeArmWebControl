#!/usr/bin/env python
from flask import Flask, render_template, Response
import servo

app = Flask(__name__)

GRIP 		= 1 # GPIO 17
ELBOW 		= 2 # GPIO 18
SHOULDER 	= 4 # GPIO 22
HIP			= 5 # GPIO 23

# Routes

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<arm_command>")
def perform_arm_command(arm_command):
	# Choose the direction of the request
	if arm_command == 'gripopen':
		servoController.setAngle(GRIP, 45)
        
	elif arm_command == 'gripclose':
		servoController.setAngle(GRIP, 90)

	elif arm_command == 'elbowup':
		servoController.incAngle(ELBOW, 10)

	elif arm_command == 'elbowdown':
		servoController.incAngle(ELBOW, -19)

	elif arm_command == 'shoulderback':
		servoController.incAngle(SHOULDER, -10)

	elif arm_command == 'shoulderforward':
		servoController.incAngle(SHOULDER, 10)

	elif arm_command == 'hipleft':
		servoController.incAngle(HIP, -10)

	elif arm_command == 'hipright':
		servoController.incAngle(HIP, 10)

	return arm_command

if __name__ == '__main__':
	servoController = servo.ServoController()

	servoController.setAngle(GRIP, 90)
	servoController.setAngle(ELBOW, 0)
	servoController.setAngle(SHOULDER, 25)
	servoController.setAngle(HIP, 0)

	app.run(host='0.0.0.0', debug=True)


