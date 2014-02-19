import threading
from wirelesslights import WirelessLights
import time
from random import randint

DEBUG = 1


class FlashLights(threading.Thread):

    def __init__(self, thread_ID, name, group=1, All=False, color="red"):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.name = name
        self.All = All
        self.kill_thread = False
        self.color = color
        self.flashing = False
        if not All:
            self.group = group
        else:
            self.group = -1
        self.set_flash_color(color)
    def run(self):
        """
        DOC STRING
        """
        w = WirelessLights(group=self.group, All=self.All)

        if DEBUG:
            print "FlashingLightsRunning"
        while not self.kill_thread:
            w.on(self.color, brightness=100)
            self.color = self.get_color()
            time.sleep(.4)
            w.off()

    def kill(self):
        self.kill_thread = True

    def set_flash_color(self, color):
        colors_l = WirelessLights(self.group).getColors()
        if color == 'random':
            self.color = colors_l[randint(0, len(colors_l) -1)]
        elif color == 'flash':
            self.init_flashing_colors()
        else:
            self.color = color

    def init_flashing_colors(self):
        self.flashing = True
        self.all_colors = WirelessLights(self.group).getColors()
        self.color = self.get_color()

    def get_color(self):
        color = ''
        if self.flashing:
            color = self.all_colors[randint(0, len(self.all_colors) -1)]
            if color == self.color:
                color = self.get_color()

        return color

    def getName(self):
        return self.name