from os import system

def emailChoices(value):
    if value == "open mail":
        system("open -a Mail")
    elif value == "close mail":
        system("pkill mail")
    else:
        pass

# list of all the accounts in Mails
def getMailAccounts():
    cmd = """osascript -e'tell application "Mail"
        name of every account
        end tell'"""
    return system(cmd)

# create a new email draft with inputs
# attachment should be the full path of the file being attached
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

# updates inbox with new mail
def checkNew():
        cmd = """osascript -e'tell application "Mail"
        check for new mail
        end tell'"""
    system(cmd)

checkNew()
#newEmail("","","","")
#emailChoices("open mail")
