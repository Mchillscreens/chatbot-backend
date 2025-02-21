import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        # Use the correct method for chat models (ChatCompletion)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Correct model
            messages=[{"role": "user", "content": user_message}]  # Format messages correctly
        )

        return jsonify({"response": response['choices'][0]['message']['content']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



