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


def virtual_memory_load():
    load = Monitor.getRamLoad()
    return load


def get_all_data():
    data = ['ServerName', 'ServerId', 'CPULoad', 'NetworkLoad', 'RamLoad', 'DiskLoad', 'DiskUsage', 'Message',
            'AlertID']
    data[0] = Monitor.getServerName()
    data[1] = Monitor.getServerId()
    data[2] = Monitor.getCPULoad()
    load = network_load_average()
    data[3] = load
    data[4] = Monitor.getRamLoad()
    data[5] = Monitor.getDiskLoad()
    data[6] = Monitor.getDiskUsage()
    return data


if __name__ == "__main__":
    print get_all_data()





