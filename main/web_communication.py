import json

def check_settings(setting):
    with open('settings.json') as json_file:
        data = json.load(json_file)
        return(data[setting])

