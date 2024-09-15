import os 
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Step 1: Configure the Google Gemini API with your API key
api_key = os.getenv("GOOGLE_AI_API_KEY")
if not api_key:
    raise ValueError("API Key for Google Generative AI is not set.")
genai.configure(api_key=api_key)

# Step 2: Start the Gemini chat model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

@app.route('/')
def home():
    return "SkamHub Intelligence is running!"

# Step 3: Chat route for interacting with the chatbot
@app.route('/chat', methods=['POST'])
def chat_with_ai():
    try:
        # Log the incoming request
        print("Request received:", request.json)

        # Step 4: Get user input from the request
        user_input = request.json.get("input")

        # Step 5: Validate that input was provided
        if not user_input:
            print("No input provided in the request.")
            return jsonify({"error": "No input provided"}), 400

        # Log the input
        print(f"User input: {user_input}")

        # Step 6: Send input to the chatbot and get the response
        response = chat.send_message(user_input)

        # Log the chatbot's response
        print(f"Chatbot response: {response.text}")

        # Step 7: Return the chatbot's response as JSON
        return jsonify({"response": response.text})
    except Exception as e:
        # Log the error and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Step 8: Run the app on the correct port (Render uses port 10000 by default)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

