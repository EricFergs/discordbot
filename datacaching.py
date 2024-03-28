import json
import requests
from datetime import datetime, timezone
from clearjson import filterData

def fetchdata(*, update: bool = False, json_cache: str, url: str):
    if update:
        json_data = None
    else:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                rotationtime = json_data['regularmatch']['turf']['1']['end']
                current_datetime_utc = datetime.now(timezone.utc)
                currtime = current_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
                if (currtime > rotationtime):
                    json_data = None
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'the error is {e}')
            json_data = None
    if not json_data:
        print("getting new data")
        json_data = requests.get(url).json()
        json_data = filterData(json_data)
        with open(json_cache, 'w') as file:
            json.dump(json_data, file)
    return json_data


if __name__ == "__main__":
    url = 'https://splatoon3.ink/data/schedules.json'
    json_cache = 'cache/splatdata.json'
    data: dict = fetchdata(
        update=False, json_cache=json_cache, url=url)

    