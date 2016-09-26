import json

with open('data.json') as data_file:
    data = json.load(data_file)

    maxServer = data["ServerList"]["totalresultsonaccount"]
    maxServer = int(maxServer)
    servers = []
    i = 0

    print 'maxServer = {0}'.format(maxServer)

    while maxServer >= i:
        ids = (data["ServerList"]["serverdata"][i]["id"])
        i += 1
        print ids

    print servers
