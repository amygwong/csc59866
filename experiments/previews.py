from os import system

def openImage(value):
    findcmd = "mdfind -name " + 
    fpath = system(findcmd)
    print (fpath)
    findcmd = "open -a Preview"
    system(findcmd)

openImage("gudetama cafe")
