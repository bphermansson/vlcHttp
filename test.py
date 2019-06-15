#!/usr/bin/env python
import sys
from vlcStatus import *
from vlcControl import *
import config as cfg

# No debug messages: python -O test.py

def main():
	url = cfg.vlcserver['host']+":"+cfg.vlcserver['port']+"/requests/status.xml"
	vlcpass=cfg.vlcserver['pass']

	if len(sys.argv) == 2: 
		if (str(sys.argv[1]) == "s"):
			vlcControl("stop", url, vlcpass) 
		elif (str(sys.argv[1]) == "p"):
			vlcControl("play", url, vlcpass) 
		elif (str(sys.argv[1]) == "gt"):
			getData("track", url, vlcpass) 
		elif (str(sys.argv[1]) == "gs"):
			getData("state", url, vlcpass) 
		elif (str(sys.argv[1]) == "gpl"):
			getData("pl", url, vlcpass)   

	else:
		print ("Usage:")		

if __name__== "__main__":
   main()
