from flask import Flask, request, jsonify 
from flask_cors import CORS
import os
import google.generativeai as genai

app = Flask(__name__)

# Enable CORS
CORS(app)

# Configure the Google Gemini API with your API key
api_key = os.getenv("GOOGLE_AI_API_KEY")
if not api_key:
    raise ValueError("API Key for Google Generative AI is not set.")
genai.configure(api_key=api_key)

# Start the Gemini chat model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# Initial introduction message
intro_message = ("You are an assistant called SkamHub Intelligence that helps people search for web games")

@app.route('/')
def home():
    return "SkamHub Intelligence is running!"

@app.route('/chat', methods=['POST'])
def chat_with_ai():
    try:
        user_input = request.json.get("input")
        if not user_input:
            return jsonify({"error": "No input provided"}), 400
        
        # Send the initial introduction message if it's the first request
        if user_input.lower() == "start":
            response = intro_message
        else:
            # Send user input to the chatbot and get a response
            response = chat.send_message(user_input).text
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)



