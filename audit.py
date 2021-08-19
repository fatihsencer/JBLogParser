import sys
import re
from datetime import date, datetime, time

class auditLog():
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
        uid = []
        cmd = []
        msg = []
        times = []
        xType = []
        cwd = []

        for x in fileNames:
            fileLines = open(x,"r").readlines()
            for y in fileLines:

                ##   TIME   ##
                                 
                date = datetime.fromtimestamp(int(re.findall("audit\((.*?)\.",y)[0]))

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

                    if self.type == "USER_CMD":
                        if re.search(self.type, y):
                            counter += 1
                            uid.append(re.findall("UID=\"(.*?)\" ",y)[0])
                            cwd.append(re.findall("cwd=\"(.*?)\"",y)[0])
                            hexText = re.findall("cmd=(.*?) ",y)[0]
                            if re.search("\"",hexText):
                                cmd.append(hexText[1:-1])
                            else:
                                cmd.append(bytes.fromhex(hexText).decode('UTF-8'))
                        else:
                            continue
                        
                    else:

                        if re.search(self.type, y):
                            tempType = re.findall("type=(.*?) ",y)[0]

                            if tempType == "BPF":
                                continue

                            xType.append(tempType)
                            counter += 1
                            uid.append(re.findall("UID=\"(.*?)\"",y)[0])
                            
                            withoutMSG = ["LOGIN","DAEMON_START","CONFIG_CHANGE","ANOM_ABEND"]

                            if tempType in withoutMSG:
                                msg.append(" ")
                            else:
                                msg.append(re.findall("msg='(.*?)'",y)[0])

                else:
                    tempType = re.findall("type=(.*?) ",y)[0]

                    if tempType == "BPF":
                        continue

                    xType.append(tempType)
                    counter += 1
                    uid.append(re.findall("UID=\"(.*?)\"",y)[0])
                    
                    withoutMSG = ["LOGIN","DAEMON_START","CONFIG_CHANGE","ANOM_ABEND"]

                    if tempType in withoutMSG:
                        msg.append(" ")
                    else:
                        msg.append(re.findall("msg='(.*?)'",y)[0])    


        
        if self.type == "USER_CMD":
            print("Time\t\t\tUID\t\tCommand\t\tPath\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            for x in range(0,counter):
              print(times[x]+"\t"+str(uid[x])+"\t"+cmd[x]+" \t|\t"+cwd[x])
        else:
            print("Type\t\t\tTime\t\t\tUID\tContent\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            for x in range(0,counter):
                print(xType[x]+"\t"+times[x]+"\t"+uid[x]+"\t"+msg[x])
        print("Total Log = "+str(counter))