from getData import GetData

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


if __name__ == "__main__":
    pass
