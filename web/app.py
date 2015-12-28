#!/usr/bin/env python
from flask import Flask, render_template, Response
import servo

app = Flask(__name__)

# Todo: Setup Servo
# grip = servo.ServoController(17)
# grip.setAngle(90)

# elbow = servo.ServoController(27)
# elbow.setAngle(0)

# shoulder = servo.ServoController(22)
# shoulder.setAngle(25)

# hip = servo.ServoController(23)
# hip.setAngle(0)

servo = servo.ServoController()

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
		servo.setAngle(GRIP, 45)
        
	elif arm_command == 'gripclose':
		servo.setAngle(GRIP, 90)

	elif arm_command == 'elbowup':
		servo.incAngle(ELBOW, 10)

	elif arm_command == 'elbowdown':
		servo.incAngle(ELBOW, -19)

	elif arm_command == 'shoulderback':
		servo.incAngle(SHOULDER, -10)

	elif arm_command == 'shoulderforward':
		servo.incAngle(SHOULDER, 10)

	elif arm_command == 'hipleft':
		servo.incAngle(HIP, -10)

	elif arm_command == 'hipright':
		servo.incAngle(HIP, 10)

	return arm_command

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)