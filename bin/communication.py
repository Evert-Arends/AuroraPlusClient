#!/usr/bin/python

from bin import encode
import SimpleHTTPServer
import SocketServer
import requests
import json
import os
from ClientSettings import ClientSettings

PORT = ClientSettings.PORT
EncodingHandler = encode.EncodingHandler()


class Communication:
    def __init__(self):
        pass

    @staticmethod
    def run_server(jsonFile):
        # Set dir for app to show
        os.chdir(jsonFile)

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)

        print "Serving at 1port", PORT
        httpd.serve_forever()

    @staticmethod
    def check_if_key_is_unique(key):
        # Converting to base64, as expected by the server.
        key = EncodingHandler.encode(key, 'base64')
        r = requests.post(ClientSettings.SERVER_CHECK_KEY_URL, json=json.dumps(key))
        if r.status_code != 204:
            print r.status_code
            print r.content
            return
        print r.status_code
        return True

if __name__ == "__main__":
    C = Communication()
    # check = C.check_if_key_is_unique('Lqdie4ARBhbJtawrmTBCkenmhb9rvqgRzWN')
    check = C.check_if_key_is_unique('Lqdie4ARBhbJtawrmTBCkenmhb9rvqgRzWN')
    if check:
        print 'It is okay!'
    else:
        print 'Definitely not ok!'
