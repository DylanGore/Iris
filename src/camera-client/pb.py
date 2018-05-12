#!/usr/local/bin/python3

from pushbullet import Pushbullet
from variables import PUSHBULLET_API_KEY

# Init Pushbullet 
pb = Pushbullet(PUSHBULLET_API_KEY)

# Send push
def sendPush(title, message):
    user = pb.chats[0]
    user.push_note(title, message)
