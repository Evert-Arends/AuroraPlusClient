# Get the data here, for now: return system time.
import datetime


class GetData:
    def __init__(self):
        pass
    def test(self):
        date = datetime.datetime.now()
        return date

if __name__ == "__main__":
    G = GetData()
    print G.test()
