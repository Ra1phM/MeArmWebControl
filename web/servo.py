# The MIT License (MIT)

# Copyright (c) 2015 ForToffee

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import os

servos = {}

class ServoController:

	def __init__(self):
		if os.system('pgrep servod') == 256: # pgrep returns 256 if process doesn't exists
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
		print "angle=%s pulse=%s" % (degrees, pulse)
		return servos[servo_id]
		
	def incAngle(self, servo_id, increment):
		angle = servos.get(servo_id, 0)
		return self.setAngle(servo_id, angle + increment)

	def clean_up(self):
		print "cleaning up"
		os.system('sudo killall servod')