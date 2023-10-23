import requests
import json

def getTime(url):
    response = requests.get(url)
    response_json = json.loads(response.text)['time']
    time = int(response_json.split(':')[0])
    if(time > 12):
        time = time - 12
        response_json = str(time) + response_json[2:] + "PM"
    else:
        if(response_json[0] == '0'):
            response_json = response_json[1:]
        response_json = response_json + "AM"
    return response_json

jp = getTime('https://timeapi.io/api/Time/current/zone?timeZone=Japan')
pst = getTime('https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles')
mst = getTime('https://timeapi.io/api/Time/current/zone?timeZone=America/Boise')
cst = getTime('https://timeapi.io/api/Time/current/zone?timeZone=America/North_Dakota/Center')
easternst = getTime('https://timeapi.io/api/Time/current/zone?timeZone=America/Detroit')
