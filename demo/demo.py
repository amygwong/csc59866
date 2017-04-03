from os import system
from commands import commands
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
        print("Oops! Didn't catch that")


a = commands()
inp = ""
sys_says = "Command me"
while True:
    inp = getUserInput(sys_says)
    if inp == "quit":
        break
    if a.getCommand(inp) == -1:
        sys_says = "Command does not exist. Try again."

