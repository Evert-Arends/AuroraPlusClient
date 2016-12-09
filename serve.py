#!/usr/bin/python
import os
import threading
from time import sleep, time
import datetime
import sys
from settings import settings

from bin import communication, monitor
Communication = communication.Communication()
Monitor = monitor.Monitor()

BASE_DIR = os.getcwd()
FILE_DIR = (BASE_DIR + '/static/')
FILE = (BASE_DIR + '/static/data.json')


def fileCheck():
    if os.path.isfile(FILE):
        return True
    else:
        return False


def start():
    while True:
        print datetime.datetime.now()
        if not Monitor.setData(FILE):
            print 'We hit rock bottom'
            return False
        sleep(settings.INTERVAL)


def runServer():
    print 'serving at http://127.0.0.1:' + str(settings.PORT)
    try:
        Communication.runServer(FILE_DIR)
    except ValueError:
        sys.exit("Socket not available.")

if __name__ == "__main__":
    if fileCheck():
        # Spawning a thread both of them.
        timerThread = threading.Thread(target=start)
        timerThread.start()
        serverThread = threading.Thread(target=runServer)
        serverThread.start()
    else:
        print 'Sorry, there is no file to serve.'
