# Pi-Net

This is a simple script that is not required but makes development much easer when using a headless Raspbery Pi setup. When the script is run, it will send a message via Pushbullet containing it's local IP address. This is especially useful if you have to use a mobile hotspot or are unable to find the Pi on your network.

---

## Setup

Install *netifaces* and *pushbullet.py* as they are required for the script to run

```bash
$ sudo pip3 install netifaces pushbullet.py
```

Replace the PUSHBULLET_API_KEY in *pi-ney.py* with your API key from Pushbullet

---

## Run automatically on startup

To have this script run automatically when the Pi starts, all you have to do is add the following to the */etc/rc.local* file:

```python
/usr/bin/python3 /home/pi/srcpi-net/pi-net.py
```

* Replace */usr/bin/python3* with the path of your python directory
* Replace */home/pi/src/pi-net/pi-net.py* with the location of the *pi-net.py* file on your system

**Important**: You must add this line above the *exit 0* line in */etc/rc.local* for it to function