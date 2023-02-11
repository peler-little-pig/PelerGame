from GUI.Label import *
from GUI.Button import *
from Data.AllData import *
from GUI.Manager import *
import platform
from Compute.SpaceCompute import *


def system():
    return f'system:{platform.system()}'


def node():
    return f'node:{platform.node()}'


def release():
    return f'release:{platform.release()}'


def version():
    return f'version:{platform.version()}'


def machine():
    return f'machine:{platform.machine()}'


def processor():
    return f'processor:{platform.processor()}'


def python_version():
    return f'python version:{platform.python_version()}'


def python_build():
    return f'python build:{platform.python_build()}'


def python_compiler():
    return f'python compiler:{platform.python_compiler()}'


def python_implementation():
    return f'python implementation:{platform.python_implementation()}'


def python_version_tuple():
    return f'python version_tuple:{platform.python_version_tuple()}'


def pip_version():
    try:
        import pip
    except ModuleNotFoundError:
        return "pip not found"
    return f'''pip version:{pip.__version__}'''


def pygame_version():
    try:
        import pygame
    except ModuleNotFoundError:
        return "pygame not found"
    return f'pygame version:{pygame.version.ver}'


def SDL_version():
    try:
        import pygame
    except ModuleNotFoundError:
        return "pygame not found"
    return f'SDL version:{pygame.version.SDL}'


class SystemInfoScreen(object):
    def __init__(self):
        self.manager = Manager('./Res/GUI_Theme/Screen/info_screen.json')
        self.system = Label(self.manager, 10, 0, GameData.WINDOW_WIDTH / 2, 30, system(), object_id='@left')
        self.node = Label(self.manager, 10, 30, GameData.WINDOW_WIDTH / 2, 30, node(), object_id='@left')
        self.release = Label(self.manager, 10, 60, GameData.WINDOW_WIDTH / 2, 30, release(), object_id='@left')
        self.version = Label(self.manager, 10, 90, GameData.WINDOW_WIDTH / 2, 30, version(), object_id='@left')
        self.machine = Label(self.manager, 10, 120, GameData.WINDOW_WIDTH / 2, 30, machine(), object_id='@left')
        self.processor = Label(self.manager, 10, 150, GameData.WINDOW_WIDTH / 2, 30, processor(), object_id='@left')

        self.python_version = Label(self.manager, GameData.WINDOW_WIDTH / 2, 0, GameData.WINDOW_WIDTH / 2, 30,
                                    python_version(),
                                    object_id='@right')
        self.python_build = Label(self.manager, GameData.WINDOW_WIDTH / 2, 30, GameData.WINDOW_WIDTH / 2, 30,
                                  python_build(),
                                  object_id='@right')
        self.python_compiler = Label(self.manager, GameData.WINDOW_WIDTH / 2, 60, GameData.WINDOW_WIDTH / 2, 30,
                                     python_compiler(),
                                     object_id='@right')
        self.python_implementation = Label(self.manager, GameData.WINDOW_WIDTH / 2, 90, GameData.WINDOW_WIDTH / 2, 30,
                                           python_implementation(),
                                           object_id='@right')
        self.python_version_tuple = Label(self.manager, GameData.WINDOW_WIDTH / 2, 120, GameData.WINDOW_WIDTH / 2, 30,
                                          python_version_tuple(),
                                          object_id='@right')
        self.pip_version = Label(self.manager, GameData.WINDOW_WIDTH / 2, 150, GameData.WINDOW_WIDTH / 2, 30,
                                 pip_version(),
                                 object_id='@right')
        self.pygame_version = Label(self.manager, GameData.WINDOW_WIDTH / 2, 180, GameData.WINDOW_WIDTH / 2, 30,
                                    pygame_version(),
                                    object_id='@right')
        self.SDL_version = Label(self.manager, GameData.WINDOW_WIDTH / 2, 210, GameData.WINDOW_WIDTH / 2, 30,
                                 SDL_version(),
                                 object_id='@right')
