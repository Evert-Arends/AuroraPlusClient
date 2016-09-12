#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os
from settings import settings

PORT = settings.PORT


class Communication:
    def __init__(self):
        print 'Serving content...'

    @staticmethod
    def runServer(jsonFile):
        # Set dir for app to show
        os.chdir(jsonFile)

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)

        print "Serving at port", PORT
        httpd.serve_forever()

if __name__ == "__main__":
    pass
