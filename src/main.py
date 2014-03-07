'''
Created on Jan 11, 2014

@author: dougnappier
'''
CH = ''
from udpcommandhandler import UDPCommandHandler
from versionsync import VersionSync


if __name__ == 'main':
    VersionSync("master").start()
    UDPCommandHandler().run()
    print 'done'
