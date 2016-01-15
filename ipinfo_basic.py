#!/usr/bin/env python
import subprocess
import re

#tresholds for packets
class trsh:
		HIGH = 50
		MEDIUM = 10
		LOW = 5


#colors
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'



#casting fwlogwatch
fwlogoutput = subprocess.check_output(["fwlogwatch"])  
 
#parsing each line
for line in fwlogoutput.splitlines():

	#check if interesting line
	if ("packet from" in line) or ("packets from" in line):
	
	
		#extracting ip
		ipl = re.findall( '[0-9]+(?:\.[0-9]+){3}', line )
		pcksl = re.findall( '^\d+', line)
		pcks = "-"
		
		#if ip list not empty fetching first occurrence (external ip)
		if len(ipl) > 0:
			
			ip = ipl[0] 
			
			#if ip list is not empty trying to fetch number of packets
			if len(pcksl) > 0:
				pcks = pcksl[0]
			else:
				pcks="-"
		
		else:
				ip = "-"
		
		#geolocating ip
		geoloc = subprocess.check_output(["geoiplookup", ip]).replace("GeoIP Country Edition: ","")
		

		#coloring packets based on tresholds
		ipcks = int(pcks)
		if ipcks >=trsh.HIGH:
				pckcolored=bcolors.RED+pcks+bcolors.ENDC
		elif ipcks>=trsh.MEDIUM:
				pckcolored=bcolors.YELLOW+pcks+bcolors.ENDC
		else:
				pckcolored=bcolors.GREEN+pcks+bcolors.ENDC
		
		#print output
		print "Offending IP: "+ip.ljust(16)+"\t"+"Country: "+geoloc.replace('\n', '').ljust(30)+"\tPcks: "+pckcolored


