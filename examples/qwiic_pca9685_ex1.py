import qwiic_pca9685
import time
import math
import sys

def runExample():

	print("\nSparkFun BME280 Sensor  Example 1\n")
	mySensor = qwiic_pca9685.QwiicPCA9685()

	if mySensor.isConnected() == False:
		print("The Qwiic PCA9685 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySensor.begin()
  
	# Sets PWM Frequency to 50 Hz
	mySensor.set_pre_scale(50)
  
	# Sets start time of PWM pulse on Channel 0 to 0s
	mySensor.set_channel_word(0, 1, 0)


	while True:
		# Increments start time of PWM pulse on Channel 0 to i (1ms to 2ms)
		for i in range(205, 410):
			fun.set_channel_word(0, 0, i)
			# Delay .05 s
			time.sleep(.05)

		# Decrements start time of PWM pulse on Channel 0 to i (2ms to 1ms)
		for i in range(410, 205, -1):
			fun.set_channel_word(0, 0, i)
			# Delay .05 s
			time.sleep(.05)
		
		time.sleep(1)