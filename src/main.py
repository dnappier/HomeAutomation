'''
Created on Jan 11, 2014

@author: dougnappier
'''
CH = ''
from udpcommandhandler import UDPCommandHandler
from versionsync import VersionSync

VersionSync("master").start()
CH = UDPCommandHandler()
CH.run()
print 'done'
