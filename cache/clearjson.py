import json


def create_regularmatch():
    cleanData = {
        "regularmatch": {
            "turf": {},
            "open": {},
            "series": {},
            "x": {},
        },
        "salmon": {},
    }
    return cleanData


def getTurf(cleanData, data):
    turf = data['data']['regularSchedules']['nodes']
    for i, rotation in enumerate(turf, start=1):
        mode = rotation['regularMatchSetting']['vsRule']['name']
        map1 = rotation['regularMatchSetting']['vsStages'][0]['name']
        map2 = rotation['regularMatchSetting']['vsStages'][1]['name']
        start = rotation['startTime']
        end = rotation['endTime']
        rotation_data = {
                "mode": mode,
                "map1": map1,
                "map2": map2,
                "start": start,
                "end": end
        }
        cleanData['regularmatch']['turf'][str(i)] = rotation_data
    return cleanData


def getOpen(cleanData, data):
    open = data['data']['bankaraSchedules']['nodes']
    for i, rotation in enumerate(open, start=1):
        mode = rotation['bankaraMatchSettings'][1]['vsRule']['name']
        map1 = rotation['bankaraMatchSettings'][1]['vsStages'][0]['name']
        map2 = rotation['bankaraMatchSettings'][1]['vsStages'][1]['name']
        start = rotation['startTime']
        end = rotation['endTime']
        rotation_data = {
                "mode": mode,
                "map1": map1,
                "map2": map2,
                "start": start,
                "end": end
        }
        cleanData['regularmatch']['open'][str(i)] = rotation_data
    return cleanData


def getSeries(cleanData, data):
    series = data['data']['bankaraSchedules']['nodes']
    for i, rotation in enumerate(series, start=1):
        mode = rotation['bankaraMatchSettings'][0]['vsRule']['name']
        map1 = rotation['bankaraMatchSettings'][0]['vsStages'][0]['name']
        map2 = rotation['bankaraMatchSettings'][0]['vsStages'][1]['name']
        start = rotation['startTime']
        end = rotation['endTime']
        rotation_data = {
                "mode": mode,
                "map1": map1,
                "map2": map2,
                "start": start,
                "end": end
        }
        cleanData['regularmatch']['series'][str(i)] = rotation_data
    return cleanData


def getX(cleanData, data):
    turf = data['data']['xSchedules']['nodes']
    for i, rotation in enumerate(turf, start=1):
        mode = rotation['xMatchSetting']['vsRule']['name']
        map1 = rotation['xMatchSetting']['vsStages'][0]['name']
        map2 = rotation['xMatchSetting']['vsStages'][1]['name']
        start = rotation['startTime']
        end = rotation['endTime']
        rotation_data = {
                "mode": mode,
                "map1": map1,
                "map2": map2,
                "start": start,
                "end": end
        }
        cleanData['regularmatch']['x'][str(i)] = rotation_data
    return cleanData

def getSalmon(cleanData, data):
    salmon = data['data']['coopGroupingSchedule']['regularSchedules']['nodes']
    for i,rotation in enumerate(salmon, start=1):
        stage = rotation['setting']['coopStage']['name']
        boss = rotation['setting']['boss']['name']
        weapon1 = rotation['setting']['weapons'][0]['name']
        weapon2 = rotation['setting']['weapons'][1]['name']
        weapon3 = rotation['setting']['weapons'][2]['name']
        weapon4 = rotation['setting']['weapons'][3]['name']
        start = rotation['startTime']
        end = rotation['endTime']
        rotation_data = {
            "stage": stage,
            "boss": boss,
            "weapon1": weapon1,
            "weapon2": weapon2,
            "weapon3": weapon3,
            "weapon4": weapon4,
            "start": start,
            "end": end
        }
        cleanData['salmon'][str(i)] = rotation_data
    
    try:
        exists = cleanData['salmon'][4]
        if exists:
            bigRun = data['data']['coopGroupingSchedule']['bigRunSchedules']['nodes'][0]
            stage = bigRun['setting']['coopStage']['name']
            boss = bigRun['setting']['boss']['name']
            weapon1 = bigRun['setting']['weapons'][0]['name']
            weapon2 = bigRun['setting']['weapons'][1]['name']
            weapon3 = bigRun['setting']['weapons'][2]['name']
            weapon4 = bigRun['setting']['weapons'][3]['name']
            start = bigRun['startTime']
            end = bigRun['endTime']
            bigRunData = {
                "stage": stage,
                "boss": boss,
                "weapon1": weapon1,
                "weapon2": weapon2,
                "weapon3": weapon3,
                "weapon4": weapon4,
                "start": start,
                "end": end
            }
            cleanData['salmon']['4'] = bigRunData   
    except (KeyError, IndexError, TypeError):
       print("Big Run doesn't exist")
    return cleanData

def filterData(data):
    cleanData = create_regularmatch()
    cleanData = getTurf(cleanData, data)
    cleanData = getOpen(cleanData, data)
    cleanData = getSeries(cleanData, data)
    cleanData = getX(cleanData, data)
    cleanData = getSalmon(cleanData, data)
    
    return cleanData

if __name__ == "__main__":
    with open('cache/splatink.json', 'r') as file:
        data = json.load(file)
        cleanData = filterData(data)
    with open('cache/splatdata.json', 'w') as file:
        json.dump(cleanData, file)
