#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

debug = True

#Pin Declare
btnPin = 16 # connected to pin 16

def setup():
	#Sets GPIO to board mode, using physical pin numbering
	GPIO.setmode(GPIO.BOARD)
	#Stops warnings being printed to console
	GPIO.setwarnings(False)
	
	GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
def log(logMsg):
	if debug:
		print('DEBUG: ' + logMsg)
	
	
def main():
	try:
		while True:
			btnInput = GPIO.input(btnPin)
			if btnInput == False:
				log('Button Pressed!')
				sleep(0.2)
				
	except(KeyboardInterrupt, SystemExit):
		GPIO.cleanup()
		
	GPIO.cleanup()

setup()
main()
