# This module binds clay functions to python. It is used by clay.py to run python scripts. It is not meant to be used by the user.

import simplejson as json

def reply(value):
    data = []
    with open("Runlogs.json", "r", encoding='utf-8') as file:    
        data = json.load(file)
        file.close()
    data["return"].append(value)
    with open("Runlogs.json", "w", encoding='utf-8') as file:
        if my_str is not None:
            file.write(json.dump(data, file))
            file.close()
def send(name):
    # Read Runlogs.json
    data = []
    with open("Runlogs.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    
    # Append name to data.requests
    data["requests"].append(name)

    # Write data to Runlogs.json
    with open("Runlogs.json", "w", encoding='utf-8') as file:
            
        json.dump(data, file)
def recieve():
    # return the last value in Runlogs.json and remove it
    data = []
    with open("Runlogs.json", "r", encoding='utf-8') as file:    
        data = json.load(file)
        file.close()
    
    value = data["data"][-1]
    return value



