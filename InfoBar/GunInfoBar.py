from GUI.Label import Label
from GUI.Manager import Manager
from InfoBar.BaseInfoBar import *
import pygame
from Data.AllData import *


class GunInfoBar(BaseInfoBar):
    def __init__(self, value):
        super().__init__(10, 130, (0, 0), value)
        self.attack_icon = pygame.image.load('./Res/Picture/image/attack/attack.png').convert_alpha()
        self.manager = Manager('./Res/GUI_Theme/Infobar/gun_info_bar.json')
        # self.label = Label(self.manager, 40, 130, 100, 20, str(value))

    def draw(self):
        GameData.surface.blit(self.attack_icon, self)
        self.manager.draw()
        self.manager.update()