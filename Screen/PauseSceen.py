from GUI.Label import *
from GUI.Button import *
from Data.AllData import *


class PauseScreen(object):
    def __init__(self):
        self.title = Label(0, 100, GameData.WINDOW_WIDTH, 100, 'Game Pause')
        self.button = Button(0, 500, GameData.WINDOW_WIDTH, 50, 'START')
        self.button.click_function = self.continue_game
        self.is_running = True

    def continue_game(self):
        self.is_running = False
        GameData.UI_MANAGER.ui_group.remove(self.title)
        GameData.UI_MANAGER.ui_group.remove(self.button)
        EventData.is_key_w_down = False
        EventData.is_key_s_down = False
        EventData.is_key_a_down = False
        EventData.is_key_d_down = False
        EventData.is_key_q_down = False
        EventData.is_key_e_down = False
        EventData.is_key_f_down = False
        EventData.is_left_mouse_down = False
        EventData.is_right_mouse_down = False