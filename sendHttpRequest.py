import json
import requests
from settings import settings


class SendRequest:
    def __init__(self):
        pass

    def SendFile(self):
        # server_url = settings.SERVER_POST_URL
        server_url = settings.SERVER_UPDATE_URL
        json_file = self._GetFile()
        json_file = json.dumps(json_file)
        print json_file
        if not json_file:
            print 'Error while trying to read data.json.'
            return

        send_file = self._SendHttpRequest(server_url, json_file)
        if not send_file:
            print 'Could not send request.'
            return
        else:
            # print 'Request sent, we are at request: {0}'.format(settings.REQUEST_COUNT)
            return True

    @staticmethod
    def _GetFile():
        with open('data.json') as data_file:
            data = json.load(data_file)
        return data

    @staticmethod
    def _SendHttpRequest(url, jsonData):
        headers = {'content-type': 'application/json'}
        try:
            request = requests.post(url, json=jsonData, headers=headers, verify=settings.SSL_CERT_REQUIRED)
        except requests.ConnectionError:
            print 'Could not connect to server.'
            return

        response = request.status_code
        # print ('content is at the moment: "' + request.content + '"')
        if response == 200:
            return request
        else:
            return False

