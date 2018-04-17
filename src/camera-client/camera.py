#! /usr/bin/python3

from time import sleep
from helper import * 
import time
import subprocess as sp

def runCamera(run_time):
    end_time = time.time() + run_time
    if time.time() < end_time:
        log('CAMERA - runnning mjpeg script')
        example = sp.Popen(['python3','mjpeg.py']) # runs myPyScript.py 
        sleep(1)

    example.kill()