# Virtual-Assistant

Alexa-like Python Voice Assistant
# Overview
This is a simple Python-based voice assistant that responds to voice commands using the speech_recognition and pyttsx3 libraries. It can play YouTube videos, tell the current time and date, fetch information from Wikipedia, tell jokes, and respond to fun questions.

The wake word for the assistant is "Alexa".

# Features
Play YouTube videos using pywhatkit

Tell the time in a 12-hour format

Tell the date

Fetch brief Wikipedia summaries

Tell random jokes using pyjokes

Fun responses to certain personal questions

# Requirements
Make sure you have Python 3.6+ installed.

Install the dependencies by running:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
You also need:

Microphone access for speech input

Internet connection for YouTube and Wikipedia features

# How It Works
Listening for Commands

The assistant listens for speech input using the speech_recognition library.

It waits for the keyword "Alexa" and processes the rest of the command.

Command Processing

play <song> → Plays the requested song/video on YouTube.

time → Tells the current time.

date → Tells the current date.

who is <person> → Fetches a one-sentence summary from Wikipedia.

joke → Tells a random joke.

are you single → Fun response.

Speaking the Response

Uses pyttsx3 for text-to-speech output.

# Code Structure
bash
Copy
Edit
voice_assistant.py   # Main script containing all logic
Main functions:

talk(text) → Speaks text aloud.

take_command() → Listens to and processes voice input.

run_alexa() → Executes commands based on the recognized speech.

# Running the Program
Run the script:

bash
Copy
Edit
python voice_assistant.py
The assistant will keep listening and responding until you manually stop it.
