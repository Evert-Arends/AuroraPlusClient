# Get the data here, for now: return system time.
import datetime


class GetData:
    def __init__(self):
        print 'Getting data'

    def test(self):
        date = 'teetetetet'
        date += 'ok'
        return date + 'ok'

if __name__ == "__main__":
    G = GetData()
    print G.test()
