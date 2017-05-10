from os import system
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()

# system says the input argument and returns the spoken user input as text

def getUserInput(input):
    system('say ' + input)
    return recorded()

def recorded():
    name = "poop"
    value = ""
    command = ""
    while command == "" and name not in value:
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            value = str(r.recognize_google(audio))
            print("You said {}".format(value))
            if name in value:
                command = value[value.find(name)+len(name):]
        except sr.UnknownValueError:
            print("dsfDSAF")
            return -1
    return command

"""
def getUserInput(input):
    system('say ' + input)
    with m as source: 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        value = r.recognize_google(audio)
        print("You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("dsfDSAF")
        return -1
"""
