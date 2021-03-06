#!/usr/bin/python3

import requests
import time
import datetime
import variables as variables
from helper import log

access_token = variables.IRIS_API_KEY

headers = {'Authorization': 'Bearer ' + access_token}
cam_id = 1
url = variables.IRIS_API_URL_BASE + str(cam_id) + '/'
data = {}

# Update IP address
def updateIP(id, ip):
    data = {'ip_address': str(ip)}
    log('API - ' + str(ip))
    cam_id = id
    sendUpdate(data, url)

# Update trigger timestamp
def updateTrigger(id):
    # 2018-04-16T12:55:45
    full_date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    cam_id = id
    log('API - ' + full_date)
    data = {'last_triggered': str(full_date)}
    sendUpdate(data, url)

# Sends update to the API
def sendUpdate(data, url):
    request = requests.patch(url, data, headers=headers)
    log('API - ' + str(request))

# Testing
# updateTrigger(1)
# updateIP(1, '192.126.234.32')