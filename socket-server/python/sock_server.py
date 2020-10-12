import libs
from flask import Flask, render_template,request
from flask_socketio import SocketIO
import time
import flask
import datetime
from flask import jsonify,request
import logging
import json
import android
droid = android.Android()
from threading import Thread
ip=""
port=0
w2=False
tsk=None
cls=None
logging.getLogger('socketio').setLevel(logging.ERROR)
app = Flask(__name__)
class Tasker(object):
    def __init__(self):
    	pass
    def sset(self,dr):
        self.droid=dr
    def gget(self):
        return self.droid
tt=Tasker()
socketio = SocketIO(app,logger= False,log_output=False)
def mes():
    tsk.gget().eventPost("my_event",'55')
@socketio.on('connect',namespace="/poc")
def client_connectedy():
	print "connected"
	socketio.emit("bar",'connected '+str(datetime.datetime.now()),namespace="/poc")
@socketio.on('disconnect',namespace="/poc")
def client_connectedyh():
	print "disconnected"
	socketio.emit("bar",'disconnected '+str(datetime.datetime.now()),namespace="/poc")
@socketio.on('connect',namespace="/clnt")
def client_connectedx():
	print "connected"
	socketio.emit("bar","connected now" +str(request.remote_addr) + str(request.namespace),namespace="/poc")
@socketio.on('disconnect',namespace="/clnt")
def client_disconnected():
	print "disconnected"
	socketio.emit("bar","disconnected "+str(datetime.datetime.now()),namespace="/poc")
@socketio.on('kill',namespace="/server")
def kill_server(msg):
	print msg
	socketio.stop()
	#tsk.gget().eventPost("stopped","/clnt")
@socketio.on('task',namespace="/poc")
def on_my_event(msg):
	#socketio.stop()
    print msg
    #w3 = Thread(target=mes)
    #w3.start()
    #socketio.emit("bar",'test')
    socketio.emit("bar",msg+str(datetime.datetime.now()),namespace="/poc")
    #socketio.emit("bar",msg,namespace="/server")
    #socketio.emit("bar",msg,namespace="/clnt")
@socketio.on('task',namespace="/clnt")
def on_my_eventx(msg):
	#socketio.stop()
    print msg
    #w3 = Thread(target=mes)
    #w3.start()
    #socketio.emit("bar",'test')
    print request
    #droid.ttsSpeak(msg)
    socketio.emit("bar",msg+str(datetime.datetime.now()),namespace="/poc")
    socketio.emit("bar",msg+str(datetime.datetime.now()),namespace="/clnt")
    #tt.gget().eventPost("my_event","stopped") 
    #socketio.emit("bar",msg,namespace="/server")
    #socketio.emit("bar",msg,namespace="/clnt")
def set_droid(dr=None):
	if dr == None:
		return 
def begin(ip,port,cc):
    tt.sset(cc)
    
    p=socketio.run(app,host=ip,port=port,debug=False)
    print p
    
    #return socketio

def start(ip,port,the_class):
    
    w2 = Thread(name="begin",target=begin,args=(ip,port,the_class))
    w2.start()
	
	#begin(ip,port)
	#socketio.run(app,host=ip,port=port,debug=False)
    return True
