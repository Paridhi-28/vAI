import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME 

# Playing assistant sound function

@eel.expose  #expose is used when backend function is used for frontend
def playAssistantSound():
    music_dir = "client\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


# code for opening application by voice sending voice message.

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("not found")
