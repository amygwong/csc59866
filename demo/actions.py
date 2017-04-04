from os import system, mkdir, path, rmdir
import instruct

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
