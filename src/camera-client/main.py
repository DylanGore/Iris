#! /usr/bin/python3

import RPi.GPIO as GPIO
import buzzer as buzzer
import subprocess as sp
from time import sleep
from helper import *
from pb import sendPush
import variables
import camera 
import api

camera_running = False
camera_time = variables.CAMERA_RUN_TIME

#Pin Declare
mtnPin = variables.MOTION_DETECTOR_PIN

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
			sendPush('Motion Detected', 'Motion has been detected on this camera!')
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
