#Author : Rimes App
# Git Repo : https://github.com/semirworkuaman/termux-demos/sl4a-flip-phone-silent

import android, time 
droid = android.Android() 

silent = False 

def checkOrientation():
    
    ret=droid.startSensingTimed(2, 10) 
    silent = False 
    if ret.error:
        if "your OS version..." in ret.error:
            return True
        return False
    while True:
    
        
        e = droid.eventPoll(1).result
        
        if e:
            
            facedown = e and 'data' in e[0] and e[0]['data']['zforce'] and e[0]['data']['zforce'] <= -9
            if facedown and not silent: 
                droid.toggleRingerSilentMode(True)
                droid.vibrate(1000)
                droid.makeToast('Silent')
                silent=True
                print 'Silent'
            elif not facedown and silent: 
                droid.toggleRingerSilentMode(False)
                silent=False
                droid.makeToast('Ring')
                print 'Ring'
            
        else:
            print("time out...")
            continue
        
    
    return False



    
    


if __name__ == '__main__':                                  # {{{1
    checkOrientation()

