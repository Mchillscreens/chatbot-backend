from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        # UPDATED OpenAI API call (compatible with openai>=1.0.0)
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Bind Flask app to a port that Render expects
if __name__ == "__main__":
    # Use Render's dynamic port or default to 5000
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if no PORT is set
    app.run(host="0.0.0.0", port=port)

