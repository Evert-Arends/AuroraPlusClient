import jsontest
import psutil
from time import sleep


def bytes_2_human_readable(number_of_bytes):
    if number_of_bytes < 0:
        raise ValueError("!!! numberOfBytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit



jsonData = [
    "{'wlp2s0': snetio(bytes_sent=168478881, bytes_recv=6461132032, packets_sent=1437653, packets_recv=6342477, errin=0, errout=0, dropin=6, dropout=0), 'eno1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'lo': snetio(bytes_sent=4694482, bytes_recv=4694482, packets_sent=43122, packets_recv=43122, errin=0, errout=0, dropin=0, dropout=0)}"]

# snetio(bytes_sent=173805460, bytes_recv=6473619759,
#  packets_sent=1485146, packets_recv=6419386, errin=0, errout=0, dropin=6, dropout=0)
NetworkUsage = psutil.net_io_counters(pernic=False)

PreviousReceived = NetworkUsage.bytes_recv
PreviousSend = NetworkUsage.bytes_sent

print PreviousReceived
print PreviousSend
sleep(1)
NetworkUsage = psutil.net_io_counters(pernic=False)
CurrentReceived = NetworkUsage.bytes_recv
CurrentSend = NetworkUsage.bytes_sent

DiffReceived = (CurrentReceived - PreviousReceived)
DiffSend = (CurrentSend - PreviousSend)

print bytes_2_human_readable(DiffReceived)
print bytes_2_human_readable(DiffSend)

