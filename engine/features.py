from playsound import playsound
import eel

# Playing assistant sound function

@eel.expose  #expose is used when backend function is used for frontend
def playAssistantSound():
    music_dir = "client\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("not found")
