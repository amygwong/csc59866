from calcDists import commandList

class commands:
    def __init__(self):
        #this variable stores the possible commands
        files = ["openFile.txt", "addEvent.txt"]
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
            print(newVal)
            if newVal > maxVal:
                maxVal = newVal
                maxInd = ind
        if maxInd > .4:
            print (self.comList[maxInd].addCommand(inp))
            self.comList[maxInd].writeToFile()
            return maxInd
        else:
            return -1
    
    

a = commands()
print(a.getCommand("can you add a new event"))
