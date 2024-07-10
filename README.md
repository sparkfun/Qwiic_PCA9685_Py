Qwiic_PCA9685_Py
==============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-pca9685/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun_qwiic_pca9685.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_PCA9685_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_PCA9685_Py.svg" /></a>
	<a href="https://qwiic-pca9685-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-pca9685-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_PCA9685_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>
	
</p>

<img src="https://cdn.sparkfun.com/assets/parts/1/3/8/2/7/15316-SparkFun_Servo_pHAT_for_Raspberry_Pi-01b.jpg"  align="right" width=300 alt="SparkFun Servo pHAT for the Raspberry Pi">

Python module for the PCA9685 PWM controller, which is part of the [SparkFun Servo pHAT for Raspberry Pi](https://www.sparkfun.com/products/15316) and [SparkFun Pi Servo HAT](https://www.sparkfun.com/products/14328)

This package should be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py). New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents
* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The qwiic PCA9685 Python package current supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)
<!-- Platforms to be tested
* [NVidia Jetson Nano](https://www.sparkfun.com/products/15297)
* [Google Coral Development Board](https://www.sparkfun.com/products/15318)
-->

Dependencies 
---------------
This package depends on the qwiic I2C driver: [Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun qwiic PCA9685 module documentation is hosted at [ReadTheDocs](https://qwiic-pca9685-py.readthedocs.io/en/latest/?)

Installation
-------------

### PyPi Installation
This repository is hosted on PyPi as the [sparkfun-qwiic-pca9685](https://pypi.org/project/sparkfun-qwiic-pca9685/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-pca9685
```
For the current user:

```sh
pip install sparkfun-qwiic-pca9685
```

### Local Installation
To install, make sure the `setuptools` package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_pca9685-<version>.tar.gz
  
```
Example Use
 ---------------
See the examples directory for more detailed use examples.

```python
import qwiic_pca9685
import time
import math
import sys

def runExample():

	print("\nSparkFun PCA9685 Example 1\n")
	mySensor = qwiic_pca9685.QwiicPCA9685()

	if mySensor.is_connected() == False:
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
			time.sleep(.1)

		# Decrements start time of PWM pulse on Channel 0 to i (2ms to 1ms)
		for i in range(410, 205, -1):
			fun.set_channel_word(0, 0, i)
			# Delay .05 s
			time.sleep(.1)
		
		time.sleep(1)
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
