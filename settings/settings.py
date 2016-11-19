import os

DEBUG = True

PORT = 7800  # Default running port Aurora client script.

SERVER_PORT = 8001
PYTHON_NAME = 'python2.7'  # Aurora is build for python2.7, if you have multiply versions, use this one
BASE_DIR = os.getcwd()
FILE_DIR = (BASE_DIR + '/static/')
FILE = (BASE_DIR + '/static/data.json')
INTERVAL = 1
SERVER_URL = ('http://localhost:%s/' % SERVER_PORT)
SERVER_POST_URL = ('%spost/' % SERVER_URL)
SERVER_REGISTER_URL = ('%sadd_client/' % SERVER_URL)
SERVER_UPDATE_URL = ('%supdate_client/' % SERVER_URL)
REQUEST_COUNT = 0
SSL_CERT_REQUIRED = True
VERSION = 1
SLEEP_FOR_ACTIONS = 1

