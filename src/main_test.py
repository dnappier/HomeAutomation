'''
Created on Jan 28, 2014

@author: dougnappier
'''
import time
from wirelesslights import WirelessLights
from homelog import Log
if __name__ == '__main__':
    t = '''for j in range(4,5):
        k = 0
        w = WirelessLights(j, All=True)
        w.on()
        time.sleep(1)
        w.setBrightness(100)
        for i in range (0x100):
            k += 1
            w.setColorInt(i)
            time.sleep(.2)
            s = '%d - %d'%(j,i)
            print s
            Log().log(s)'''
    w = WirelessLights(2)
    w.on()
    w.white()
    w.setBrightness(75)
    time.sleep(5)
    w = WirelessLights(2).off()
    del(w)