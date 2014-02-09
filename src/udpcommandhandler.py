'''
Created on Jan 11, 2014

@author: dougnappier
'''

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from actionhandler import ActionHandler

class UDPCommandHandler(DatagramProtocol):
    
    def datagramReceived(self, data, (host, port)): 
        #print "received %r from %s:%d" % (data, host, port)
        self.transport.write(data, (host, port))
        action = ActionHandler()
        action.executeCommand(data)

    def run(self):
        reactor.listenUDP(8899, UDPCommandHandler())
        reactor.run()