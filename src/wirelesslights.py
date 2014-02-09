GROUPBASE = 0x45
PACKETEND = 0x55

UDP_PORT = 8899
UDP_IP = "192.168.1.255"

BASE = 0x41
ALLOFF = BASE
ALLON = BASE + 1
SPEEDSLOWER = BASE + 2
SPEEDFASTER = BASE + 3
WHITE = 0x45
WHITE2 = 0xC5
WHITEALL = 0x42
WHITEALL2 = 0xC2
import socket
import time

COLORDICT = {
         'Violet'        : 0x00,
         'Royal_Blue'    : 0x10,
         'Baby_Blue'     : 0x20,
         'Aqua'          : 0x30,
         'Mint'          : 0x40,
         'Seafoam_Green' : 0x50,
         'Green'         : 0x60, 
         'Lime_Green'    : 0x70,
         'Yellow'        : 0x80,
         'Yellow_Orange' : 0x90,
         'Orange'        : 0xA0,
         'Red'           : 0xB0,   
         'Pink'          : 0xC0,
         'Fusia'         : 0xD0,
         'Lilac'         : 0xE0,
         'Lavendar'      : 0xF0
}

#
#  wait for 50ms before consecutive commands
#
class WirelessLights(object):
    
    def __init__(self, group=1, All=False):
        self.group = group
        self.packet = []
        self.all = All
        if All:
            self.on = self.onAll
            self.off = self.offAll
            self.white = self.whiteAll
        else:
            self.on = self.ON
            self.off = self.OFF
            self.white = self.WHITE
        
    def ON(self):
        self.packet.append(GROUPBASE + ((self.group - 1)*2) )
        self.packet.append(0x00)
        self.send()

    def OFF(self):
        self.packet.append(GROUPBASE + ((self.group - 1)*2) + 1)
        self.send()
  
    def onAll(self):
        self.packet.append(ALLON)
        self.packet.append(0x00)
        self.send()
        
    def send(self, use2ndByte=False):
        if not use2ndByte:
            self.packet.append(0x00);
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.packet.append(PACKETEND)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.sendto(self.packetToString(), (UDP_IP, UDP_PORT))
        sock.close()
        self.packet = []
          
    def offAll(self):
        self.packet.append(ALLOFF)
        self.send()
        
    def packetToString(self):
        packetStr = ''
        for x in self.packet:
            packetStr += chr(x)

        return packetStr
        
    def WHITE(self):
        self.packet.append(WHITE + ((self.group - 1)*2))
        self.send()
        #packet is set []
        self.packet.append(WHITE2 + ((self.group - 1)*2))
        time.sleep(.1)
        self.send()
        
    def whiteAll(self):
        self.packet.append(WHITEALL)
        self.send()
        #packet is cleared by send
        self.packet.append(WHITEALL2)
        self.send()
        
    def setColor(self, color):
        self.packet.append(0x40)
        self.packet.append(COLORDICT[color])
        self.send(use2ndByte=True)
    
    def setColorInt(self, integer):
        self.packet.append(0x40)
        self.packet.append(integer)
        self.send(use2ndByte=True)
        
    def setBrightness(self, percent):
        self.packet.append(0x4E)
        self.packet.append( (percent * 0x1B)/100 )
        self.send(use2ndByte=True)
        
    def getColors(self):            
        return list(COLORDICT.keys())
    
    def flashColor(self, color, timeS):
        self.on()
        self.setColor(color)
        self.setBrightness(100)
        time.sleep(timeS)
        self.off()
        time.sleep(timeS)
        
        