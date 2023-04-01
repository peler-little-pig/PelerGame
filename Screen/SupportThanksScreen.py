from GUI.Label import *
from GUI.Manager import *


class SupportThanksScreen(object):
    def __init__(self):
        self.supporter_list = ['aaa','bbbb','ccdada']
        self.manager = Manager('./Res/GUI_Theme/Screen/info_screen.json')
        for i in range(len(self.supporter_list)):
            Label(self.manager, 10, i*30, GameData.WINDOW_WIDTH, 30, self.supporter_list[i], object_id='@left')
