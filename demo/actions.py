from os import system, mkdir, path, rmdir
from speech_to_text import getUserInput
import instruct
import vol
import cal

#this file is to handle the actions after classification

#function takes the command number and executes the function to do that certain command
def action(com):
    
    #this is the value for an unknown command
    if com == -1:
        system('say Command not classified please try again')
        print("Command not classified")
    
    #opening safari
    elif com == 0:
        instruct.openSafari()
    elif com == 1:
       instruct.closeSafari()
    elif com == 2:
        instruct.openMessages()
    elif com == 3:
        instruct.closeMessages()    
    elif com == 4:
        instruct.openNotes()
    elif com == 5:
        instruct.closeNotes()
    elif com == 6:
        vol.increaseVolume()
    elif com == 7:
        vol.decreaseVolume()
    elif com == 8:
        print("Work in progress atm")
    elif com == 9:
        cal.listEvents()
        print("Work in progress atm")
    elif com == 10:
        inp = ""
        while inp == "" or inp == -1:
            inp = getUserInput("What should the folder be named?")
        print(inp)
        instruct.createDesktopFolder(inp)