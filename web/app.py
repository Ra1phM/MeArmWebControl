#!/usr/bin/env python

from flask import Flask, render_template, Response
import servo

app = Flask(__name__)

# Todo: Setup Servo
grip = servo.ServoController(17)
grip.setAngle(90)

elbow = servo.ServoController(27)
elbow.setAngle(0)

shoulder = servo.ServoController(22)
shoulder.setAngle(25)

hip = servo.ServoController(23)
hip.setAngle(0)


# Routes

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<arm_command>")
def perform_arm_command(arm_command):
	# Choose the direction of the request
	if arm_command == 'gripopen':
		grip.setAngle(45)
        
	elif arm_command == 'gripclose':
		grip.setAngle(90)

	elif arm_command == 'elbowup':
		elbow.incAngle(10)

	elif arm_command == 'elbowdown':
		elbow.incAngle(-19)

	elif arm_command == 'shoulderback':
		shoulder.incAngle(-10)

	elif arm_command == 'shoulderforward':
		shoulder.incAngle(10)

	elif arm_command == 'hipleft':
		hip.incAngle(-10)

	elif arm_command == 'hipright':
		hip.incAngle(10)

	return arm_command

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)