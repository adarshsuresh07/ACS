
import speech_recognition as sr
import os
def recognize_speech_from_mic(recognizer, microphone):
    with sr.WavFile("genevieve.wav") as source:    
     audio = recognizer.record(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("wait!")
    guess = recognize_speech_from_mic(recognizer, microphone)
    if guess["transcription"]:
        f = open("demo.txt", "w")
    f.write("{}".format(guess["transcription"]))
    f.close()
    if guess["error"]:
            print("ERROR: {}".format(guess["error"]))

