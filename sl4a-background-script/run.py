import android
import time
import datetime
droid= android.Android()
n = 0
while n < 20:
	droid.makeToast(str(datetime.datetime.now()))
	time.sleep(5)
	n+=1
