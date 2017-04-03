from os import system, mkdir, path, rmdir

#this file is to handle the actions after classification

#function takes the command number and executes the function to do that certain command
def action(com):
    
    #this is the value for an unknown command
    if com == -1:
        system('say Command not classified please try again')
        print("Command not classified")
    
    #opening safari
    elif com == 0:
        system("open /Applications/Safari.app")
    elif com == 1:
        print("Bad")
    elif com == 2:
        print("Bad")
    elif com == 3:
        print("Bad")    
    elif com == 4:
        print("Bad")
    elif com == 5:
        print("Bad")
    elif com == 6:
        print("Bad")