import json
import requests
from datetime import datetime


def fetchdata(*, update: bool = False, json_cache: str, url: str):
    if update:
        json_data = None
    else:
        try:
            with open(json_cache, 'r') as file:
                print("no new data")
                json_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'the error is {e}')
            json_data = None
    if not json_data:
        print("getting new data")
        json_data = requests.get(url).json()
        currtime = datetime.now().replace(microsecond=0).isoformat()
        json_data_with_time = {
            'data': json_data,
            'timestamp': currtime
        }
        with open(json_cache, 'w') as file:
            json.dump(json_data_with_time, file)
    return json_data_with_time

if __name__ == "__main__":
    url = 'https://splatoon3.ink/data/schedules.json'
    json_cache = 'cache/splatink.json'
    data: dict = fetchdata(
        update=False, json_cache=json_cache, url=url)

    print("done")
