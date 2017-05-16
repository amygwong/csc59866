from calcDists import commandList
import os

class commands:
    def __init__(self):
        #this variable stores the possible commands

        files = ["openSafari.txt", "closeSafari.txt","openMessages.txt",
                 "closeMessages.txt", "openNotes.txt", "closeNotes.txt",
                 "upVol.txt", "downVol.txt","setVol.txt", "listEvents.txt",
                 "createFolder.txt", "openImage.txt", "openMail.txt",
                 "closeMail.txt", "syncMail.txt", "readUnreadMail.txt",
                 "createEmailDraft.txt", "sendCurrentMail.txt", "logOut.txt",
                 "restart.txt", "shutDown.txt", "closeFromLeft.txt",
                 "closeFromRight.txt", "copyUrl.txt", "firstTab.txt",
                 "lastTab.txt", "moveLeftTab.txt", "moveRightTab.txt",
                 "playSong.txt"
                ]

        #add the current directory path and trainingData folder to path for opening files
        dir = os.path.dirname(__file__)
        dir = dir + "/trainingData/"
        ind = 0
        for name in files:
            files[ind] = dir + name
            ind = ind +1

        self.comList = []

        #load the files into the commandlist
        for i in files:
            a = commandList()
            a.filename = i
            a.readFile()
            self.comList.append(a)

    #this function is to handle new input and specify the classification
    def getCommand(self,inp):
        maxVal = 0
        maxInd = 0
        for ind,com in enumerate(self.comList):
            newVal = com.getScore(inp)
            #print(ind)
            #print(newVal)
            if newVal > maxVal:
                maxVal = newVal
                maxInd = ind
        if maxVal > .4:
            return maxInd
        else:
            return -1
