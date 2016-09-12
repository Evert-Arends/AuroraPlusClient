#!/usr/bin/python
import os
import threading
from time import sleep, time

import datetime

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
        sleep(5)


def runServer():
    print 'serving at http://127.0.0.1:' + str(settings.PORT)
    Communication.runServer(FILE_DIR)


def runTimer():
    start()


if __name__ == "__main__":
    if fileCheck():
        timerThread = threading.Thread(target=start())
        timerThread.start()
        serverThread = threading.Thread(target=runServer())
        serverThread.start()

    else:
        print 'Sorry, there is no file to serve.'
