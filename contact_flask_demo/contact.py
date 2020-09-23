import subprocess
import shlex
import json
import time
# Call termux api's contact list script
contacts = subprocess.Popen(
             "termux-contact-list",
             stdout=subprocess.PIPE)
contact_string=""
# Put the result in a string
for c in contacts.stdout:
	data=c.decode("utf-8").strip()
	contact_string+=data

# Json loads to covert to array
contact_array=json.loads(contact_string)
