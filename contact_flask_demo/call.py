import subprocess
import shlex
import json
import time
import os
def call(number):
	# Call termux-api's telephony call script with the passed number
	os.system("termux-telephony-call %s" % number)

