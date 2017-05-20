
#this file is what is executed and contains the loop

from os import system
from commands import commands
from actions import action
from speech_to_text import getUserInput
import time
from e_mail import psyncMail
from battery import checkBattery
import cal

commandList = [(2,"delete a folder"),(3,"create a new event"),(6,"increase volume"), 
                (7,"decrease volume"),(9,"list events"),(10,"create a folder"), 
                (11,"open image"),(12,"open file"),(13,"find gender of voice"),
                (14,"get new mail"),(15,"read new mail"),(16,"create a mail draft"),
                (17,"send mail"),(18,"log out"),(19,"restart computer"),
                (20,"shut down computer"),(21,"close from left tab"),
                (22,"close from right tab"),(23,"copy URL"),(24,"select first tab"),
                (25,"select last tab"),(26,"move to the left tab"),
                (27,"move to the right tab"),(28,"play a song"),(29,"what time is it"),
                (30,"what is today's date"),(31,"battery percentage"),(32,"battery status")]

# gets the user's version of the command phrase
def trainCommand(com):
    pair = [item for item in commandList if item[0] == com]
    inp = getUserInput("please repeat a variation of the command" + pair[0][1])
    return inp

def getCommandNumber():
    done = False
    while done == False:
        try:
            system('say Type the number that corresponds with the command you want to train from the list above and press Enter.')
            cnum = int(input("Type the number that corresponds with the command you want to train from the list above and press Enter. "))
            print(cnum)
            if (cnum == 0 or cnum == 1 or cnum == 4 or cnum == 5 or cnum == 8 or cnum >= 33):
                done = False
            else:
                done = True
        except ValueError:
            done = False
    return cnum

#setting everything up for the loop
a = commands()
inp = ""
val = -1
startTime = time.time()
while True:
    system('say Press T, then Enter to do training. Otherwise, press Enter to do a command')
    k = input("Press T, then Enter to do training. Otherwise, press Enter to do a command. ")
    if (k == 't'):
        for num, comm in commandList:
            print (str(num)+" : "+comm) 
        val = getCommandNumber()
        system('say Start Training')
        print("Start Training")
        for i in range(3):
            uinput = trainCommand(val)
            a.comList[val].addCommand(uinput)
            a.comList[val].writeToFile()
        system('say Training Completed')    
        print("Training Completed")
    else:
        sys_says = "Command me"
        inp = getUserInput(sys_says)

        while inp == "" or inp == -1:
            inp = getUserInput("Try Again")
        if inp == -2:
            print("ddsfsdaflkasjfd")

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

    if time.time()-startTime > 200000:
        #do passive checking here
        print("Passive check now")
        cal.checkForEvents()
        psyncMail()
        checkBattery()
        print("Passive check done")

        #reset the clock
        startTime = time.time()
    input("Press Enter to Continue")


"""
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

    if time.time()-startTime > 200000:
        #do passive checking here
        print("Passive check now")
        cal.checkForEvents()
        psyncMail()
        checkBattery()
        print("Passive check done")

        #reset the clock
        startTime = time.time()
    input("Press Enter to Continue")
"""
