from playsound import playsound
import eel

# Playing assistant sound function

@eel.expose  #expose is used when backend function is used for frontend
def playAssistantSound():
    music_dir = "client\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)