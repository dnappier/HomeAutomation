__author__ = 'dougnappier'
import time
import subprocess


#sleep 5 minutes
time.sleep(5000)
subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE).communicate()[0]