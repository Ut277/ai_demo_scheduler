# listen.py

import speech_recognition as sr

def listen(device_index=None):
    recognizer = sr.Recognizer()
    print("Recognizer initialized.")

    try:
        if device_index is not None:
            microphone = sr.Microphone(device_index=device_index)
            print(f"Using microphone with device_index={device_index}.")
        else:
            microphone = sr.Microphone()
            print("Using default microphone.")

        with microphone as source:
            print("Microphone opened.")
            recognizer.adjust_for_ambient_noise(source)
            print("Adjusted for ambient noise.")
            print("Waiting for customer response...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Audio captured.")
    except Exception as e:
        print(f"An error occurred while capturing audio: {e}")
        return ""

    try:
        response = recognizer.recognize_google(audio)
        print(f"Customer said: {response}")
        return response.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during recognition: {e}")
        return ""

if __name__ == "__main__":
    # Test the listen function independently
    result = listen()
    print(f"Result: {result}")
