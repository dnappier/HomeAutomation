__author__ = 'dougnappier'
import subprocess
from threading import Timer

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


    def __update_if_necessary(self):
        if self.__check_latest_version():
            Timer(self.duration, self.__update_if_necessary, ()).start()
        else:
            self.__get_update()

    def __get_update(self):
        subprocess.Popen(['git', 'pull', 'origin', '%s:%s'%(self.branch, self.branch)], stdout=subprocess.PIPE).communicate()[0]
        subprocess.Popen(['python', 'bootloader.py'], stdout=subprocess.PIPE).communicate()[0]

    def start(self, duration=5):
        self.duration = duration
        Timer(duration, self.__update_if_necessary, ()).start()