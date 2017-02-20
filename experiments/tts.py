from os import system, mkdir, path, rmdir
#system('say Hello world!')
#system('say She Sell Sea Shells by the Sea Shore!')
#system('say How Much Wood Could A Woodchuck Wood If A Woodchuck Wood Chuck Wood!')



#testVar = input("Hi, What is your name?")
#system('say Nice to meet you ' + testVar)


# Functions for Opening Apps

def openSafari():
  system("open /Applications/Safari.app")

def openITunes():
  system("open /Applications/iTunes.app")

def openMessages():
  system("open /Applications/Messages.app")

def openMail():
  system("open /Applications/Mail.app")








# Function to create Folders on Desktop
def createDesktopFolder(str):
    mkdir(path.expanduser("~/Desktop/" + str))





# os.remove() will remove a file.
# os.rmdir() will remove an empty directory.
# shutil.rmtree() will delete a directory and all its contents.

# Function to remove Folders on Desktop
def deleteDesktopFolder(str):
    rmdir(path.expanduser("~/Desktop/" + str))





str = input("Hi, What is your first name?")
system('say Nice to meet you ' + str)
mkdir(path.expanduser("~/Desktop/" + str))
system('say There is a folder with your name on your desktop now.')
system('say Do you see it?')
str2 = input("Do you see it?")
rmdir(path.expanduser("~/Desktop/" + str))
system('say Now it is gone.')
