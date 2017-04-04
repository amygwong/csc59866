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
  system("pkill Safari")

def closeITunes():
  system("pkill iTunes")

def closeMessages():
  system("pkill Messages")

def closeMail():
    system("pkill Mail")

def closeStore():
    system("pkill App\ Store")

def closeReminder():
    system("pkill Reminders")

def closeCalendar():
    system("pkill Calendar")

def closeCalculator():
    system("pkill Calculator")

def closeNotes():
    system("pkill Notes")

def closePhotos():
    system("pkill Photos")




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
