from GUI.Label import *
from GUI.Button import *
from Data.AllData import *
from GUI.Manager import *
from Screen.BaseScreen import BaseScreen


class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.title = Label(self.manager, 0, 100, GameData.WINDOW_WIDTH, 100, 'PelerGame!!!')
        self.button = Button(self.manager, 0, 500, GameData.WINDOW_WIDTH, 50, 'START')
        self.button.click_function = self.start_game
        self.is_running = True

    def start_game(self):
        self.is_running = False
