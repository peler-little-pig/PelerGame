from GUI.Label import *
from GUI.Button import *
from Data.AllData import *


class EndScreen(object):
    def __init__(self):
        self.title = Label(0, 100, GameData.WINDOW_WIDTH, 100, 'Game Over')
        self.button1 = Button(0, 500, GameData.WINDOW_WIDTH/2, 50, 'RESTART')
        self.button1.click_function = self.restart_game
        self.button2 = Button(GameData.WINDOW_WIDTH/2, 500, GameData.WINDOW_WIDTH/2, 50, 'EXIT')
        self.button2.click_function = self.exit_game
        self.is_running = True

    def restart_game(self):
        self.is_running = False
        GameData.UI_MANAGER.ui_group.remove(self.title)
        GameData.UI_MANAGER.ui_group.remove(self.button1)
        GameData.UI_MANAGER.ui_group.remove(self.button2)
        ShareData.game.is_restart = True

    def exit_game(self):
        self.is_running = False
        GameData.UI_MANAGER.ui_group.remove(self.title)
        GameData.UI_MANAGER.ui_group.remove(self.button1)
        GameData.UI_MANAGER.ui_group.remove(self.button2)
        ShareData.game.is_restart = False