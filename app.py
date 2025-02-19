from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS  # <-- Import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for the app

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        # OpenAI API call to get the chat response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        # Access the content of the chat response
        chat_response = response['choices'][0]['message']['content']

        return jsonify({"response": chat_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Bind Flask app to a port that Render expects
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if no PORT is set
    app.run(host="0.0.0.0", port=port)
