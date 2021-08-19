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
┌──(root㉿kali)-[~]
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

## Example

````bash

┌──(root㉿kali)-[~]
└─$ python3 JBLogParser.py -l audit -f /var/log/audit/audit.log -t USER_CMD

Time                    UID             Command         Path
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
2021-08-19 09:48:22     <username>        systemctl enable auditd.service
2021-08-19 09:48:22     <username>        ls /var/log/
2021-08-19 09:48:22     <username>        ls /var/log/audit
2021-08-19 09:48:22     <username>        cp /var/log/audit/audit.log .
2021-08-19 09:48:22     <username>        chown <username> audit.log
2021-08-19 09:48:22     <username>        python3 JBLogParser.py -l audit -f logFiles/audit.log -t USER_CMD

--

┌──(root㉿kali)-[~]
└─$ python3 JBLogParser.py -l audit -f /var/log/audit/audit.log -t USER_CMD

Time                    UID             Command         Path
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
2021-08-17      kali CRON[1582]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
2021-08-17      kali CRON[1582]: pam_unix(cron:session): session closed for user root
2021-08-17      kali CRON[1778]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
2021-08-17      kali CRON[1778]: pam_unix(cron:session): session closed for user root
```
