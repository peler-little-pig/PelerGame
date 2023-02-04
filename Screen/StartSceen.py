from GUI.Label import *
from GUI.Button import *
from Data.AllData import *


class StartScreen(object):
    def __init__(self):
        self.title = Label(0, 100, GameData.WINDOW_WIDTH, 100, 'PelerGame!!!')
        self.button = Button(0, 500, GameData.WINDOW_WIDTH, 50, 'START')
        self.button.click_function = self.start_game
        self.is_running = True

    def start_game(self):
        self.is_running = False
        GameData.UI_MANAGER.ui_group.remove(self.title)
        GameData.UI_MANAGER.ui_group.remove(self.button)