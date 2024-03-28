import json


def create_regularmatch():
    cleanData = {
        "regularmatch": {
            "turf": {},
            "open": {},
            "series": {},
            "x": {}
        },
    }
    return cleanData


def getTurf(cleanData, data):
    turf = data['data']['regularSchedules']['nodes']
    i = 1
    for rotation in turf:
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
        cleanData['regularmatch']['turf'][i] = rotation_data
        i += 1
    return cleanData


def getOpen(cleanData, data):
    open = data['data']['bankaraSchedules']['nodes']
    i = 1
    for rotation in open:
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
        cleanData['regularmatch']['open'][i] = rotation_data
        i += 1
    return cleanData


def getSeries(cleanData, data):
    series = data['data']['bankaraSchedules']['nodes']
    i = 1
    for rotation in series:
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
        cleanData['regularmatch']['series'][i] = rotation_data
        i += 1
    return cleanData


def getX(cleanData, data):
    turf = data['data']['xSchedules']['nodes']
    i = 1
    for rotation in turf:
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
        cleanData['regularmatch']['x'][i] = rotation_data
        i += 1
    return cleanData


def filterData(data):
    cleanData = create_regularmatch()
    cleanData = getTurf(cleanData, data)
    cleanData = getOpen(cleanData, data)
    cleanData = getSeries(cleanData, data)
    cleanData = getX(cleanData, data)
    return cleanData


if __name__ == "__main__":
    with open('cache/splatink.json', 'r') as file:
        data = json.load(file)
        cleanData = filterData(data)
    with open('cache/splatdata.json', 'w') as file:
        json.dump(cleanData, file)
