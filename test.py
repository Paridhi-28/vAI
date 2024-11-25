import struct
import time
import pvporcupine
import pyaudio


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # pre trained keywords
        porcupine = pvporcupine.create(keywords = ["jarvis", "alexa"])
        paud = pyaudio.Pyaudio()
        audio_stream = paud.open(
            rate = porcupine.sample_rate,
            channels = 1,
            format  = pyaudio.paInt16,
            input = True,
            framers_per_buffer = porcupine.frame_length
        )

        # loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)

            # processing keyword come from mic
            keyword_index = porcupine.process(keyword)

            # checking first keyword detected or not 
            if keyword_index >=0 :
                print("Hotword detected")

                # pressing shortcut key window + v
                import pyautogui as autogui #python automation lib ie user does not require to press win + j key it will press virtually by this lib
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate() 


hotword()