import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


# code for writing listing and recognising when mic button is active
# code for converting speak into text 

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source)

        # Time how much time vai listen to user
        audio = r.listen(source, 10, 6)

    # Convert above audio to text
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

# code for opening particular application said by user

@eel.expose
def allCommands():
    query = takecommand()
    print(query)

    if "open" in query:
       from engine.features import openCommand
       openCommand(query)
    else:
        print("not run")