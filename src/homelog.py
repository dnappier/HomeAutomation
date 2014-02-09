'''
Created on Jan 30, 2014

@author: dougnappier
'''

BUFFERSIZE = 500 #lines
import datetime

class Log(object):
    '''
    just use read and write
    '''
    

    def __init__(self, filePath=r'/home/dougnappier/homelog.txt'):
        '''
        optionally pass in filePath
        '''
        self.filePath = filePath
        self.open()
        
    def log(self, comment, priority=0):
        if comment[-1:] == '\n':
            addChar = ''
        else:
            addChar = '\r\n'
        lineToAdd = '[%s, %d] '%(str(datetime.datetime.now())[:-4], priority)
        lineToAdd = lineToAdd + comment + addChar
        print lineToAdd
        self.lines.append(lineToAdd)
        
        if len(self.lines) > BUFFERSIZE:
            self.lines = self.lines[1:]
        
        wholeFile = ''.join(self.lines)
        self.f.write(wholeFile)
        self.f.close()
        
    def open(self):
        self.f = open(self.filePath, 'r')
        f = self.f.read()
        self.lines = f.splitlines(True)
        self.f.close()
        self.f = open(self.filePath, 'w+')
         
