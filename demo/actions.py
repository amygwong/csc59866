from os import system, mkdir, path, rmdir

#this file is to handle the actions after classification

#function takes the command number and executes the function to do that certain command
def action(com):
    
    #this is the value for an unknown command
    if com == -1:
        system('say Command not classified please try again')
        print("Command not classified")
    
    #opening safari
    else if com == 0:
        system("open /Applications/Safari.app")
    else if com == 1:
    else if com == 2:
    else if com == 3:
    else if com == 4:
    else if com == 5:
    else if com == 6: