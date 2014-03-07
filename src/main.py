'''
Created on Jan 11, 2014

@author: dougnappier
'''
CH = ''
from os import system
from versionsync import VersionSync


print 'test'
VersionSync("github_sync").start()
system(r'python server/udpserver.py &')
print 'done'
