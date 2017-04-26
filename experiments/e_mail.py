import speech_recognition as sr
from os import system, path
import subprocess

r = sr.Recognizer()
m = sr.Microphone()

# list of all the accounts in Mails
def getMailAccounts():
    cmd = """osascript -e'tell application "Mail"
        name of every account
        end tell'"""
    return system(cmd)

# create a new email draft with inputs
# attachment should be the full path of the file being attached
# ADD SENDER OPTION
def newEmail(subject, body, recipient, attachment):
    # given subject and body, recipient and attachment missing
    if recipient == "" and attachment == "":
        cmd = """ osascript -e 'tell application "Mail"
            make new outgoing message with properties {visible:true, subject:"%s", content:"%s"}
        end tell'""" % (subject, body)
    # given subject, body and attahcment, recipient missing
    elif recipient == "":
        cmd = """ osascript -e 'tell application "Mail"
            make new outgoing message with properties {visible:true, subject:"%s", content:"%s"}
            tell result
                make new attachment with properties {file name:"%s"}
            end tell
        end tell'""" % (subject, body, attachment)
    # given subject, body, and recipient, attachment missing
    elif attachment == "":
        cmd = """ osascript -e 'tell application "Mail"
            make new outgoing message with properties {visible:true, subject:"%s", content:"%s"}
            tell result
                make new to recipient with properties {address:"%s"}
            end tell
            end tell'""" % (subject, body, recipient)
    # given all inputs
    else:
        cmd = """ osascript -e 'tell application "Mail"
            make new outgoing message with properties {visible:true, subject:"%s", content:"%s"}
            tell result
            make new to recipient with properties {address:"%s"}
            make new attachment with properties {file name:"%s"}
            end tell
            end tell'""" % (subject, body, recipient)
    system(cmd)
# sends the draft email that was most recently created
def sendCurrent():
    cmd = """ osascript -e 'tell application "Mail"
        set newMessage to item -1 of ((every outgoing message))
        tell newMessage
            send
        end tell
        end tell'"""
    system(cmd)

# updates inbox with new mail
def checkNew():
    cmd = """osascript -e'tell application "Mail"
        check for new mail
        end tell'"""
    system(cmd)

def emailChoices(value):
    if value == "open mail":
        system("open -a Mail")
    elif value == "close mail":
        system("pkill mail")
    elif value == "check mail":
        checkNew()
    elif value == "create draft":
        recipient = getUserInput("Who is the recipient?")
        recipient = editAddress(recipient)
        print(recipient)
        subject = getUserInput("What is the subject line?")
        file = getUserInput("Do you want to attach a file?")
        if file == "yes":
            file = getUserInput("What is called?")
            filepath = findFile(file)
        else:
            file = ""
        content = getUserInput("What is the content?")
        newEmail(subject, content, recipient, file)
        system('say Please check and edit. If correct say send email')
    elif value == "send email":
        sendCurrent()
    else:
        pass

def editAddress(input):
    input = input.replace(" ","")
    at_position = input.rfind("at")
    if at_position == -1:
        return -1
    input = input[:at_position] + "@" + input[at_position+2:]
    return input.lower()

# get filepath of file
def findFile(name):
    # get all paths of files with value in its name
    fpath = subprocess.check_output("mdfind -name " + name, shell=True)
    fpath = fpath.decode("utf-8")
    flist = fpath.split()
    
    # no files found
    if len(flist) == 0:
        return -1

    dist = len(path.splitext(path.basename(flist[0]))[0])
    curfp = flist[0]
    for fp in flist:
        fpName = len(path.splitext(path.basename(fp))[0])
        
        # open file with the exact name
        if fpName == len(name):
            return fp
        # get the path of file that has the closest match with name
        # file with smallest name length
        else:
            if fpName < dist:
                dis = fpName
                curfp = fp
    return curfp

def getUserInput(input):
    system('say ' + input)
    with m as source: audio = r.listen(source)
    try:
        value = r.recognize_google(audio)
        print("You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")

#checkNew()
#newEmail("","","","")
"""
try:
    cont = True
    while cont:
        value = getUserInput("Command me")
        emailChoices(value)
        if value == "no":
            cont = False
except KeyboardInterrupt:
    pass
    """
