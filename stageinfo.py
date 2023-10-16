import json
import requests
from datetime import datetime
from dateutil import tz


url = 'https://splatoon3.ink/data/schedules.json'
response = requests.get(url)

def time_frame(start, end):
    utc = tz.tzutc()
    pt = tz.gettz('America/Los_Angeles')
    start_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
    end_time = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
    formatted_start_time = start_time.strftime("%I:%M %p")
    formatted_end_time = end_time.strftime("%I:%M %p")
    formatted_time_range = f"{formatted_start_time} - {formatted_end_time}"
    return formatted_time_range




def get_turf():
    turf = json.loads(response.text)['data']['regularSchedules']['nodes'][0]
    stage1 = turf['regularMatchSetting']['vsStages'][0]['name']
    image1 = turf['regularMatchSetting']['vsStages'][0]['image']['url']
    stage2 = turf['regularMatchSetting']['vsStages'][1]['name']
    image2 = turf['regularMatchSetting']['vsStages'][1]['image']['url']
    startTime = turf['startTime']
    endTime = turf['endTime']
    time = time_frame(startTime, endTime)
    all = f"Stages are {stage1} and {stage2} and the timeframe is {time} \n {image1} {image2}"
    return all

def get_anarchyOpen():
    anarchy = json.loads(response.text)['data']['bankaraSchedules']['nodes'][0]
    stage1 = anarchy['bankaraMatchSettings'][0]['vsStages'][0]['name']
    image1 = anarchy['bankaraMatchSettings'][0]['vsStages'][0]['image']['url']
    stage2 = anarchy['bankaraMatchSettings'][0]['vsStages'][1]['name']
    image2 = anarchy['bankaraMatchSettings'][0]['vsStages'][1]['image']['url']
    startTime = anarchy['startTime']
    endTime = anarchy['endTime']
    time = time_frame(startTime, endTime)
    all = f"Open stages are {stage1} and {stage2} and the timeframe is {time} \n {image1} {image2}"
    return all

def get_anarchySeries():
    anarchy = json.loads(response.text)['data']['bankaraSchedules']['nodes'][0]
    stage1 = anarchy['bankaraMatchSettings'][1]['vsStages'][0]['name']
    image1 = anarchy['bankaraMatchSettings'][1]['vsStages'][0]['image']['url']
    stage2 = anarchy['bankaraMatchSettings'][1]['vsStages'][1]['name']
    image2 = anarchy['bankaraMatchSettings'][1]['vsStages'][1]['image']['url']
    startTime = anarchy['startTime']
    endTime = anarchy['endTime']
    time = time_frame(startTime, endTime)
    all = f"Series stages are {stage1} and {stage2} and the timeframe is {time} \n {image1} {image2}"
    return all