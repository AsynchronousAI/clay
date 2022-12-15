# This module binds clay functions to python. It is used by clay.py to run python scripts. It is not meant to be used by the user.

import simplejson as json
class NoneToEmptyJSON(json.JSONEncoder):
    def default(self, o):
        if o == None:
            o = ''
        elif type(o) == dict:
            return {self.default(key): self.default(value) for key, value in o.items()}
        elif type(o) == list or type(o) == tuple:
            return [self.default(item) for item in o]
        return o
    def encode(self, o):
        return super().encode(self.default(o))
def reply(value):
    data = []
    with open("Runlogs.json", "r", encoding='utf-8') as file:    
        data = json.load(file)
        file.close()
    data["return"].append(value)
    with open("Runlogs.json", "w", encoding='utf-8') as file:
        if data is not None:
            file.write(NoneToEmptyJSON().encode(data))
            file.close() #
def send(name, dt = "None"):
    # Read Runlogs.json
    data = []
    with open("Runlogs.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    
    # Append name to data.requests
    data["requests"].append(name)
    data["data"].append(dt)

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



