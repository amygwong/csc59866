
#this file is what is executed and contains the loop

from os import system
from commands import commands
from actions import action
from speech_to_text import getUserInput
import time

#setting everything up for the loop
a = commands()
inp = ""
val = -1
startTime = time.time()



while True:
    sys_says = "Command me"
        #while inp == "" :
    inp = input()
    """inp = getUserInput(sys_says)
    while inp == "" or inp == -1:
        inp = getUserInput("Try Again")
    #handle quiting case    
    if inp == "quit" or inp == "quick":
        break
        """
    #handle the command classification    
    val = a.getCommand(inp)
    print(val)
    #do the command
    action(val)
    print(time.time()-startTime)
    if time.time()-startTime > 120:
        #do passive checking here
        print("Passive check now")
        
        #reset the clock
        startTime = time.time()
    



