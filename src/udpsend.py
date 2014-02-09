'''
Created on Jan 12, 2014

@author: dougnappier
'''
#import socket

#UDP_IP = "127.0.0.1"
#UDP_PORT = 2015
#MESSAGE = "Hello, World!"
 
#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE
 
#sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

import socket

UDP_IP = "192.168.1.95" #this is the IP of the wifi bridge
UDP_PORT = 8899

MESSAGE1 = "\x39\x00\x55" #this turns all lights off

print "UDP target IP:", UDP_IP #don't really need this
print "UDP target port:", UDP_PORT #don't really need this
print "message:", MESSAGE1 #don't really need this

sock = socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)
sock.sendto(MESSAGE1, (UDP_IP, UDP_PORT))