from getData import GetData
import requests
import sendHttpRequest
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
        print load.sent
        print load.received
        return load

    @staticmethod
    def SendJsonToServer():
        print 'sending HTTP request to server...'
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
        print server_name
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

if __name__ == "__main__":
    pass
