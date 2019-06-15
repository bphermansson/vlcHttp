This is a package to control VLC via Http.
The script fetches information from the VLC media player and also can control the player.  
For this to work VLC has to be started with it's http-server activated, this can be done with a command line like this:

vlc --aout=alsa --alsa-audio-device="hw:0,0" --daemon --syslog -I http --http-port 8080 --http-password <password>

Where you select the password yourself. Then, create a file called "config.py" with the following content:

vlcserver = {
'host': 'http://192.168.1.190',
'port': '8080',
'pass': 'password'
}

Where 'password' is the password for the VLC server.

(C) Patrik Hermansson
