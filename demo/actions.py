from os import system, mkdir, path, rmdir
from speech_to_text import getUserInput
import instruct
import vol
import cal
import previews
import e_mail

#this file is to handle the actions after classification
def getDetails(info):
    np = ""
    while inp == "" or inp == -1:
        inp = getUserInput(info)
    print(inp)
    return inp

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
        inp = getDetails("What should the folder be named?")
        instruct.createDesktopFolder(inp)
    elif com == 11:
        previews.openImage()
    elif com == 12:
        instruct.openMail()
    elif com == 13:
        instruct.closeMail()
    elif com == 14:
        e_mail.syncMail()
    elif com == 15:
        e_mail.readUnreadMail()
    elif com == 16:
        recipient = getDetails("Who is the recipient?")
        recipient = e_mail.editAddress(recipient)
        subject = getDetails("What is the subject line?")
        file = getUserInput("Do you want to attach a file? yes or no?")
        if file == "yes":
            file = getUserInput("What is called?")
            filepath = findFile(file)
        else:
            file = ""
        content = getDetails("What is the content?")
        e_mail.newEmail(subject, content, recipient, file)
        system('say Please check and edit. If correct say send mail')
    elif com == 17:
        e_mail.sendCurrentMail()



