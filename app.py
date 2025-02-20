from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)  # This allows all domains to access this backend. You can customize this later for specific domains if needed.

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        # OpenAI API call
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response.choices[0].message['content']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
