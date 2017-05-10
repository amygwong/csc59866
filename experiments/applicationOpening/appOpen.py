from os import listdir, system
import re

#open an application with the name of app
def openApp(app):
    system("open -a \"" + app + "\"")
    
    #closes an application of the name app
def closeApp(app):
    system("pkill " + app)
    
#check if an application name appears in the command
def checkApp(comm):

    #go through applications and strip '.app'
    for i in listdir('/Applications'):
        if i.endswith('.app'):
            i = i[:-4]
            
        #change to return the index here ------------------------
        #check to see if there is a match
        if i.lower() in comm:
            print("yay")
            return i
        
        appName = re.findall('[A-Z][a-z]*', i)
        appName = " ".join(appName)
        print(appName)
    #return false if there are no matches has been found
    print("nothing found")
    return -1


    
k = checkApp("open virtual box please")
print (k)
if k != -1:
    closeApp(k)