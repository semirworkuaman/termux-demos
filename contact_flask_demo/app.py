from flask import render_template,Flask
# Import contact script
import contact as c
import datetime
# import call script
import call
from time import sleep
app = Flask(__name__)
# Controller to do the dialing
@app.route('/call/<number>')
def dial(number=None):
    call.call(number)
    # Give a couple of seconds for the script to run
    # before respondng
    sleep(2)
    return "Calling %s " % (number)
# Main controller to display contacts
@app.route('/')
def get_contacts(contacts=None,no_contacts=None):
	# Render html with passed values
    return render_template('index.html', no_contacts=len(c.contact_array),contacts=c.contact_array)
if __name__ == '__main__':
	# Run app on port 8069
    app.run(port=8069)
