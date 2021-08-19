# JBLogParser

## About
`JBLogParser` is a log parser of audit and auth.

`JBLogParser` decodes the encrypted data in log files and present it to us.

## Installation

Clone source:
```bash
git clone https://github.com/fatihsencer/JBLogParser.git
cd JBLogParser
python3 JBLogParser.py --help
```

## Usage

`JBLogParser` has the following flags and options (which you can see with the `-h` flag):

* `-h`/`--help`: Show help message and exit
* `-l`/`--logType`: Select log type (Audit or Auth)
* `-f`/`--filename`: Log file or Log files ( e.g. -f logfile1,logfile2,...)
* `-t`/`--type`: Select to type (e.g. USER_CMD, USER_START)
* `-T`/`--time`: Time Range (e.g MM/DD/YYYY-MM/DD/YYYY)

```bash
┌──(root㉿kal')-[~]
└─$ python3 JBLogParser.py --help


Usage: python3 JBLogParser -l [Log Type] -f [filename1,filename2,filename*]

      _ ____  _                ____                          
     | | __ )| |    ___   __ _|  _ \ __ _ _ __ ___  ___ _ __ 
  _  | |  _ \| |   / _ \ / _` | |_) / _` | '__/ __|/ _ \ '__|
 | |_| | |_) | |__| (_) | (_| |  __/ (_| | |  \__ \  __/ |   
  \___/|____/|_____\___/ \__, |_|   \__,_|_|  |___/\___|_|   
                         |___/                               

*-* JB Log Parser. Version 1.0 -- 07.25/2021 *-*

Options:
  -h, --help            show this help message and exit
  -l LOGTYPE, --logType=LOGTYPE
                        Select log type (e.g Audit, auth)
  -f FILE, --filename=FILE
                        Log file or Log files
  -t TYPE, --type=TYPE  Select to type (e.g. USER_CMD, USER_START)
  -T TIME, --time=TIME  Time Range (e.g MM/DD/YYYY-MM/DD/YYYY)
```
