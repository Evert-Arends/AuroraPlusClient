import requests
from settings import settings


class SendRequest:
    def __init__(self):
        pass

    def SendFile(self):
        ServerUrl = settings.SERVER_POST_URL
        JsonFile = self._GetFile()
        if not JsonFile:
            print 'Error while trying to read data.json.'
            return

        SendFile = self._SendHttpRequest(ServerUrl, JsonFile)
        if not SendFile:
            print 'Could not send request.'
            return
        else:
            print 'Request sent, we are at request: {0}'.format(settings.REQUEST_COUNT)
            settings.REQUEST_COUNT += 1
            return True

    @staticmethod
    def _GetFile():
        return 'ok'

    @staticmethod
    def _SendHttpRequest(url, jsonData):
        headers = {'content-type': 'application/json'}
        try:
            request = requests.post(url, json=jsonData, headers=headers, verify=settings.SSL_CERT_REQUIRED)
        except requests.ConnectionError:
            print 'Could not connect to server.'
            return

        response = request.status_code
        if '200' in response:
            return request
        else:
            return

# example:
# r = requests.post("https://hackflag.org/forum/xmlhttp.php", cookies=cookie, data={'action': 'dvz_sb_shout',
#                                                                                   'text': text,
#                                                                    'key': 'bd8a90464844abec93c473945b880e54'
#                                                                                   })
