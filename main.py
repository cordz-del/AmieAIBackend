

from flask import Flask
from guided_sel_exercise import guided_sel_exercise
from greet_user_with_memory import greet_user_with_memory
from livekit_integration import generate_t

app = Flask(__name__)

@app.route('/')
def home():
    return "Amie Chatbot Interface"

@app.route('/generate_token')
def generate_token():
    # Call the function from livekit_integration.py to generate a token
    token = livekit_integration.generate_livekit_token)
    return token
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
