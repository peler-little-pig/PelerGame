from GUI.Manager import *


class BaseScreen(object):
    def __init__(self):
        self.manager = Manager('./Res/GUI_Theme/Screen/screen.json')
