from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime

app = Flask(__name__)

# Configure Gemini API (you'll need to set your API key)
# genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # For demo purposes, return a mock response
        # In real implementation, you would use:
        # model = genai.GenerativeModel('gemini-pro')
        # response = model.generate_content(user_message)
        # bot_response = response.text

        # Mock response for demonstration
        bot_response = f"I received your message: '{user_message}'. This is a demo response. To use real Gemini API, configure your API key."

        # Log the conversation
        log_entry = f"[{datetime.now()}] User: {user_message}\nBot: {bot_response}\n\n"
        with open('server_log.txt', 'a') as f:
            f.write(log_entry)

        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/models')
def get_models():
    # Mock model list (in real app, get from Gemini API)
    models = [
        'gemini-pro',
        'gemini-pro-vision',
        'gemini-1.5-pro',
        'gemini-1.5-flash'
    ]
    return jsonify({'models': models})

if __name__ == '__main__':
    app.run(debug=True)