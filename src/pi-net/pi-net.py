#!/usr/local/bin/python3

import netifaces
from pushbullet import Pushbullet

pb = Pushbullet("PUSHBULLET_API_KEY")

# Get IP address
localip = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']

# Send push
user = pb.chats[0]
user.push_note("Raspberry Pi IP Address", localip)

# Uncomment the line below to send the push to yourself rather than someone else
#pb.push_note("Raspberry Pi IP", localip)
