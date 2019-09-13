#-----------------------------------------------------------------------
# SparkFun Pi Servo Hat Python Library
#-----------------------------------------------------------------------
#
# Written by  SparkFun Electronics, June 2019
# Author: Wes Furuya
#
# Compatibility:
#     * Original: https://www.sparkfun.com/products/14328
#     * v2: https://www.sparkfun.com/products/15316
# 
# Do you like this library? Help support SparkFun. Buy a board!
# For more information on Pi Servo Hat, check out the product page
# linked above.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http:www.gnu.org/licenses/>.
#
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#==================================================================================
#
# pylint: disable=line-too-long, bad-whitespace, invalid-name

"""
pi_servo_hat
===============
Python module for the [SparkFun Pi Servo HAT](https://www.sparkfun.com/products/14328) and [SparkFun Servo pHAT for Raspberry Pi](https://www.sparkfun.com/products/15316)
This package should be used in conjunction with the sparkfun_pca9685 package.
"""
#-----------------------------------------------------------------------------


# Load Necessary Modules:
import time						# Time access and conversion package
import math						# Basic math package
import qwiic_pca9685					# PCA9685 LED driver package (used on Pi Servo pHAT)

# Device Name:
_DEFAULT_NAME = "Pi Servo HAT"


# Device Address:
# Some devices have multiple available addresses - this is a list of
# these addresses.
# NOTE: The first address in this list is considered the default I2C
# address for the device.
#
# Currently, the Pi Servo Hat (original and v2), the I2C address is
# fixed at 0x40. In the future, should this option become available,
# users will only need to modify the list below.

# Fixed Address:
_AVAILABLE_I2C_ADDRESS = [0x40]

# Full List:
#_AVAILABLE_I2C_ADDRESS = list(range(0x40,0x7F+1))					# Full Address List
#_AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(acAddr)		# Exclude All Call
#_AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_1)	# Exclude Sub Addr 1
#_AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_2)	# Exclude Sub Addr 2
#_AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_3)	# Exclude Sub Addr 3

# Default Servo Frequency:
_DEFAULT_SERVO_FREQUENCY = 200	# Hz

class PiServoHat(object):

	# Constructor

	#----------------------------------------------
	# Device Name:
	device_name = _DEFAULT_NAME
	
	#----------------------------------------------
	# Available Addresses:
	available_addresses = _AVAILABLE_I2C_ADDRESS
	# available_addresses = SparkFunPCA9685.available_addresses

	#----------------------------------------------
	# Available Channels:
	available_pwm_channels = QwiicPCA9685._AVAILABLE_PWM_CHANNELS

	# Special Use Addresses:
	gcAddr = 0x00 		# General Call address for software reset
	acAddr = 0x70		# All Call address- used for modifications to multiple PCA9685 chips
						# reguardless of thier I2C address set by hardware pins (A0 to A5).
	subAddr_1 = 0x71	# 1110 001X or 0xE2 (7-bit)
	subAddr_2 = 0x72	# 1110 010X or 0xE4 (7-bit)
	subAddr_3 = 0x74	# 1110 100X or 0xE8 (7-bit)

	# _AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(acAddr)		# Exclude All Call
	# _AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_1)	# Exclude Sub Addr 1
	# _AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_2)	# Exclude Sub Addr 2
	# _AVAILABLE_I2C_ADDRESS = _AVAILABLE_I2C_ADDRESS.remove(subAddr_3)	# Exclude Sub Addr 3

	def __init__(self, address=None, i2c_driver=None):
		# Initialization
		piservohat = QwiicPCA9685(address=None, i2c_driver=None)

		self.set_pwm_frequency(_DEFAULT_SERVO_FREQUENCY)
		
		# Begin operation
		return piservohat.begin()

	#----------------------------------------------
	# get PWM Frequency
	def get_pwm_frequency(self):
		
		# Get pre-scale value (determines PWM frequency)
		prescale = piservohat.get_pre_scale()

		# Calculate frequency based off internal clock frequency (default)
		self.frequency = float((prescale +1) * 4096/(25*10^6))

		return self.frequency

	#----------------------------------------------
	# Set PWM Frequency
	def set_pwm_frequency(self, frequency):
		
		if piservohat.set_pre_scale(frequency) == True:
			self.frequency = frequency
			return True
		else:
			return False


	def move_servo_position(self, channel, position, speed = None):
		"""
		Moves servo to specified location at a specified speed.
		A 'speed' of 'None', changes the immediate position and the servo will transition as fast a possible. This is most useful as an extension for a task scheduler to control the transition of multiple servos asynchonously.
		"""
		period = 1 / self.frequency			# seconds
		resolution = period / 4096			# seconds

		m = 1 / 180							# ms/degree

		position_time = (m *position + 1)	# seconds

		delay = 0
		on_value = delay
		off_value = position_time / resolution + delay

		if speed == None:
			# Move servo to position immediately
			piservohat.set_channel_word(channel, 1, on_value)
			piservohat.set_channel_word(channel, 0, off_value)
		else:
			initial_on = get_channel_word(channel, 0)
			initial_off = get_channel_word(channel, 1)

			initial_position = 

			piservohat.set_channel_word(channel, on_off, value = None)




	# def change_duty_cycle(self, channel, duty_cycle):

	# def enableAllChannels():
	# def disableAllChannels():
	# def enableChannel():
	# def disableChannel():