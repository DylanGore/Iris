#! /usr/bin/python3

import RPi.GPIO as GPIO

debug = True

# Logging helper function
def log(logMsg):
	if debug:
		print('[camera-client] DEBUG: ' + logMsg)


# RPi GPIO setup helper function
def setupGPIOBoard():
    #Sets GPIO to board mode, using physical pin numbering
	GPIO.setmode(GPIO.BOARD)
	#Stops warnings being printed to console
	GPIO.setwarnings(False)

# Set pin as GPIO ouput
def setupGPIOOutput(pin):
    GPIO.setup(pin, GPIO.OUT)

# Set pin as GPIO input
def setupGPIOInput(pin):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Get GPIO input state
def getGPIOInput(pin):
    return GPIO.input(pin)

# Cleanup GPIO to avoid issues with future use
def cleanupGPIO():
    GPIO.cleanup()
    log('HELPER - GPIO cleanup')