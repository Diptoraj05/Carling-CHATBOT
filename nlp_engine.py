# nlp_engine.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyAIOAPSW-r7xEOOgJDNcjTOEsxVE4tKFrE"))

def generate_career_response(user_input):
    """
    Sends the user input to Gemini API and returns a generated response.
    Works with google-generativeai v0.8.5 and Python 3.13.
    """
    try:
        # Use gemini-pro (not 1.5)
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"