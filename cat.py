import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()

Cat_API = os.getenv("CAT_API_TOKEN")

def get_cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    params = {
        "api-key" : Cat_API
    }
    response = requests.get(url,params=params)
    response = response.json()[0]["url"]
    return response