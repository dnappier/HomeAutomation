'''
Created on Jan 11, 2014

@author: dougnappier
'''
CH = ''
from udpcommandhandler import UDPCommandHandler
from threading import Timer

def runTest():
    print CH
    CH.exitServer()

#Timer(15, runTest, ()).start()
CH = UDPCommandHandler()
CH.run()
print 'done'
