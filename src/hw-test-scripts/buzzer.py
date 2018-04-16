#! /usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

#Sets GPIO to board mode, using physical pin numbering
GPIO.setmode(GPIO.BOARD)
#Stops warnings being printed to console
GPIO.setwarnings(False)

#Buzzer Setup
buzzer = 12 # connected to pin 12
GPIO.setup(buzzer, GPIO.OUT) # Set to output

while True:
    try:
        GPIO.output(buzzer, 1)
        sleep(10)
        GPIO.output(buzzer, 0)
    except(KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
GPIO.cleanup()
