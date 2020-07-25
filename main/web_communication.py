import json

def check_settings():
    with open('settings.json') as json_file:
        data = json.load(json_file)
        for p in data:
            print(data[p])

check_settings()