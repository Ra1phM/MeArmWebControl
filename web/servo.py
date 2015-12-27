from RPIO import PWM
import time
import math


class ServoController:
	def __init__(self, gpio):
		self.gpioPin = gpio
		self.servo = PWM.Servo(pulse_incr_us=1)
		self.angle = 0
		self.pulseWidth = 0

	def setAngle(self, degrees):
		#http://www.raspberrypi.org/forums/viewtopic.php?f=44&t=36572
		pulse = 1520 + (degrees * 400) / 45
		
		if degrees > 90:
			degrees = 90
		elif degrees < -90:
			degrees = -90
		pulse = int(pulse)

		self.servo.set_servo(self.gpioPin, pulse)
		time.sleep(0.1)
		self.angle = degrees
		self.pulseWidth = pulse
		print "angle=%s pulse=%s" % (degrees, pulse)
		
	def incAngle(self, increment):
		self.setAngle(self.angle + increment)
	
	def cleanup(self):
		self.servo.stop_servo(self.gpioPin)

	def setAngleNew(self, degrees, delta=170):
		"""
			Sets angle of servo (approximate).
			:param channel: Channel servo is attached to (0-15)
			:param angle:   off of center, ( -80 through 80)
			:param delta:   Angle changed from past position. Used to calculate
							delay, since rotating thru a larger arc takes longer
							than a shorter arc.
		"""
		delay = max(delta * 0.003, 0.03)        # calculate delay
		zero_pulse = (servoMin + servoMax) / 2  # half-way == 0 degrees
		pulse_width = zero_pulse - servoMin     # maximum pulse to either side 
		pulse = zero_pulse + (pulse_width * degrees / 80)
		print "angle=%s pulse=%s" % (degrees, pulse)
		self.servo.set_servo(self.gpioPin, int(pulse/10) * 10)
		time.sleep(delay)  # sleep to give the servo time to do its thing
		self.angle = degrees
