import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user message from the request
        user_message = request.json.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Make a request to the OpenAI API
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_message}]
        )

        # Extract the response content
        assistant_reply = response['choices'][0]['message']['content']

        return jsonify({'response': assistant_reply}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
