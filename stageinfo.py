import json
from datetime import datetime
from dateutil import tz
from datacaching import fetchdata


class splatinfo:
    url = 'https://splatoon3.ink/data/schedules.json'
    cache = 'cache/splatdata.json'
    time = None
    stage1 = None

    @classmethod
    def getdata(cls):
        return fetchdata(update=False, json_cache=cls.cache, url=cls.url)

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
    def get_turf(cls):
        turf = cls.getdata()['regularmatch']['turf']['1']
        stage1 = turf['map1']
        stage2 = turf['map2']
        startTime = turf['start']
        endTime = turf['end']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Turf war"
        cls.gamemode = None

    def get_anarchyOpen(cls):
        anarchy = cls.getdata()['regularmatch']['open']['1']
        stage1 = anarchy['map1']
        stage2 = anarchy['map2']
        startTime = anarchy['start']
        endTime = anarchy['end']
        mode = anarchy['mode']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Anarchy Open"
        cls.gamemode = mode

    def get_anarchySeries(cls):
        anarchy = cls.getdata()['regularmatch']['series']['1']
        stage1 = anarchy['map1']
        stage2 = anarchy['map2']
        startTime = anarchy['start']
        endTime = anarchy['end']
        mode = anarchy['mode']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "Anarchy Series"
        cls.gamemode = mode

    def get_xBattles(cls):
        x = cls.getdata()['regularmatch']['x']['1']
        stage1 = x['map1']
        stage2 = x['map2']
        startTime = x['start']
        endTime = x['end']
        mode = x['mode']
        cls.time_frame(startTime, endTime)
        cls.stage1 = stage1
        cls.stage2 = stage2
        cls.mode = "X"
        cls.gamemode = mode

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

    boss = None
    weapon1 = None
    weapon2 = None
    weapon3 = None
    weapon4 = None

    def get_salmon(cls):
        salm = cls.getdata()[
            'data']['coopGroupingSchedule']['regularSchedules']['nodes'][0]
        cls.stage1 = salm['setting']['coopStage']['name']
        cls.weapon1 = salm['setting']['weapons'][0]['name']
        cls.weapon2 = salm['setting']['weapons'][1]['name']
        cls.weapon3 = salm['setting']['weapons'][2]['name']
        cls.weapon4 = salm['setting']['weapons'][3]['name']
        startTime = salm['startTime']
        endTime = salm['endTime']
        cls.time_frame(startTime, endTime)
        word = f'The stage is {cls.stage1} and weapons are {cls.weapon1},{cls.weapon2},{cls.weapon3}, and {cls.weapon4} at time {cls.time}'
