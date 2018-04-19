#! /usr/bin/python3

from time import sleep
from helper import * 
import time
import picamera

def runCamera(run_time):
    end_time = time.time() + run_time
    cam = picamera.PiCamera()
    if time.time() < end_time:
        log('CAMERA - taking photos')
        cam.capture('/home/dylan/iris_output/img-' + time + '.jpg')
        sleep(1)