import sys
import datetime
import erppeek
from threading import Thread
import libs
import json
import requests
from threading import *
from time import sleep
import multiprocessing
#import chatterbot
#from android import Android
from python import *
import android
from socketIO_client import SocketIO, LoggingNamespace
droid = android.Android()
chat_namespace = False

def hide_loader():
	droid.dialogDismiss()
def show_loader(title,message):
	title = title
	message = message
	droid.dialogCreateSpinnerProgress(title, message,10000)
	droid.dialogShow()

droid.webViewShow('file:///sdcard/sl4a/scripts/socket-server/index.html') 
#droid.webViewShow('http://127.0.0.1:8000/rimes-builder/index.html#/app')
#show_loader("44","44")
#sleep(6)
#hide_loader()
sock_servers=[]
class tata(object):
	def __init__(self):
	    drd=droid
	    while True:
		    event = droid.eventWait().result
		    if event['name'] == 'start_server':
			    show_loader("Info","Starting Server")
			    data=json.loads(event["data"])
			    #tsk=sock_server.Tasker(droid)
			    #sock_server.set_android(droid)
			    sock_servers.append(data)
			    res=sock_server.start(data['ip'],data['port'],droid)
			    sleep(2)
			    if 1==1:
				    droid.eventPost("server_status","running")
				    hide_loader()
				    #w3 = Thread(target=worker)
	    		    #w3.start()
		    if event['name'] == 'stop_server':
			    data=json.loads(event["data"])
			    show_loader("Info","Stopping Server")
			    #requests.post(data['ip']+':'+str(data['port'])+'/clnt', "hello")
			    so=SocketIO(data['ip'], data['port']).define(LoggingNamespace, '/server')
			    sleep(2)
			    so.emit('kill', 'killl')
			    #so.close()
			    hide_loader()
			    sock_servers.pop(data["item_index"])
			    droid.eventPost("server_status","stopped")
		    if event['name'] == 'kill':
			    ind=0
			    
			    sys.exit()
		    
			    #show_loader("44","44")
			    #sleep(6)
			    #hide_loader()
		    #droid.webViewShow('file:///sdcard/sl4a/scripts/Examples/starter/index2.html') 
		

def start():
    t = tata()
	
w2 = Thread(name="begin",target=start)
w2.start()