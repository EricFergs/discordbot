import json
from datetime import datetime
from dateutil import tz
from cache.datacaching import fetchdata





class splatinfo:
    url = 'https://splatoon3.ink/data/schedules.json'
    cache = 'cache/splatdata.json'
    time = None
    stage1 = None

    @classmethod
    def getdata(cls):
        data = fetchdata(update=False, json_cache=cls.cache, url=cls.url)
        return data
    
    @classmethod
    def time_frame(cls, start, end):
        utc = tz.tzutc()
        pt = tz.gettz('America/Los_Angeles')
        start_time = datetime.strptime(
            start, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
        end_time = datetime.strptime(
            end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc).astimezone(pt)
        formatted_start_time = start_time.strftime("%I:%M %p")
        formatted_end_time = end_time.strftime("%I:%M %p")
        formatted_time_range = f"{formatted_start_time} - {formatted_end_time}"
        cls.time = formatted_time_range


class rotation_info(splatinfo):
    stage2 = None
    mode = None
    gamemode = None

    @classmethod
    def get_rotationinfo(cls,rmode):
        r = cls.getdata()['regularmatch'][rmode]['1']
        stage1 = r['map1']
        stage2 = r['map2']
        startTime = r['start']
        endTime = r['end']
        mode = r['mode']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = rmode
        cls.gamemode = mode

    @classmethod
    def get_turf(cls):
        cls.get_rotationinfo('turf')
        cls.mode = "Turf war"
        cls.gamemode = None

    def get_anarchyOpen(cls):
        cls.get_rotationinfo('open')
        cls.mode = "Anarchy Open"
     
    def get_anarchySeries(cls):
        cls.get_rotationinfo('series')
        cls.mode = "Anarchy Series"

    def get_xBattles(cls):
        cls.get_rotationinfo("x")
        cls.mode = "X rank"

    def modeAndStage(cls, final, allrotation, map, gamemode):
        for rotation in allrotation:
            rotation = allrotation[rotation]
            if (rotation['mode'] == gamemode):
                stage1 = rotation['map1']
                stage2 = rotation['map2']
                startTime = rotation['start']
                endTime = rotation['end']
                cls.time_frame(startTime, endTime)
                if (stage1 == map or stage2 == map):
                    final.append(
                        f'{map} {gamemode} found at time {cls.time}')
        return final

    def modeOnly(cls, final, allrotation, gamemode):
        for rotation in allrotation:
            rotation = allrotation[rotation]
            if (rotation['mode'] == gamemode):
                stage1 = rotation['map1']
                stage2 = rotation['map2']
                startTime = rotation['start']
                endTime = rotation['end']
                cls.time_frame(startTime, endTime)
                final.append(
                    f'{gamemode} {stage1} and {stage2} at times {cls.time}')
        return final

    def mapOnly(cls, final, allrotation, map):
        for rotation in allrotation:
            rotation = allrotation[rotation]
            stage1 = rotation['map1']
            stage2 = rotation['map2']
            startTime = rotation['start']
            endTime = rotation['end']
            gamemode = rotation['mode']
            cls.time_frame(startTime, endTime)
            if (stage1 == map or stage2 == map):
                final.append(
                    f'{map} {gamemode} found at time {cls.time}')
        return final

    def findmaps(cls, mode, map=None, gamemode=None):
        final = []
        allrotation = cls.getdata()['regularmatch'][mode]
        if (map and gamemode):
            final = cls.modeAndStage(final, allrotation, map, gamemode)
        elif (gamemode):
            final = cls.modeOnly(final, allrotation, gamemode)
        else:
            final = cls.mapOnly(final, allrotation, map)
        return final


class salmon_info(splatinfo):
    map = None
    boss = None
    weapon1 = None
    weapon2 = None
    weapon3 = None
    weapon4 = None
    start = None

    def get_salmon(cls, key):
        salm = cls.getdata()['salmon'][key]
        cls.map = salm['stage']
        cls.weapon1 = salm['weapon1']
        cls.weapon2 = salm['weapon2']
        cls.weapon3 = salm['weapon3']
        cls.weapon4 = salm['weapon4']
        startTime = salm['start']
        cls.start = startTime
        endTime = salm['end']
        cls.boss = salm['boss']
        cls.time_frame(startTime, endTime)