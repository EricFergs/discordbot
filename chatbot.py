import requests

# Cody AI API base URL
api_base_url = "https://getcody.ai/api/v1"

# Your Cody AI API key
api_key = "NTM03VnUdS0l5opQcHmGoFXwrLvuJAgfleEHfSgF5039df50"

# Your bot ID
bot_id = "W4QbY72JAezq"

conversation_id = '7LDdw25wmb1Y'

# Headers for API requests
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# Create a conversation
def create_conversation(bot_id):
    endpoint = f"{api_base_url}/conversations"
    data = {
        "name": "Splatconv",
        "bot_id": bot_id
        }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()["data"]["id"]

# Send a message to the bot
def send_message(conversation_id, content):
    endpoint = f"{api_base_url}/messages"
    data = {
        "conversation_id": conversation_id,
        "content": content,
    }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()["data"]["id"]

# Retrieve the response for a message
def get_message_response(message_id):
    endpoint = f"{api_base_url}/messages/{message_id}"
    response = requests.get(endpoint, headers=headers)
    return response.json()["data"]["content"]

def bring_back_message(content):
    message_id = send_message(conversation_id, content)
    response_content = get_message_response(message_id)
    return response_content



# Example usage
if __name__ == "__main__":
    message_content = "What are the prioties in splatoon?"
    message_id = send_message(conversation_id, message_content)

    # Retrieve the response
    response_content = get_message_response(message_id)

    print(f"User: {message_content}")
    print(f"Bot: {response_content}")
