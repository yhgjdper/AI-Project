import json

def check_settings(setting):
    with open('settings.json') as json_file:
        data = json.load(json_file)
        return(data[setting])

def talk_toggled():
    with open('startTalking.json') as json_file:
        data = json.load(json_file)
        if data['toggleTalking'] == 'on':
            return True
        return False

def talk_toggle_off():
    f = open('startTalking.json', 'w')
    f.write('{"toggleTalking":"off"}')
    f.close()
