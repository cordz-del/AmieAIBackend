from flask import Flask, request, jsonify
import requests

app = Flask(__name__))

# Define the /tts endpoint
@app.route('/tts', methods=['POST'])
def text_to_speech():
    # Get the text from the request
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Deepgram TTS API URL and headers
    deepgram_tts_url = 'https://api.deepgram.com/v1/tts'
    headers = {
        'Authorization': 'YOUR_DEEPGRAM_API_KEY',  # Replace with your Deepgram API key
        'Content-Type': 'application/json'
    }

    # TTS request payload
    payload = {
        'text': text,
        'model': 'alloy'  # Use the Alloy model
    }

    # Make the TTS request to Deepgram
    response = requests.post(deepgram_tts_url, headers=headers, json=payload)

    if response.status_code != 200:
        return jsonify({'error': 'TTS request failed'}), response.status_code

    # Return the TTS audio URL
    tts_audio_url = response.json().get('audio_url')
    return jsonify({'audio_url': tts_audio_url})

if __name__ == '__main__':
    app.run(debug=True)
