
#this file is what is executed and contains the loop

from os import system
from commands import commands
import speech_recognition as sr
from actions import action
r = sr.Recognizer()
m = sr.Microphone()

a = commands()
inp = ""
val = -1



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


while True:
    sys_says = "Command me"
    inp = getUserInput(sys_says)    
    if inp == "quit":
        break
    #handle the command classification    
    val = a.getCommand(inp)
    action(val)
    #create function to handle execution



