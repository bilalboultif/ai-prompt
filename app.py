from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the Gemini API SDK with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Flask application instance
app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Function to generate text based on a prompt
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

# Route to handle POST requests for text generation
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    generated_text = generate_text(prompt)
    return jsonify({'response': generated_text})

# Main section to run the Flask application
if __name__ == '__main__':
    # Run Flask app in debug mode
    app.run(debug=True)
