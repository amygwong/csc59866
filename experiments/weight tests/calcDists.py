from dist_exp import distScore

#This is a class that is meant to hold commands for a type of command
class commandList:

    def __init__(self):
        #this variable stores the list of commands and 
        #the following stores the number of occurances
        self.samples = []
        self.occur = []
        self.filename = "openFile.txt"
        self.maxSize = 10
        self.maxOccur = 20
        self.occurSum = 0
        
    #calculate how close the input is to the command
    def getScore(self,inp):
        sum = 0
        
        for ind, i in enumerate(self.samples):
            sum = sum + (distScore(inp,i)*(1+.1*(self.occur[ind]/self.occurSum)))
        return sum/len(self.samples)
        
    #add a command to the command list    
    def addCommand(self,inp):
        for ind,i in enumerate(self.samples):
            #print (distScore(inp,i))
            
            #check if the command is already in the list
            if inp == i:
                #if it is then add to the occurrences, if its not above the threshold
                if self.occur[ind] < self.maxOccur:
                    self.occur[ind] = self.occur[ind]+1 
                    self.occurSum = self.occurSum+1
                return True
        
        #add the command if the max size isn't reached
        #add an occurrence of 1 in this case
        if len(self.samples) < self.maxSize:
            self.samples.append(inp)
            self.occur.append(1)
            self.occurSum = self.occurSum+1
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
            self.occurSum = self.occurSum+1
            return True
    
    #function to read written file for samples
    def readFile(self):
        f = open(self.filename, 'r')
        self.samples = f.readlines()
        self.samples = [x.strip() for x in self.samples]
        
        #go through each line and pull the number out and put it into occur
        for lineNum,line in enumerate(self.samples):
            #check to see if the next value is a number
            #if it is remove 2 numbers from string and stor in occur
            if self.samples[lineNum][-2:].isdigit():
                self.occur.append(int(line[-2:]))
                self.samples[lineNum] = self.samples[lineNum][:-3]
            else:
                self.occur.append(int(line[-1]))
                self.samples[lineNum] = self.samples[lineNum][:-2]
            
        #sum the value of occurrences
        self.occurSum = sum(self.occur)
            
        #close the file
        f.close()
    
    
    #function to write the samples into a file
    def writeToFile(self):
        with open(self.filename, 'w') as f:
            for ind,i in enumerate(self.samples):
                f.write(i)
                f.write(" ")
                f.write(str(self.occur[ind]))
                f.write('\n')
            f.close()
            
a = commandList()
a.readFile()
a.addCommand("open the file please")
print (a.occurSum)
print(a.samples)
print(a.occur)
a.writeToFile()
