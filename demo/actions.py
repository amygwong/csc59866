from os import system, mkdir, path, rmdir
from speech_to_text import getUserInput
import appOpen
import instruct
import vol
import cal
import previews
import e_mail
import safari
import tunes
import currentTime, battery

#this file is to handle the actions after classification
def getDetails(info):
    inp = ""
    while inp == "" or inp == -1:
        inp = getUserInput(info)
    print(inp)
    return inp

#function takes the command number and executes the function to do that certain command

def action(com,inp):

    #this is the value for an unknown command
    if com == -1:
        system('say Command not classified please try again')
        print("Command not classified")


    #opening an application
    elif com == 0:
        app = appOpen.checkApp(inp)
        if app == -1:
            system('say could not find the application')
            return ""
        else:
            appOpen.openApp(app[0])
            print(app[1])
            return app[1] +'!'

    #closing an application
    elif com == 1:
        app = appOpen.checkApp(inp)
        if app == -1:
            system('say could not find the application')
            return ""
        else:
            appOpen.closeApp(app[0])
            return app[1] + '!'

    elif com == 2:
        inp = getDetails("What is the name of the folder you would like to delete?")
        instruct.deleteDesktopFolder(inp)
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
        cal.listAllEvents()
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
    elif com == 18:
        instruct.systemLogOut()
    elif com == 19:
        instruct.systemRestart()
    elif com == 20:
        instruct.systemShutDown()
    elif com == 21:
        safari.closeFromLeft()
    elif com == 22:
        safari.closeFromRight()
    elif com == 23:
        safari.copyUrl()
    elif com == 24:
        safari.firstTab()
    elif com == 25:
        safari.lastTab()
    elif com == 26:
        safari.moveLeft()
    elif com == 27:
        safari.moveRight()
    elif com == 28:
        title = getDetails("What is the title of the song you wish to listen to?")
        tunes.playTrack(title)
    elif com == 29:
        currentTime.getTime()
    elif com == 30:
        currentTime.getDate()
    elif com == 31:
        battery.getBatteryPercentage()
    elif com == 32:
        battery.getBatteryStatus()
    return inp
