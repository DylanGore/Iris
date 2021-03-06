#!/usr/bin/python3

import RPi.GPIO as GPIO
from variables import BUZZER_PIN as buzzPin
from time import sleep
from helper import *

# RPi GPIO Setup
setupGPIOBoard()
setupGPIOOutput(12)

# Activate buzzer when called
def buzz():
    GPIO.output(buzzPin, 1)
    log('BUZZER - On')
    sleep(0.5)
    GPIO.output(buzzPin, 0)
    log('BUZZER - Off')