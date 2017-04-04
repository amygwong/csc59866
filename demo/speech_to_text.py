from os import system
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()

# system says the input argument and returns the spoken user input as text
def getUserInput(input):
    system('say ' + input)
    with m as source: audio = r.listen(source)
    try:
        value = r.recognize_google(audio)
        print("You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("dsfDSAF")
        return -1
