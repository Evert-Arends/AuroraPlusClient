import os

DEBUG = False

PORT = 7800  # Default running port Aurora client script.

if DEBUG:
    SERVER_PORT = 8002
    SERVER_URL = ('http://127.0.0.1:%s/' % SERVER_PORT)
else:
    SERVER_PORT = 80
    SERVER_URL = ('http://51.15.63.248:%s/' % SERVER_PORT)

PYTHON_NAME = 'python2.7'  # Aurora is build for python2.7, if you have multiply versions, use this one
BASE_DIR = os.getcwd()
FILE_DIR = (BASE_DIR + '/static/')
FILE = (BASE_DIR + '/static/data.json')
INTERVAL = 1
SERVER_POST_URL = ('%spost/' % SERVER_URL)
SERVER_CHECK_KEY_URL = ('%scheck_client_key/' % SERVER_URL)
SERVER_REGISTER_URL = ('%sadd_client/' % SERVER_URL)
SERVER_UPDATE_URL = ('%supdate_client/' % SERVER_URL)
SSL_CERT_REQUIRED = True
VERSION = 1
SLEEP_FOR_ACTIONS = 1

