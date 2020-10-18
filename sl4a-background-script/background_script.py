#Author : Rimes App
# Git Repo : https://github.com/semirworkuaman/termux-demos/sl4a-bacground-script

import android 
droid = android.Android() 
# Assign Action
action = "com.googlecode.android_scripting.action.LAUNCH_BACKGROUND_SCRIPT" 
# Assign Class Name
clsname = "com.googlecode.android_scripting" 
# Assign Package Name
pkgname = "com.googlecode.android_scripting.activity.ScriptingLayerServiceLauncher" 
# Provide the path of the script to run as extras
# The run.py script shows a toast with
# the current time every 5 seconds
extras = {"com.googlecode.android_scripting.extra.SCRIPT_PATH":
 "/sdcard/sl4a/scripts/run.py"} 
# Make the intent
myintent = droid.makeIntent(action, None, None, extras, None, clsname, pkgname).result 
# Start Activity Intent
droid.startActivityIntent(myintent)