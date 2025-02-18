import requests

# Define the URL for the /tts endpoint
url = 'http://localhost:5000/tts'

# Define the JSON payload with sample text
payload = {
    'text': 'Hello, this is a test for the TTS endpoint.'
}

# Send the POST request to the /tts endpoint
response = requests.post(url, json=payload)

# Print the response
print(response.json())
