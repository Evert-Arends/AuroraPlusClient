from bin import monitor

Monitor = monitor.Monitor


def load_average():
    load = Monitor.getLoadAverage()
    if load:
        return load
    else:
        return


def network_load_average():
    return Monitor.GetNetworkLoad()

if __name__ == "__main__":
    # Monitor.SendJsonToServer()
    # print Monitor.getServerName()
    # print Monitor.getServerId()
    # print Monitor.getLoadAverage()
    # print Monitor.GetNetworkLoad()
    print Monitor.getCPULoad()

