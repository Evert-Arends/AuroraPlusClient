#!/usr/bin/env python2

# Imports
import json
import datetime
from bin import monitor
from settings import settings
from settings import constants
import dataCollector

Monitor = monitor.Monitor()

message1 = "Client script running on version: {0}".format(settings.VERSION)
message2 = "Your version is still maintained: {0}".format('True')


class StartMonitor:
    def __init__(self):
        print message1, message2
        print 'Initialising...'

    def monitor(self):
        while 1:
            MonitorData = self.collect_data()
            self.write_data(MonitorData)
            self.upload_data()
            self.update_count_requests()
            self.print_data(MonitorData)
            print

    @staticmethod
    def collect_data():
        MonitorData = dataCollector.get_all_data()
        return MonitorData

    @staticmethod
    def print_data(MonitorData):
        print '\-----------------------------------System Statistics--------------------------------------\\'
        print ' Your Network load is at the moment sent: {0} Bytes, and received: {1} Bytes.'.format(MonitorData[3][0],
                                                                                                     MonitorData[3][1])
        print ' Your CPU load is at the moment: {0}%.'.format(MonitorData[2])
        print ' Your RAM usage is at the moment: {0}%.'.format(MonitorData[4])
        print ' Your ServerId is: {0}.'.format(MonitorData[1])
        print ' Your HostName is: {0}.'.format(MonitorData[0])
        print ' This is request: {0}.'.format(constants.REQUEST_COUNT)
        print '\------------------------------------------------------------------------------------------\\'

    @staticmethod
    def write_data(MonitorData):
        with open('data.json', 'r+') as f:
            json_data = json.load(f)
            json_data["RequestDetails"]["Time"]["RequestSent"] = str(datetime.datetime.now())
            json_data["Server"]["ServerDetails"]["NetworkLoad"]["Sent"] = MonitorData[3][0]
            json_data["Server"]["ServerDetails"]["NetworkLoad"]["Received"] = MonitorData[3][1]
            json_data["Server"]["ServerDetails"]["ServerName"] = MonitorData[0]
            json_data["Server"]["ServerDetails"]["CPU_Usage"] = MonitorData[2]
            json_data["Server"]["ServerDetails"]["ServerKey"] = MonitorData[1]
            json_data["Server"]["ServerDetails"]["RamUsage"] = MonitorData[4]

            f.seek(0)
            f.write(json.dumps(json_data))
            f.truncate()

    @staticmethod
    def upload_data():
        # print 'Sending json.'
        Monitor.SendJsonToServer()

    @staticmethod
    def update_count_requests():
        constants.REQUEST_COUNT += 1
        return constants.REQUEST_COUNT


if __name__ == '__main__':
    StartMonitor = StartMonitor()
    StartMonitor.monitor()
