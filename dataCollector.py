from bin import monitor

Monitor = monitor.Monitor


def load_average():
    load = Monitor.getLoadAverage()
    if load:
        return load
    else:
        return False

if __name__ == "__main__":
    print load_average()
