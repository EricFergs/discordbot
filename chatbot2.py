import requests


# Cody AI API base URL
api_base_url = "https://getcody.ai/api/v1"

# Your Cody AI API key
api_key = "NTM03VnUdS0l5opQcHmGoFXwrLvuJAgfleEHfSgF5039df50"

# Your bot ID
bot_id = "W4QbY72JAezq"

# Headers for API requests
headers = {
    "Authorization": f"Bearer {api_key}"
}



def list_bots():
    endpoint = f"{api_base_url}/bots"
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error listing bots: {response.status_code}, {response.json()}")

# Call the function to list all bots

