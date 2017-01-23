#!/usr/bin/env python2

# Imports
import json
import datetime
from bin import monitor, register
from ClientSettings import ClientSettings
from ClientSettings import constants
import dataCollector
import settings
import time
import sys

Monitor = monitor.Monitor()

message1 = "Client script running on version: {0}".format(ClientSettings.VERSION)
message2 = "Your version is still maintained: {0}".format('True')


class StartMonitor:
    def __init__(self):
        print message1, message2
        print 'Initialising...'

    def monitor(self):
        while 1:
            MonitorData = self.collect_data()
            MonitorData = self.check_need_to_log(MonitorData)
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
        print ' Your DISK usage is at the moment: {0}%.'.format(MonitorData[5])
        print ' You currently have {0} read, and {1} written.'.format(MonitorData[6][0], MonitorData[6][1])
        print ' Your ServerId is: {0}.'.format(MonitorData[1])
        print ' Your HostName is: {0}.'.format(MonitorData[0])
        print ' Last reported message ID is: {0}.'.format(MonitorData[8])
        print ' Last reported message is: {0}.'.format(MonitorData[7])
        print ' This is request: {0}.'.format(constants.REQUEST_COUNT)
        print '\------------------------------------------------------------------------------------------\\'

    @staticmethod
    def write_data(MonitorData):
        with open(settings.JSON_FILE, 'r+') as f:
            json_data = json.load(f)
            json_data["RequestDetails"]["Time"]["RequestSent"] = str(time.time())
            json_data["Server"]["ServerDetails"]["NetworkLoad"]["Sent"] = MonitorData[3][0]
            json_data["Server"]["ServerDetails"]["NetworkLoad"]["Received"] = MonitorData[3][1]
            json_data["Server"]["ServerDetails"]["ServerName"] = MonitorData[0]
            json_data["Server"]["ServerDetails"]["CPU_Usage"] = MonitorData[2]
            json_data["Server"]["ServerDetails"]["ServerKey"] = MonitorData[1]
            json_data["Server"]["ServerDetails"]["Ram_Usage"] = MonitorData[4]
            json_data["Server"]["ServerDetails"]["Disk_Usage"] = MonitorData[5]
            json_data["Server"]["ServerDetails"]["Disk_Load"]["Read"] = MonitorData[6][0]
            json_data["Server"]["ServerDetails"]["Disk_Load"]["Write"] = MonitorData[6][1]

            if MonitorData[8]:
                if Monitor.getLastLogID() < float(MonitorData[8]):
                    json_data["Server"]["Messages"]["Log"] = MonitorData[7]
                    json_data["Server"]["Messages"]["AlertID"] = MonitorData[8]
                    json_data["Server"]["Messages"]["Alert"] = True
                else:
                    json_data["Server"]["Messages"]["Alert"] = False
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

    def check_need_to_log(self, MonitorData):
        if not MonitorData:
            pass
        CPU = MonitorData[2]
        RAM = MonitorData[4]
        if float(CPU) > 75:
            MonitorData = self.log_message(target='CPU', spike=CPU, MonitorData=MonitorData)
        elif float(RAM) > 75:
            MonitorData = self.log_message(target='RAM', spike=RAM, MonitorData=MonitorData)
        else:
            MonitorData = MonitorData
            MonitorData[7] = 'None'
            MonitorData[8] = 0
            self.log_message(target='None', spike=0, MonitorData=MonitorData)
        return MonitorData

    @staticmethod
    def log_message(target, spike, MonitorData):
        if target == 'CPU':
            message = 'There has been a CPU usage spike of: {0}%!'.format(spike)
        elif target == 'RAM':
            message = 'There has been a RAM usage spike of: {0}%!'.format(spike)
        elif target == 'None':
            message = ''
        else:
            message = 'There is an unexpected spike, we are not sure where it is coming from, ' \
                      'but the value is: {0}'.format(spike)
        MonitorData[7] = message
        LastID = Monitor.getLastLogID()
        LastID += 1
        MonitorData[8] = LastID
        return MonitorData


if __name__ == '__main__':
    Arguments = sys.argv
    try:
        if Arguments[1].lower() == '-r':
            print 'Registering...'
            register = register.Register()
            key = register.register_agent()
            with open(ClientSettings.FILE_DIR + 'details.json', 'r+') as f:
                json_data = json.load(f)
                json_data["ServerDetails"]["ServerKey"] = key
                f.seek(0)
                f.write(json.dumps(json_data))
                f.truncate()
        else:
            constants.REGISTER = False
    except IndexError:
        constants.REGISTER = False

    StartMonitor = StartMonitor()
    StartMonitor.monitor()
