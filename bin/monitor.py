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
        try:
            HttpServe = sendHttpRequest.SendRequest()
            HttpServe.SendFile()
            return True
        except requests.ConnectionError:
            print 'error'
            return


if __name__ == "__main__":
    pass
