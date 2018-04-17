#! /usr/bin/python3

import RPi.GPIO as GPIO
import buzzer as buzzer
import subprocess as sp
from time import sleep
from helper import *
import camera 
import api

camera_running = False
camera_time = 6

#Pin Declare
mtnPin = 16 # connected to pin 16

setupGPIOBoard()
setupGPIOInput(mtnPin)
	
try:
	while True:
		if camera_running:
			log('MAIN - Camera is running for ' + str(camera_time)  + ' seconds')
			camera.runCamera(camera_time)
			log('MAIN - Camera is finished running')
			camera_running = False

		mtnInput = getGPIOInput(mtnPin)
		if mtnInput == False:
			log('MAIN - Motion Detected!')
			api.updateTrigger(1)
			buzzer.buzz()
			camera_running = True
			sleep(0.2)
		else:
			camera_running = False
				
except(KeyboardInterrupt, SystemExit):
	cleanupGPIO()
	log('MAIN - Exception')

cleanupGPIO()
