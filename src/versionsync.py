__author__ = 'dougnappier'
import subprocess
from multiprocessing import Process, current_process
from threading import Timer
from server import homelog
import time
import os

class VersionSync(object):
    """
    Syncs running version with Git
    """
    def __init__(self, branch='master'):
        self.branch = branch
        self.duration = 5
        self.current_ref = subprocess.Popen(["git", "rev-parse", self.branch], stdout=subprocess.PIPE).communicate()[0]


    def __check_latest_version(self):
        origin_sha = subprocess.Popen(['git', 'rev-parse', 'remotes/origin/%s' %self.branch], stdout=subprocess.PIPE).communicate()[0]
        if self.current_ref == origin_sha:
            return True
        else:
            self.__get_update()
            #check update if sucessful
            homelog.Log().log("Sending kill signal")
            os.system('echo -n "kill" | nc -4u -w1 localhost 8899')

    def __update_if_necessary(self):
        if self.__check_latest_version():
            Timer(self.duration, self.__update_if_necessary, ()).start()
        else:
            self.__get_update()

    def __get_update(self):
        self.spawn_detached(self.__restart_program)

    def __restart_program(self):
        time.sleep(60)
        out = subprocess.Popen(['git', 'pull', 'origin', '%s:%s'%(self.branch, self.branch)], stdout=subprocess.PIPE).communicate()[0]
        homelog.Log().log(out)
        time.sleep(1)
        subprocess.Popen(['python', 'bootloader.py'], stdout=subprocess.PIPE).communicate()[0]

    def spawn_detached(self, callable):
        p = self.__spawn_detached(0, callable)
        # give the process a moment to set up
        # and then kill the first child to detach
        # the second.
        time.sleep(.001)
        p.terminate()

    def __spawn_detached(self, count, callable):
        count += 1
        p = current_process()

        if count < 2:
            name = 'child'
        elif count == 2:
            name = callable.func_name
        else:
            # we should now be inside of our detached process
            # so just call the function
            return callable()

        # otherwise, spawn another process, passing the counter as well
        p = Process(name=name, target=self.__spawn_detached, args=(count, callable))
        p.daemon = False
        p.start()
        return p

    def start(self, duration=5):
        self.duration = duration
        Timer(duration, self.__update_if_necessary, ()).start()