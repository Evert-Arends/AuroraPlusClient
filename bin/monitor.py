import os
import subprocess
from settings import settings
from getData import GetData

dataCollection = GetData()


class Monitor:
    def __init__(self):
        print 'Monitoring...'

    @staticmethod
    def getLoadAverage():
        load = dataCollection.uptime_load_average()
        if not load:
            return False
        else:
            return load

    def setData(self, FILE):
        try:
            data = self._readData()
            self._writeData(FILE, data)
            return True
        except:
            return False

    def _readData(self):
        pythonFile = (settings.BASE_DIR + '/bin/getData.py')
        if os.path.isfile(pythonFile):
            cmd = ['python2.7', pythonFile]
            output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
            return output
        else:
            output = 'false, no file'
            return output

    def _writeData(self, FILE, data):
        if os.path.isfile(FILE):
            open(FILE, 'a').write(data)  # Write to existing json file
        else:
            open(FILE, 'w+').write(data)  # Create new json file


if __name__ == "__main__":
    pass
