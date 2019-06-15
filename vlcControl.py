
from vlcStatus import *
def vlcControl(action, url, vlcpass):
	import requests, time
	from requests.auth import HTTPBasicAuth
	
	print(action)

	url=url+"?command=pl_"

	if (action == "stop"):
		url = url + "stop"
	elif (action == "play"):
		url = url + "play"
	
	r = requests.get(url, auth=('', vlcpass))
	
	# Wiat for Vlc to react and then check status
	time.sleep(.500)
	getData("state", url, vlcpass) 
def stop():
	pass
