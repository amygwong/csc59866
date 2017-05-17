from os import system, path
from speech_to_text import getUserInput
import subprocess

# opens a file in Prview with name
def findOpenImage(name):
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
            findcmd = "open -a Preview " + fp
            system(findcmd)
            return 1
        # get the path of file that has the closest match with name
        # file with smallest name length
        else:
            if fpName < dist:
                dis = fpName
                curfp = fp
    findcmd = "open -a Preview " + curfp
    system(findcmd)
    return 1

# calls this when user asks to open an image
def openImage():
    found = -1
    # get name of image
    inp = getUserInput("What is the name of the image")
    while inp == "" or inp == -1 or found == -1:
        inp = getUserInput("Try Again")
        if inp != "" and inp != -1:
            found = findOpenImage(inp)
        if inp == "quit" or found == 1:
            break

def openFile():
    found = -1
    # get name of image
    inp = getUserInput("What is the name of the file")
    while inp == "" or inp == -1 or found == -1:
        inp = getUserInput("Try Again")
        if inp != "" and inp != -1:
            found = findOpenImage(inp)
        if inp == "quit" or found == 1:
            break
#openImage()

