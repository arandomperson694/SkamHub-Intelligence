from flask import Flask, request, jsonify 
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_AI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# Pre-set introduction for the chatbot
chat.send_message("You are an assistant for a gaming website called SkamHub. It has games, indian music, news, and you, an AI chatbot. Its main games that you should reccomend is neal.fun, hexanaut.io and imadejptr")

@app.route('/')
def home()
    return "Aman Intelligence is running"
    
@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    
    if user_input.lower() == "bye":
        return jsonify({'response': 'Goodbye!'})

    # Send the user input to Gemini model
    response = chat.send_message(user_input)

    # Return chatbot response
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
