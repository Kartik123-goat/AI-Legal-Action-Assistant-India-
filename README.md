# AI Legal Action Assistant (India)

## Overview

AI Legal Action Assistant is a multilingual AI-powered web application designed to help Indian citizens understand their legal rights and possible legal actions in real-life situations. Users can describe their problem in detail through text or voice input, and the system provides structured legal guidance instantly.

The platform is built to simplify legal awareness by giving users:

* Immediate actions they should take
* Relevant Indian legal sections and laws
* Future legal steps and legal recourse options

The application supports multiple Indian languages including:

* English
* Hindi
* Marathi
* Telugu

---

# Features

## AI-Powered Legal Guidance

Users can describe any legal situation such as:

* Police-related issues
* Landlord disputes
* Online fraud
* Workplace harassment
* Domestic violence
* Property disputes
* Cybercrime cases

The AI analyzes the situation and generates structured legal guidance.

---

## Structured Legal Response

The system provides responses in 3 major sections:

### 1. Immediate Actions

Explains what the user should do immediately after the incident.

### 2. Relevant Legal Sections

Provides applicable Indian legal sections and acts such as:

* IPC/BNS Sections
* Motor Vehicles Act
* Cyber Laws
* Consumer Protection Laws

### 3. Future Legal Steps

Suggests possible legal actions users can take in the future.

---

# Multilingual Support

The platform supports multiple regional languages for better accessibility:

* English
* Hindi
* Marathi
* Telugu

Users can select their preferred language before asking questions.

---

# Voice Interaction

The application includes voice-enabled interaction features:

* Speech-to-Text using Web Speech API
* Text-to-Speech for AI responses
* Regional language audio support using Google Text-to-Speech (gTTS)

This improves accessibility for users who are not comfortable typing.

---

# User Interface

The frontend is designed with a modern glassmorphism UI and includes:

* Animated welcome screen
* Interactive legal topic cards
* Responsive mobile-friendly design
* Smooth transitions and animations
* Dark premium theme

---

# Tech Stack

## Backend

* Python
* Flask
* Groq API
* Llama 3.1 8B Instant
* Google Text-to-Speech (gTTS)

## Frontend

* HTML
* Tailwind CSS
* JavaScript
* Marked.js
* Web Speech API

---

# Project Workflow

## Step 1 — User Describes Situation

The user enters their legal problem using:

* Text input
* Voice input
* Predefined legal issue cards

---

## Step 2 — AI Processing

The backend sends the user query to the Llama 3.1 AI model through Groq API with a structured legal prompt.

---

## Step 3 — Legal Analysis

The AI analyzes the situation and generates:

* Immediate actions
* Relevant legal sections
* Future legal options

---

## Step 4 — Response Display

The response is formatted and displayed in a user-friendly chat interface.

---

## Step 5 — Voice Output

Users can listen to the AI-generated response in their selected language using Text-to-Speech functionality.

---

# Folder Structure

```bash
AI-Legal-Assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   ├── index.html
│   ├── chat bot video.mp4
│   └── chat bot.png
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI-Legal-Assistant.git
```

## Move to Project Folder

```bash
cd AI-Legal-Assistant
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Run the Project

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Future Improvements

* PDF legal report generation
* User authentication system
* FIR document assistance
* Legal chatbot memory
* More Indian language support
* Lawyer contact integration
* Mobile application version

---

# Disclaimer

This platform is built for educational and informational purposes only and does not replace professional legal advice from certified lawyers or legal authorities.


