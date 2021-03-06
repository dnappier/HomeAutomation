'''
Created on Jan 11, 2014

@author: dougnappier
'''

import command, time, os
from wirelesslights import WirelessLights
from homelog import Log
import datetime

class ActionHandler(object):
    def executeCommand(self, cmd, **kwargs):
        if(cmd == command.STARTMORNINGRADIO):
            os.system("firefox http://www.pandora.com/station/play/1398303715177272562")

        if(cmd == command.SETVOLUME):
            Log().log("Volume Set to: %s" %(kwargs['volume']))
            os.system("amixer --quiet set Master %d" %(kwargs['volume']) )

        if(cmd == command.MUTE):
            Log().log("Mute")
            os.system("amixer --quiet set Master toggle")

        if(cmd == command.VOLUMEDOWN):
            Log().log("Volume Down")
            os.system("amixer --quiet set Master 5-")
    
        if(cmd == command.VOLUMEUP):
            Log().log("Volume Up")
            os.system("amixer --quiet set Master 5+")

        if(cmd == command.SILET):
            Log().log("Computer Silent")
            os.system("amixer --quiet set Master 0")
            
        if(cmd == command.START):
            Log().log("Radio started")
            self.executeCommand(command.STARTMORNINGRADIO)
            self.executeCommand(command.SETVOLUME, volume=50)
            
        if(cmd == command.KITCHEN_ON):
            Log().log("Kitchen On")
            w = WirelessLights(1)
            w.on()
            w.white()
            w.setBrightness(90)
            del(w)
            
        if(cmd == command.LIVINGROOM_ON):
            Log().log("Living Room On")
            w = WirelessLights(2)
            w.on()
            w.white()
            w.setBrightness(75)
            del(w)
            
        if(cmd == command.KITCHEN_OFF):
            Log().log("Kitchen Off")
            w = WirelessLights(1)
            w.off()
            del(w)
        
        if(cmd == command.LIVINGROOM_OFF):
            Log().log("Living Room Off")
            w = WirelessLights(2).off()
            del(w)
        if(cmd == command.ALL_OFF):
            Log().log("All off")
            w = WirelessLights(All=True)
            w.off()
            del(w)
            
        if(cmd == command.ALL_ON):
            Log().log("All on")
            w = WirelessLights(All=True).off()
            del(w)

        if (cmd == command.KILL):
            Log().log("Going Down")
            return True
            
        if(cmd ==command.WAKEUP):
            Log().log("Wakeup")
            w = WirelessLights(4)
            w.on()
            w.setColor('Red')
            w.setBrightness(100)
            for i in range(90):
                w.on()
                time.sleep(.5)
                w.off()
                time.sleep(.5)

        return False