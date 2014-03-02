'''
Created on Jan 11, 2014

@author: dougnappier
'''
CH = ''
from src.udpcommandhandler import UDPCommandHandler
from versionsync import VersionSync

VersionSync("github_sync").start()
CH = UDPCommandHandler()
CH.run()
print 'done'
