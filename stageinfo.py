import json
from datetime import datetime
from dateutil import tz
from datacaching import fetchdata

class rotation_info:
    url = 'https://splatoon3.ink/data/schedules.json'
    cache = 'cache/splatink.json'
    time = None
    stage1 = None
    stage2 = None
    mode = None
    gamemode = None

    @classmethod
    def getdata(cls):
        return fetchdata(update = False,json_cache=cls.cache,url = cls.url)

    @classmethod
    def time_frame(cls, start, end):
        utc = tz.tzutc()
        pt = tz.gettz('America/Los_Angeles')
        start_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
        end_time = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
        formatted_start_time = start_time.strftime("%I:%M %p")
        formatted_end_time = end_time.strftime("%I:%M %p")
        formatted_time_range = f"{formatted_start_time} - {formatted_end_time}"
        cls.time = formatted_time_range

    @classmethod
    def get_turf(cls):
        turf = cls.getdata()['data']['regularSchedules']['nodes'][0]
        stage1 = turf['regularMatchSetting']['vsStages'][0]['name']
        stage2 = turf['regularMatchSetting']['vsStages'][1]['name']
        startTime = turf['startTime']
        endTime = turf['endTime']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Turf war"
        cls.gamemode = None

    def get_anarchyOpen(cls):
        anarchy = cls.getdata()['data']['bankaraSchedules']['nodes'][0]
        stage1 = anarchy['bankaraMatchSettings'][1]['vsStages'][0]['name']
        stage2 = anarchy['bankaraMatchSettings'][1]['vsStages'][1]['name']
        startTime = anarchy['startTime']
        endTime = anarchy['endTime']
        mode = anarchy['bankaraMatchSettings'][1]['vsRule']['name']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Anarchy Open"
        cls.gamemode = mode
    

    def get_anarchySeries(cls):
        anarchy = cls.getdata()['data']['bankaraSchedules']['nodes'][0]
        stage1 = anarchy['bankaraMatchSettings'][0]['vsStages'][0]['name']
        stage2 = anarchy['bankaraMatchSettings'][0]['vsStages'][1]['name']
        startTime = anarchy['startTime']
        endTime = anarchy['endTime']
        mode = anarchy['bankaraMatchSettings'][0]['vsRule']['name']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Anarchy Series"
        cls.gamemode = mode

    def get_xBattles(cls):
        x = cls.getdata()['data']['xSchedules']['nodes'][0]
        stage1 = x['xMatchSetting']['vsStages'][0]['name']
        stage2 = x['xMatchSetting']['vsStages'][1]['name']
        startTime = x['startTime']
        endTime = x['endTime']
        mode = x['xMatchSetting']['vsRule']['name']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "X"  
        cls.gamemode = mode      
    
