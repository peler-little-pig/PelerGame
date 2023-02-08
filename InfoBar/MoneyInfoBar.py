from GUI.Label import Label
from GUI.Manager import Manager
from InfoBar.BaseInfoBar import *
import pygame
from Data.AllData import *


class MoneyInfoBar(BaseInfoBar):
    def __init__(self, value):
        super().__init__(10, 130, (0, 0), value)
        self.money_coin_image = pygame.image.load('./Res/Picture/image/money_coin/money_coin.png').convert_alpha()
        self.manager = Manager('./Res/GUI_Theme/Infobar/money_info_bar.json')
        self.label = Label(self.manager, 40, 130, 100, 20, str(value))

    def draw(self):
        GameData.surface.blit(self.money_coin_image, self)
        self.manager.draw()
        self.manager.update()

    def set_value(self, value):
        self.value = value
        self.label.set_text(str(self.value))

    def add_value(self,add):
        self.value += add
        self.label.set_text(str(self.value))