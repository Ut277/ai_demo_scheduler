# speak.py

import os
from gtts import gTTS
from playsound import playsound

def speak(text):
    print(f"AI Agent says: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print(f"An error occurred during text-to-speech or playback: {e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)
            print("Temporary audio file removed.")

if __name__ == "__main__":
    # Test the speak function independently
    test_text = "This is a test of the speak function."
    speak(test_text)
