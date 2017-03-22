from dist_exp import distScore
from reminders import getUserInput

#This is a class that is meant to hold commands for a type of command
class commandList:

    def __init__(self):
        #this variable stores the list of commands
        self.samples = []
        self.filename = "openFile.txt"
        self.maxSize = 7
        
    #calculate how close the input is to the command
    def getScore(self,inp):
        sum = 0
        for i in self.samples:
            sum = sum + distScore(inp,i)
        return sum/len(self.samples)
        
    #add a command to the command list    
    def addCommand(self,inp):
        #check if the command is already in the list
        for i in self.samples:
            print (distScore(inp,i))
            if inp == i:
                return True
        
        #add the command if the max size isn't reached
        if len(self.samples) < self.maxSize:
            self.samples.append(inp)
            return True
        
        scores = []
        newVal = self.getScore(inp)
        
        #calculate the scores for each value and get max/min value's index
        for sam in self.samples:
            scores.append(self.getScore(sam))
        maxInd = scores.index(max(scores))
        minInd = scores.index(min(scores))
        
        if newVal < scores[minInd]:
            return False
        if newVal > scores[minInd]:
            self.samples[minInd] = inp
            return True
    
    #function to read written file for samples
    def readFile(self):
        f = open(self.filename, 'r')
        self.samples = f.readlines()
        self.samples = [x.strip() for x in self.samples] 
        f.close()
    
    
    #function to write the samples into a file
    def writeToFile(self):
        with open(self.filename, 'w') as f:
            for i in self.samples:
                f.write(i)
                f.write('\n')
            f.close()

    
             
    
#inp =  "Open fold"
a = commandList()
a.readFile()
inp = getUserInput("hello")
print(a.getScore(inp))
print("____________________")
print(a.addCommand(inp))
a.writeToFile()
print(a.samples)