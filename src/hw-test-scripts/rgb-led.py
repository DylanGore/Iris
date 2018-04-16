#! /usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

debug = True

#Led Declare
redPin = 11
greenPin = 13
bluePin = 15

def setup():
	#Sets GPIO to board mode, using physical pin numbering
	GPIO.setmode(GPIO.BOARD)
	#Stops warnings being printed to console
	GPIO.setwarnings(False)
	GPIO.setup(redPin, GPIO.OUT) # Set to output
	GPIO.setup(greenPin, GPIO.OUT) # Set to output
	GPIO.setup(bluePin, GPIO.OUT) # Set to output

def turnOn(pinNum):
	GPIO.output(pinNum, 1)
	log('Turned on pin: ' + str(pinNum))
	
def turnOff(pinNum):
	GPIO.output(pinNum, 0)
	log('Turned off pin: ' + str(pinNum))

def red():
	turnOn(redPin)
	turnOff(greenPin)
	turnOff(bluePin)
	log('Set RGB to Red')
	
def green():
	turnOff(redPin)
	turnOn(greenPin)
	turnOff(bluePin)
	log('Set RGB to Green')
	
def blue():
	turnOff(redPin)
	turnOff(greenPin)
	turnOn(bluePin)
	log('Set RGB to Blue')
	
	
def log(logMsg):
	if debug:
		print('DEBUG: ' + logMsg)
	
	
def main():
	for i in range(0, 1):
		try:
			turnOff(redPin)
			turnOn(greenPin)
			turnOff(bluePin)
			sleep(1)
		except(KeyboardInterrupt, SystemExit):
			GPIO.cleanup()


	GPIO.cleanup()

setup()
main()
