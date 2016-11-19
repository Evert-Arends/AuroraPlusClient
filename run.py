#!/usr/bin/env python2
# Imports
from bin import monitor
from settings import settings
import dataCollector

Monitor = monitor.Monitor()

message1 = "Client script running on version: {0}".format(settings.VERSION)
message2 = "Your version is still maintained: {0}".format('True')


class StartMonitor:
    def __init__(self):
        print message1, message2
        print 'Initialising...'
    MonitorData = dataCollector.get_all_data()
    print 'Your CPU load is at the moment: {0}'.format(MonitorData[2])
    print 'Your Network load is at the moment sent: {0} received: {1}'.format(MonitorData[3][0], MonitorData[3][1])
    print 'Your ServerId is: {0}'.format(MonitorData[1])
    print 'Your HostName is: {0}'.format(MonitorData[0])
    print 'Exiting...'

if __name__ == '__main__':
    StartMonitor = StartMonitor()

