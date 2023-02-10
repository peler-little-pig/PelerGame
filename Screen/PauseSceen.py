from GUI.Label import *
from GUI.Button import *
from Data.AllData import *
from GUI.Manager import Manager


class PauseScreen(object):
    def __init__(self):
        self.manager = Manager('./Res/GUI_Theme/Screen/title_screen.json')
        self.title = Label(self.manager,0, 100, GameData.WINDOW_WIDTH, 100, 'Game Pause')
        self.button = Button(self.manager,0, 500, GameData.WINDOW_WIDTH, 50, 'START')
        self.button.click_function = self.continue_game
        self.is_running = True

    def continue_game(self):
        self.is_running = False
        EventData.is_key_w_down = False
        EventData.is_key_s_down = False
        EventData.is_key_a_down = False
        EventData.is_key_d_down = False
        EventData.is_key_q_down = False
        EventData.is_key_e_down = False
        EventData.is_key_f_down = False
        EventData.is_left_mouse_down = False
        EventData.is_right_mouse_down = False