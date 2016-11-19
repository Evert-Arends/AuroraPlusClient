from bin import monitor

Monitor = monitor.Monitor


# Get cpu load
def get_cpu_data():
    c = Monitor.getCPULoad()
    if not c:
        return
    return c


# Send json data to the API server.
def post_json_data():
    request = Monitor.SendJsonToServer()
    if request:
        return True
    else:
        return


def network_load_average():
    load = Monitor.GetNetworkLoad()
    return load


def get_all_data():
    data = ['ServerName', 'ServerId', 'CPULoad', 'NetworkLoad_Sent', 'NetworkLoad_Received']
    data[0] = Monitor.getServerName()
    data[1] = Monitor.getServerId()
    data[2] = Monitor.getCPULoad()
    load = network_load_average()
    data[3] = load
    test = load
    print test

    return data


if __name__ == "__main__":
    data = ['ServerName', 'ServerId', 'CPULoad', 'NetworkLoad']
    data[0] = Monitor.getServerName()
    data[1] = Monitor.getServerId()
    data[2] = Monitor.getCPULoad()
    load = Monitor.GetNetworkLoad()
    data[3] = load
    print data[3][1]





