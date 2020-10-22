# git url 
# https://github.com/semirworkuaman/termux-speech-recognition

import subprocess
import shlex
import json
from termcolor import colored
import sys
from time import sleep
import time
c=False
while True:
	speech = subprocess.Popen(
             "termux-speech-to-text",
             stdout=subprocess.PIPE)
	#print c

	c= speech.stdout.readline()
	res=c.replace("\n","")
	print colored(res,"cyan")
	print "-"*30
	if res == 'stop':
		break
		sys.exit()


