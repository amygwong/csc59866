#this file is what is executed and contains the loop

from commands import commands
from actions import action
a = commands()
inp = ""
val = -1
while true:
    #NEED TO PUT THE SPEECH INPUT STUFF HERE
    if inp == "quit":
        break
    #handle the command classification    
    val = a.getCommand(inp)
    
    #create function to handle execution
    