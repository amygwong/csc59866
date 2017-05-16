
#this file is what is executed and contains the loop

from os import system
from commands import commands
from actions import action
from speech_to_text import getUserInput
import time
import cal

#setting everything up for the loop
a = commands()
inp = ""
val = -1
startTime = time.time()



while True:
    sys_says = "Command me"
    inp = getUserInput(sys_says)

    while inp == "" or inp == -1:
        inp = getUserInput("Try Again")

    #handle quiting case
    if inp == "quit" or inp == "quick":
        break

    #handle the command classification
    val = a.getCommand(inp)
    print(val)
    #do the command
    sent = action(val,inp)
    if sent != "" and val != -1:
        a.comList[val].addCommand(sent)
        a.comList[val].writeToFile()

    if time.time()-startTime > 20:
        #do passive checking here
        print("Passive check now")
        cal.checkForEvents()

        #reset the clock
        startTime = time.time()
