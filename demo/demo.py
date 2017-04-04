
#this file is what is executed and contains the loop

from os import system
from commands import commands
from actions import action
from speech_to_text import getUserInput

a = commands()
inp = ""
val = -1

while True:
    sys_says = "Command me"
    inp = getUserInput(sys_says)    
    if inp == "quit":
        break
    #handle the command classification    
    val = a.getCommand(inp)
    action(val)
    #create function to handle execution



