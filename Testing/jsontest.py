import json

with open('details.json') as data_file:
    data = json.load(data_file)
    i = 0
    servers = 0
    print data["Server"]["Action"]["Register"]

