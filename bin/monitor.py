import json

from getData import GetData
import requests
import sendHttpRequest
import settings

dataCollection = GetData()


class Monitor:
    def __init__(self):
        print 'Monitoring...'

    @staticmethod
    def getLoadAverage():
        load = dataCollection.uptime_load_average()
        if not load:
            return
        else:
            return load

    @staticmethod
    def GetNetworkLoad():
        load = dataCollection.network_usage()
        return load

    @staticmethod
    def SendJsonToServer():
        # print 'sending HTTP request to server...'
        try:
            HttpServe = sendHttpRequest.SendRequest()
            HttpServe.SendFile()
            return True
        except requests.ConnectionError:
            print 'error'
            return

    @staticmethod
    def getServerName():
        server_name = dataCollection.system_hostname()
        return server_name

    @staticmethod
    def getNewServerId():
        server_id = dataCollection.new_server_id()
        if not server_id:
            return
        return server_id

    @staticmethod
    def getServerId():
        server_id = dataCollection.server_id()
        if not server_id:
            server_id = Monitor.getNewServerId()

        return server_id

    @staticmethod
    def getCPULoad():
        load = dataCollection.cpu_load()
        if not load:
            load = 0

        return load

    @staticmethod
    def getRamLoad():
        load = dataCollection.ram_load()
        if not load:
            load = 0

        return load

    @staticmethod
    def getDiskLoad():
        # Disk usage in percent. (Only the home partition.)
        load = dataCollection.disk_load()
        return load

    @staticmethod
    def getDiskUsage():
        # Read and write (in that order) in user readable format.
        load = dataCollection.disk_usage()
        return load

    @staticmethod
    def getLastLogID():
        with open(settings.JSON_FILE, 'r+') as f:
            json_data = json.load(f)
            LastID = json_data["Server"]["Messages"]["AlertID"]
            if LastID:
                return float(LastID)
            return


if __name__ == "__main__":
    Monitor = Monitor()
    Monitor.getLastLogID()


