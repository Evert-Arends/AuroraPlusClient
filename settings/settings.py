import os

PORT = 7802  # Default running port Aurora.
# PYTHON_NAME = 'python'  # If python is default 2.7.
PYTHON_NAME = 'python2.7'  # Aurora is build for python2.7, if you have multiply versions, use this one
BASE_DIR = os.getcwd()
FILE_DIR = (BASE_DIR + '/static/')
FILE = (BASE_DIR + '/static/data.json')
INTERVAL = 2


