from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

def speak(say):
    tts = gTTS(say)
    tts.save('tts.mp3') 
    playsound('tts.mp3')
    os.remove('tts.mp3')


r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("minimum energy threshold: {}".format(r.energy_threshold))
    print("Say something")
    with m as source: 
        audio = r.listen(source)
    print("Got it! Now to recognize it...")
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print((value).encode("utf-8"))
        else:  # this version of Python uses unicode for strings (Python 3+)
            print(value)
    except sr.UnknownValueError:
        print("Didn't catch that")
    except sr.RequestError as e:
        print("Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
speak(value)
