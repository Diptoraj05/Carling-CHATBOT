# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from nlp_engine import generate_career_response
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
@app.route('/api/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    response = generate_career_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
