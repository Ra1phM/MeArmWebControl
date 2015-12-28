import time
import os

servos = {}

class ServoController:

	def __init__(self):
		os.system('ServoBlaster/user/servod')

	def setAngle(self, servo_id, degrees):

		if degrees > 90:
			degrees = 90
		elif degrees < -90:
			degrees = -90
			
		#http://www.raspberrypi.org/forums/viewtopic.php?f=44&t=36572
		pulse = 1520 + (degrees * 400) / 45

		os.system("echo %d=%d > /dev/servoblaster" % (servo_id, pulse/10))
		time.sleep(0.1)
		servos[servo_id] = degrees
		#print "angle=%s pulse=%s" % (degrees, pulse)
		return servos[servo_id]
		
	def incAngle(self, servo_id, increment):
		angle = servos.get(servo_id, 0)
		return self.setAngle(servo_id, angle + increment)

	def clean_up(self):
		print "cleaning up"
		os.system('sudo killall servod')