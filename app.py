from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS
import logging

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    app.logger.debug(f"Received message: {user_message}")  # Log the message

    try:
        # Make the OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        # Log the OpenAI API response
        app.logger.debug(f"OpenAI API response: {response}")

        # Extract the response from OpenAI
        bot_response = response['choices'][0]['message']['content']

        # Return the response to the frontend
        return jsonify({"response": bot_response})

    except Exception as e:
        # Log the error and return it
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
