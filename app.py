import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

# Initialize Flask App
app = Flask(__name__, template_folder='.')
CORS(app)
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__, template_folder='.')
CORS(app)

# --- API CONFIGURATION ---
# We use Qwen because it is free, fast, and highly intelligent
API_KEY = "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" 
BASE_URL = "https://router.huggingface.co/v1"

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

@app.route('/')
def home():
    print("Request received for Home Page")
    try:
        return render_template('index.html')
    except Exception as e:
        return f"<h1>Error</h1><p>Could not find index.html. Error: {e}</p>"

@app.route('/ask', methods=['POST'])
def ask_jarvis():
    try:
        data = request.json
        user_text = data.get('message', '')
        print(f"User said: {user_text}")

        # 1. Check if message is empty
        if not user_text:
            return jsonify({"reply": "I didn't hear anything, sir."})

        # 2. Call the Hugging Face API (Using Qwen Model)
        print("Contacting AI Brain...")
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct", 
            messages=[
                {"role": "system", "content": "You are J.A.R.V.I.S. You are an AI assistant. Keep your answers short, precise, and spoken like a helpful butler."},
                {"role": "user", "content": user_text}
            ],
            max_tokens=150
        )
        
        ai_response = completion.choices[0].message.content
        print(f"Jarvis Replied: {ai_response}")
        
        return jsonify({"reply": ai_response})

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return jsonify({"reply": "I am unable to connect to the server at the moment, sir."}), 500

if __name__ == '__main__':
    print("-------------------------------------------------")
    print("JARVIS SERVER IS ONLINE")
    print("-------------------------------------------------")
    print("1. Go to your browser.")
    print("2. Type exactly: http://127.0.0.1:5000")
    print("-------------------------------------------------")
    app.run(debug=True, port=5000)
# --- CONFIGURATION ---
# ideally use environment variables, but this works for your local test
API_KEY = "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" 
BASE_URL = "https://router.huggingface.co/v1"

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

@app.route('/')
def home():
    # This serves your existing HTML file
    try:
        return render_template('index.html')
    except Exception as e:
        return f"<h3>Error: Could not find index.html</h3><p>Make sure 'app.py' and 'index.html' are in the exact same folder.</p><p>Details: {e}</p>"

@app.route('/ask', methods=['POST'])
def ask_jarvis():
    try:
        data = request.json
        user_text = data.get('message', '')
        
        print(f"User said: {user_text}")

        # Call the AI API
        completion = client.chat.completions.create(
            model="zai-org/GLM-4.6:novita",
            messages=[
                {"role": "system", "content": "You are Jarvis. Keep answers short, punchy, and futuristic."},
                {"role": "user", "content": user_text}
            ],
        )
        
        ai_response = completion.choices[0].message.content
        print(f"Jarvis says: {ai_response}")
        return jsonify({"reply": ai_response})

    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"reply": "I am having trouble connecting to the network, sir."}), 500

if __name__ == '__main__':
    print("Starting Jarvis Server...")
    print("Go to http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)