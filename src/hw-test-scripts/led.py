#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

#Sets GPIO to board mode, using physical pin numbering
GPIO.setmode(GPIO.BOARD)
#Stops warnings being printed to console
GPIO.setwarnings(False)

#LED Setup
led = 8 # connected to pin 8
GPIO.setup(led, GPIO.OUT) # Set to output

def blinkLED(noOfTimes, speed):
    try:
        print("Flashing LED " + str(noOfTimes) + " times")
	for i in range(1, noOfTimes + 1):
	    GPIO.output(led, 1) #on
            print("  " + str(i) + ": on")
            sleep(speed) # Wait 1 second
            print("  " + str(i) + ": off")
	    GPIO.output(led, 0) #off
            sleep(speed) # Wait 1 second
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
#END blinkLED()

def solidLED(state):
    try:
        GPIO.output(led, state)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()

blinkLED(6, 0.1)
solidLED(1)
sleep(2)
solidLED(0)

GPIO.cleanup()