import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            return command
    except Exception:
        return ""


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        pyttsx3.speak("Good Morning! How can I help you?")

    elif 12 <= hour < 18:
        pyttsx3.speak("Good Afternoon! What can I do for you?")

    else:
        pyttsx3.speak("Good Evening! How may I assist you?")


def run_jarvis():
    command = take_command()
    if not command:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'search' in command:
        search1 = command.replace('search', '')
        pywhatkit.search(command)
        google = wikipedia.summary(search1, sentences=2)
        talk(google)
        print(google)
    elif any(k in command for k in ['who', 'what', 'where']):
        person = command
        for kw in ['who', 'what', 'where']:
            person = person.replace(kw, '')
        info = wikipedia.summary(person.strip(), sentences=2)
        talk(info)
        print(info)
    elif any(k in command for k in ['funny', 'joke', 'sarcastic', 'silly', 'bored']):
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('Could you please repeat that?')


while True:
    wishme()
    run_jarvis()
