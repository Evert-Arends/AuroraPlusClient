import json

with open('data.json') as data_file:
    data = json.load(data_file)
    i = 0
    servers = 0
    for server in data["ServerList"]["Servers"]:
        servers += 1
        print data
        print servers

    while i <= 2:
        ids = (data["ServerList"]["Servers"][i]["NetworkUsage"]["Sent"])
        i += 1
        print ids
