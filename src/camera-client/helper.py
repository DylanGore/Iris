#! /usr/bin/python3

import RPi.GPIO as GPIO

debug = True

def log(logMsg):
	if debug:
		print('[camera-client] DEBUG: ' + logMsg)


def setupGPIOBoard():
    #Sets GPIO to board mode, using physical pin numbering
	GPIO.setmode(GPIO.BOARD)
	#Stops warnings being printed to console
	GPIO.setwarnings(False)


def setupGPIOOutput(pin):
    GPIO.setup(pin, GPIO.OUT)


def setupGPIOInput(pin):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getGPIOInput(pin):
    return GPIO.input(pin)

def cleanupGPIO():
    GPIO.cleanup()
    log('HELPER - GPIO cleanup')