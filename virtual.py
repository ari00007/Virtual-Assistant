import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()  # Remove "alexa" and strip whitespace
            print(command)
    except Exception as e:
        print(f"An error occurred: {e}")
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who ' in command:
        person = command.replace('who the heck is', '').strip()
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("Sorry, I couldn't find any information on that person.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on that person.")
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk('Current date is ' + date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry, I didn\'t understand that command. Please try again.')


while True:
    run_alexa()