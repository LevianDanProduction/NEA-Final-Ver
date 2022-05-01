import strOP


class Assembler():

    def __init__(self):
        self.converted = None
        self.currentCode = []
        self.convertedCode = []
        self.currentLine = []
        self.currentPart = None
        self.convertedLines = []

    def clear(self):
        self.convertedCode = []
        self.convertedLines = []

    def splitTextField(self, text):
        self.currentCode = text

    def fillLine(self):
        while len(self.currentLine) < 5:
            if len(self.currentLine) > 3:
                break
            else:
                self.currentLine.append("")

    def convertIntoBin(self):
        self.clear()
        for line in self.currentCode:
            self.currentLine = line.split()
            print(self.currentLine)
            self.fillLine()
            print(self.currentLine)
            self.convertedLines.append(strOP.findOP(self.currentLine[0],self.currentLine[1],self.currentLine[2],self.currentLine[3]))
            print(self.convertedLines[-1])
            print("----")
            listforconvert = strOP.toBytes(self.convertedLines[-1],self.currentLine)
            if listforconvert == None:
                continue
            for x in (listforconvert):    
                self.convertedCode.append(x)
            print(self.convertedCode)


    def binDump(self):
        return self.convertedCode
    

    