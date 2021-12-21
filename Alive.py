#!/usr/bin/env python 

#	Script, that is supposed to be started upon boout-up. Marks start
#	with a Started note, then every minute, time delta is calculated and 
# 	the last line of the logfile is edited and updated. 
# 	features used: file handling, time-delta calculation. 

import time
import os
from time import strftime
from datetime import datetime
import sys
logfile="/home/pi/dev/08-Iamstillalive/logfile.log"

with open(logfile,"a") as log:
	log.write("\n\n"+strftime("%Y-%m-%d %H:%M:%S")+",Started\n"+strftime("%Y-%m-%d %H:%M:%S")+",Alive")
start_date = datetime.strptime(strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
	

while True:
	
	lines = open(logfile, 'r').readlines()
	end_date = datetime.strptime(strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
	new_last_line = "Alive for " + str(abs(end_date-start_date))
	lines[-1] = new_last_line
	open(logfile, 'w').writelines(lines)
	time.sleep(60)
