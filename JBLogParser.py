#!/usr/bin/env python
#      _ _    _____ _        ___  _
#     (_) |__|___ /| |_ __  / _ \(_)___
#     | | '_ \ |_ \| | '_ \| | | | / __|
#     | | |_) |__) | | |_) | |_| | \__ \
#    _/ |_.__/____/|_| .__/ \___/|_|___/
#   |__/             |_|
#
# Log Parser 07/25/2021

from optparse import OptionParser
from re import findall
import audit
import auth

class startUp():

    def __init__(self):

        self.description = "*-* JB Log Parser. Version 1.0 -- 07.25/2021 *-*"
        self.usage = "Usage: python3 JBLogParser -l [Log Type] -f [filename1,filename2,filename*]"

    def getArg(self):
            argv=OptionParser(description=self.description, usage=self.usage, prog="Log Parser:")
            argv.add_option("-l", "--logType",
                dest="logType",
                help="Select log type (e.g Audit, auth)")

            argv.add_option("-f", "--filename",
                dest="file",
                help="Log file or Log files")     

            argv.add_option("-t", "--type",
                dest="type",
                help="Select to type (e.g. USER_CMD, USER_START)")
            
            argv.add_option("-T", "--time",
                dest="time",
                help="Time Range (e.g MM/DD/YYYY-MM/DD/YYYY)")
            
            (options,arguments)= argv.parse_args()

            if not options.logType:
                argv.error("[-] Please select Log Type.")
            elif not options.file:
                argv.error("[-] Please select Log File")
            else:
                return options

parser = startUp()
argvs = parser.getArg()
argvs.logType = argvs.logType.lower()

if argvs.logType == "audit":
    auditClass = audit.auditLog(argvs.file,argvs.type,argvs.time)
    auditClass.fileCheck()
    auditClass.readLog()

elif argvs.logType == "auth":
    authClass = auth.authLog(argvs.file,argvs.type,argvs.time)
    authClass.fileCheck()
    authClass.readLog()