import os
import subprocess
from settings import settings


class Monitor:
    def __init__(self):
        print 'Monitoring...'

    def setData(self, FILE):
        data = self._readData()
        self._writeData(FILE, data)

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
            data = (str(data) + "\n")
            open(FILE, 'a').write(data)  # Write to existing json file
        else:
            open(FILE, 'w+').write(data)  # Create new json file


if __name__ == "__main__":
    pass