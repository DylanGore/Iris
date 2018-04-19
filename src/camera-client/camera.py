#! /usr/bin/python3

from time import sleep
from helper import * 
import time
import datetime
import picamera

def runCamera(run_time):
    curr_time = time.time()
    end_time = curr_time + run_time
    cam = picamera.PiCamera()
    timestamp = datetime.datetime.fromtimestamp(curr_time).strftime('%Y-%m-%d-%H:%M:%S')
    if time.time() < end_time:
        log('CAMERA - taking photos')
        cam.capture('/home/dylan/iris_output/img-' + timestamp + '.jpg')
        cam.close()
        sleep(0.5)