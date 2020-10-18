#Author : Rimes App
# Git Repo : https://github.com/semirworkuaman/termux-demos/sl4a-broadcast-receiver




import android
import socket
from json import loads

droid = android.Android()
# Data Parser
def parseEvent(line):
	out=loads(line)
	out.update(loads(out['data']))
	return out
#For reading phone state
ACTION1='android.intent.action.PHONE_STATE'
# For intercepting SMS Messages
ACTION2='android.provider.Telephony.SMS_RECEIVED'
# Register for the broadcasts above
droid.eventRegisterForBroadcast(ACTION1, False)
droid.eventRegisterForBroadcast(ACTION2, False)
# To view the categories we registered for
reg_cat=droid.eventGetBrodcastCategories()
print reg_cat

# Start the event dispatcher
p=droid.startEventDispatcher().result

# Creat a socket form incoming
# broadcasts we registered to
s=socket.socket()

# Connect to the socket
s.connect(('localhost',p))
# Create a file for reading and writting
# broadcasts
f=s.makefile()

while True:
    res = parseEvent(f.readline())
    print res
    # Here is where you put actions to
    # be taken upon the received broadcasts
    # Ex - You can send notifications to  
    # other devices or you can read 
	# messages using ttsSpeak.
# Unregister from the broadcasts
droid.eventUnregisterForBroadcast(ACTION1)
droid.eventUnregisterForBroadcast(ACTION2)
# Stop Dispatcher
droid.stopEventDispatcher()