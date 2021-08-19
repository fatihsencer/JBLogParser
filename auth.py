import sys
import re
from datetime import datetime, time

class authLog():
    def __init__(self,logFiles,type,timeRange):
        self.logFiles = logFiles
        self.type = type
        self.timeRange = timeRange


    def fileCheck(self):
        fileNames = self.logFiles.split(',')

        try:
            for x in fileNames:
                open(x,"r")

        except Exception as ex:
            print(ex)
            sys.exit()

    def readLog(self):
        fileNames = self.logFiles.split(',')

        counter = 0
        times = []
        msg = []

        for x in fileNames:
            fileLines = open(x,"r").readlines()

            for y in fileLines:

                ##   TIME   ##
                splitLine = y.strip('\x00').split(' ')
                tempDate = "{} {} {}".format(splitLine[1],splitLine[0],2021)
                date = datetime.strptime(tempDate, "%d %b %Y")

                if self.timeRange:
                    rangeX = self.timeRange.split("-") 
                    lower = rangeX[0].split("/")
                    lowerDate = datetime(int(lower[2]),int(lower[0]),int(lower[1]),0,0,1)
                    upper = rangeX[1].split("/")
                    upperDate = datetime(int(upper[2]),int(upper[0]),int(upper[1]),23,59,59)
                    if date >= lowerDate and date <= upperDate:
                        times.append(str(date))
                    else:
                        continue
                
                else:
                    times.append(str(date))

                #############

                if self.type:
                    if re.search(self.type,y):
                        msg.append(re.findall("(..:..:..)(.*)",y)[0][1].strip())
                        counter += 1
                else:
                    msg.append(re.findall("(..:..:..)(.*)",y)[0][1].strip())
                    counter += 1


        
        if self.type:
            print("Time\t\t\tUID\t\tCommand\t\tPath\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            for x in range(0,counter):
                print(times[x].split(' ')[0]+"\t"+msg[x])
        else:
            print("Type\t\t\tTime\t\t\tUID\tContent\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            for x in range(0,counter):
                print(times[x].split(' ')[0]+"\t"+msg[x])

        print("Total Log = "+str(counter))