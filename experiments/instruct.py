from os import system, mkdir, path, rmdir

# Functions for Opening Apps
def openSafari():
  system("open -a Safari")

def openITunes():
  system("open -a iTunes")

def openMessages():
  system("open -a Messages")

def openMail():
    system("open -a Mail")

def openStore():
    system("open -a App\ Store")

def openReminder():
    system("open -a Reminders")

def openCalendar():
    system("open -a Calendar")

def openCalculator():
    system("open -a Calculator")

def openNotes():
    system("open -a Notes")

def openPhotos():
    system("open -a Photos")


# Functions to Close apps

def closeSafari():
    cmd = """osascript -e 'quit app "Safari"' """
    system(cmd)

def closeITunes():
    cmd = """osascript -e 'quit app "iTunes"' """
    system(cmd)


def closeMessages():
    cmd = """osascript -e 'quit app "Messages"' """
    system(cmd)

def closeMail():
    cmd = """osascript -e 'quit app "Mail"' """
    system(cmd)

def closeStore():
    cmd = """osascript -e 'quit app "App\ Store"' """
    system(cmd)

def closeReminder():
    cmd = """osascript -e 'quit app "Reminders"' """
    system(cmd)

def closeCalendar():
    cmd = """osascript -e 'quit app "Calendar"' """
    system(cmd)

def closeCalculator():
    cmd = """osascript -e 'quit app "Calculator"' """
    system(cmd)

def closeNotes():
    cmd = """osascript -e 'quit app "Notes"' """
    system(cmd)

def closePhotos():
    cmd = """osascript -e 'quit app "Photos"' """
    system(cmd)




# Function to create Folders
def createDesktopFolder(str):
    mkdir(path.expanduser("~/Desktop/" + str))

def createDocumentsFolder(str):
    mkdir(path.expanduser("~/Documents/" + str))

def createFolder(des, soc):
    mkdir(path.expanduser("~/" + des + "/" + soc))


# Function to remove Folders
def deleteDesktopFolder(str):
    rmdir(path.expanduser("~/Desktop/" + str))

def deleteDesktopFolder(str):
    rmdir(path.expanduser("~/Documents/" + str))

def deleteFolder(des, soc):
    rmdir(path.expanduser("~/" + des + "/" + soc))
