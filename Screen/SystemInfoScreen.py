from GUI.Label import *
from GUI.Button import *
from Data.AllData import *
from GUI.Manager import *
import platform


def system():
    return f'system={platform.system()}'


def node():
    return f'node={platform.node()}'


def release():
    return f'release={platform.release()}'


def version():
    return f'version={platform.version()}'


def machine():
    return f'machine={platform.machine()}'


def processor():
    return f'processor={platform.processor()}'

class SystemInfoScreen(object):
    def __init__(self):
        self.manager = Manager('./Res/GUI_Theme/Screen/info_screen.json')
        self.system = Label(self.manager, 10, 0, GameData.WINDOW_WIDTH / 2, 30, system())
        self.node = Label(self.manager, 10, 30, GameData.WINDOW_WIDTH / 2, 30, node())
        self.release = Label(self.manager, 10, 60, GameData.WINDOW_WIDTH / 2, 30, release())
        self.version = Label(self.manager, 10, 90, GameData.WINDOW_WIDTH / 2, 30, version())
        self.machine = Label(self.manager, 10, 120, GameData.WINDOW_WIDTH / 2, 30, machine())
        self.processor = Label(self.manager, 10, 150, GameData.WINDOW_WIDTH / 2, 30, processor())
