#! /usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
from helper import *

#Pin Declare
buzzPin = 12

setupGPIOBoard()
setupGPIOOutput(12)

def buzz():
    GPIO.output(buzzPin, 1)
    log('BUZZER - On')
    sleep(0.5)
    GPIO.output(buzzPin, 0)
    log('BUZZER - Off')