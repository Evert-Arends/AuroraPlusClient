#!/usr/bin/python
import os
import threading
from time import sleep

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
    Monitor.setData(FILE)
    t = threading.Timer(3, start())
    t.start()

if __name__ == "__main__":
    if fileCheck():
        start()
        Communication.runServer(FILE_DIR)
    else:
        print 'Sorry, there is no file to serve.'
