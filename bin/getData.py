from collections import namedtuple
from subprocess import check_output
import psutil
from time import sleep


class GetData:
    def __init__(self):
        pass

    def uptime(self):
        uptime = check_output("uptime")
        if uptime:
            return uptime
        else:
            return

    def uptime_load_average(self):
        """
        Returns load average of the server.
        :return:
        """
        blob_data = self.uptime()
        if not blob_data:
            return

        uptime_data = blob_data.split(' ', 15)

        # Removing last comma's
        one_minute = uptime_data[13][:-1].upper()
        five_minutes = uptime_data[14][:-1].upper()
        fifteen_minutes = uptime_data[15][:-1].upper()

        load_average = ('%s;%s;%s' % one_minute, five_minutes, fifteen_minutes)
        if not load_average:
            return
        else:
            return load_average

    def network_usage(self):
        network_usage = psutil.net_io_counters(pernic=False)
        previous_received = network_usage.bytes_recv
        previous_sent = network_usage.bytes_sent

        sleep(1)

        network_usage = psutil.net_io_counters(pernic=False)
        current_received = network_usage.bytes_recv
        current_sent = network_usage.bytes_sent

        diff_received = (current_received - previous_received)
        diff_sent = (current_sent - previous_sent)

        network = namedtuple('network', 'received sent')
        total = network(diff_received, diff_sent)

        # Return data send in and out per second
        return total

if __name__ == "__main__":
    G = GetData()
    data = G.uptime_load_average()
    print data

# Sample: load average: 1.05, 0.70, 5.09
#
#
# over the last 1 minute: The computer was overloaded by 5% on average. On average,
# .05 processes were waiting for the CPU. (1.05)
#
# over the last 5 minutes: The CPU idled for 30% of the time. (0.70)
#
# over the last 15 minutes: The computer was overloaded by 409% on average. On average,
# 4.09 processes were waiting for the CPU. (5.09)

