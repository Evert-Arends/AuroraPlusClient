#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import requests
import json
import os
from ClientSettings import ClientSettings

PORT = ClientSettings.PORT


class Communication:
    def __init__(self):
        pass
    @staticmethod
    def run_server(jsonFile):
        # Set dir for app to show
        os.chdir(jsonFile)

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)

        print "Serving at port", PORT
        httpd.serve_forever()

    @staticmethod
    def check_if_key_is_unique(key):
        keyList = ['Key', key]
        # ENCODE INTO BASE64!! (Encoding class in /bin/
        r = requests.post(ClientSettings.SERVER_CHECK_KEY_URL, json=json.dumps(keyList))
        if r.status_code != 204:
            return

        return True

if __name__ == "__main__":
    C = Communication()
    # check = C.check_if_key_is_unique('Lqdie4ARBhbJtawrmTBCkenmhb9rvqgRzWN')
    check = C.check_if_key_is_unique('Lqdie4ARBhbJtawrmTBCkenmhk9rvqgRzWN')
    if check:
        print 'It is okay!'
    else:
        print 'Definitely not ok!'
