
AI-powered Career Counselling Chatbot Backend (TF-IDF based NLP)
=============================================================

Project structure:
- app.py            : Main Flask application with API endpoints
- nlp_engine.py     : TF-IDF based NLPEngine that matches user queries to intents
- responses.json    : Knowledge base (intents, patterns, responses)
- requirements.txt  : Python dependencies

How to run:
1. Create & activate a virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate    # Linux / Mac
   venv\Scripts\activate     # Windows

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   python app.py

4. Health check
   GET http://127.0.0.1:5000/api/ping

5. Chat
   POST http://127.0.0.1:5000/api/message
   Body (JSON): { "message": "I like maths and coding" }

Notes:
- This is a starter project with no persistence. You can later add a database and admin endpoints.
- The NLPEngine uses TF-IDF over intent patterns; add more patterns to improve matching.
