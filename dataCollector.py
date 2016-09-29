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
    print 'sending HTTP request to server...'
    Monitor.SendJsonToServer()
