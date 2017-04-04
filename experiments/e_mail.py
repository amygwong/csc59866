from os import system

def emailChoices(value):
    if value == "open mail":
        system("open -a Mail")
    elif value == "close mail":
        system("pkill mail")
    else:
        pass

#def getAccounts:
#    pass
        
        
#emailChoices("open mail")

#osascript -e'tell application "Mail" to name every account end tell'
