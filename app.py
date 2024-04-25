from flask import Flask, render_template, request
from pybot_logic import chat  # Import the chat function from pybot_logic.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = chat(user_message)  # Use the chat function from pybot_logic.py
    return bot_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
