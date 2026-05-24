import os
import logging
from flask import Flask, render_template, request, jsonify, send_file
from groq import Groq
from dotenv import load_dotenv
from gtts import gTTS
import io

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

app = Flask(__name__)

# Groq API Key Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat_bot_video.mp4')
def serve_video():
    return send_file('templates/chat bot video.mp4', mimetype='video/mp4')

@app.route('/chat_bot.png')
def serve_bg():
    return send_file('templates/chat bot.png', mimetype='image/png')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    language = data.get('language', 'English')
    
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
        
    logging.info(f"Received query: {user_message}")
        
    try:
        # System prompt specifically designed for Indian legal guidance
        system_prompt = """
        You are the AI Legal Action Assistant for India. Your purpose is to provide helpful, structured, actionable legal guidance to Indian citizens based on their queries.
        
        When a user asks a legal question, you MUST structure your response into EXACTLY the following three clear, distinct sections using markdown headers:
        
        ### 1. What You Should Do (Immediate Steps)
        Explain in simple, easy-to-understand terms the immediate, practical, and safe steps the user should take right now to protect themselves and address the issue.
        
        ### 2. Relevant Legal Sections & Laws
        Identify and explain the specific Indian laws, acts, and sections that govern this issue. For example:
        - Motor Vehicles Act (e.g., regarding confiscating vehicle keys).
        - Bharatiya Nyaya Sanhita (BNS) / Indian Penal Code (IPC).
        - Consumer Protection Act, etc.
        Ensure you break down the legalese into simple language for the user.
        
        ### 3. Actions You Can Take (Legal Recourse)
        Detail the formal legal actions the user can execute. Outline how they can:
        - File an FIR/complaint.
        - File a grievance on official portals.
        - Escalate to higher authorities (e.g., SP, Commissioner).
        - Seek professional legal representation.
        
        Guidelines:
        - Be empathetic, reassuring, yet objective.
        - Avoid giving definitive legal conclusions (e.g., "You will definitely win").
        - At the absolute end of your response, append this EXACT text as a disclaimer:
        
        ---
        *Disclaimer: The legal information provided is for educational purposes only and does not constitute formal legal advice. Please consult a licensed advocate for specific legal representation.*
        """
        
        if language != 'English':
            system_prompt += f"\n\nCRITICAL: You MUST respond entirely in the {language} language. Translate the headers and all content accordingly, but maintain the exact 3-part structure."
        
        # groq chat completion call
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.4,
            max_tokens=2500
        )
        
        ai_response = completion.choices[0].message.content
        logging.info("Successfully received response from Groq.")
        return jsonify({'response': ai_response})
        
    except Exception as e:
        logging.error(f"Error processing legal query: {str(e)}")
        return jsonify({'error': f'An error occurred while generating legal guidance: {str(e)}'}), 500

@app.route('/api/tts')
def tts():
    text = request.args.get('text', '')
    lang = request.args.get('lang', 'en')
    
    if not text:
        return jsonify({'error': 'Text is required'}), 400
        
    try:
        logging.info(f"Generating TTS for language: {lang}")
        tts_obj = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts_obj.write_to_fp(fp)
        fp.seek(0)
        return send_file(fp, mimetype='audio/mp3')
    except Exception as e:
        logging.error(f"TTS Error: {str(e)}")
        return jsonify({'error': 'Failed to generate speech'}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
