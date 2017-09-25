#!/usr/bin/python

import os
import commands
import getopt
import sys
import time
import subprocess
import logging
# encoding: utf-8


base_dir=os.path.dirname(os.path.abspath(__file__))
base_filename=os.path.basename(os.path.abspath(__file__))
file_name=base_filename.split(".")[-2]
configfile=base_dir+"/"+file_name+".cfg"
nowtime=time.strftime("%Y-%mtime-%d %H:%M:%S",time.localtime())
##date=time.strftime("%Y-%m-%d",time.localtime())
#date=time.strftime("%a %b %d %Y ",time.localtime())
date=time.strftime("%b %d",time.localtime())
today=time.strftime("%Y-%m-%d",time.localtime())
log_file=base_dir+"/"+file_name+date+".log"

print "today is ",date
history_log="/tmp/alert.log-"+today
cmd=r"cat /etc/sysconfig/network-scripts/ifcfg-eth0|grep 'IPADDR'|awk -F '=' '{print $2}'"
stat,result=map(str,commands.getstatusoutput(cmd))
local_ip=result


logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s", filename=log_file, filemode='w')

def usage():
    print "-h for help"
    print "-f filename"

def getopts():
    logging.info("    getops function begin")
    try:
      opt,argv=getopt.getopt(sys.argv[1:],'hf:')
    except:
       usage()
    for k,v in opt:
        if k=='-h':
            usage()
            return 0
        if k=='-f':
            logfile=v
    logs=logfile.strip()
    if not (logs and os.path.isfile(logs)):
        print "log file is not exitst"
        usage()
        return 1
    return logs
def main():
    logging.info("Begin start logfile monitor check")
    logs=getopts()
    cmd = ('tail', '-f',logs)
    output=subprocess.Popen(cmd,stdout=subprocess.PIPE)
    ##get keyword from config file
    keywordmap={}
    with open(configfile) as lines:
        for line in lines:
            print line
            k,v=line.strip().split(':')
            keywordmap[k]=v
    while True:
        line=output.stdout.readline()
        print "line is ",line
        if not line:
            time.sleep(0.01)
            sys.exit(0)
            continue
        line=line.strip().decode('utf-8')
        if line.find(date) ==-1:
            time.sleep(1)
            continue
        for (k,v) in keywordmap.items():
            if line.find(v)==-1:
                continue
            if line.find(v)>-1:
                f=open(history_log,'a')
                f.write(line)
                alert_info=local_ip+line
                print alert_info
                time.sleep(3)

if __name__ == '__main__':
    sys.exit(main())
