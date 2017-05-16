from os import system, path
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
found = -1
found = findOpenImage("gudetama")
print(found)
    
