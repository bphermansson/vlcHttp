def getData(what, url, vlcpass):
	import requests
	from requests.auth import HTTPBasicAuth
	import xml.etree.ElementTree as ET 

	r = requests.get(url, auth=('', vlcpass))

	if (r.status_code == 200):
		if __debug__:
			print ("Request succeded")
	else:
		if __debug__:
			print ("Request failed, check your settings")
			exit();

	tree = ET.fromstring(r.text)
	if (what == "track"):
		if __debug__:
			print ("decodeTrack")
		decodeTrack(tree)
	elif (what == "state"):
		getState(tree)
	elif (what == "pl"):
		getPlaylistName(tree)

	# Uncomment to see whole answer from VLC:
	#print (r.text)

#<state>stopped</state>

#<information>
#    <category name="meta">
#        </category>
#    </information>


def getState(tree):
	state = tree.findall("./state")
	if (len(state)!=0):
		for status in state:
			print ("Status: " + status.text)
	else:
		print ("Fetch status error")
	#for status in tree.findall("./state"):
	#	print ("Status: " + status.text)

def getPlaylistName(tree):
	# Playlist name
	pls = tree.findall("./information/category/info/[@name='title']")
	if (len(pls)):
		for station in pls:
			print ("Playlist name: " + station.text)


def decodeTrack(tree):
	# All track data:
	# print ("Decoded data: ")
	# for info in tree.findall('./information/category/info'):
	#    print (info.text)

	# Artist & track
	for track in tree.findall("./information/category/info/[@name='now_playing']"):
	   print ("Current track: " + track.text)


