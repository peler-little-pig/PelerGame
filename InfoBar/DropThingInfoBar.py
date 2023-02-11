from GUI.Label import Label
from GUI.Manager import Manager
from InfoBar.BaseInfoBar import *
import pygame
from Data.AllData import *


class DropThingInfoBar(BaseInfoBar):
    def __init__(self,thing):
        super().__init__(450, 350, (0, 0), 0)
        self.thing = thing
        self.attack_icon = pygame.image.load('./Res/Picture/image/attack/attack.png').convert_alpha()
        self.manager = Manager('./Res/GUI_Theme/Infobar/thing_info_bar.json')
        self.attack = Label(self.manager, 480, 350, 500, 30, str(self.thing.egg_type(0,0,0,0,0,0,0).hurt))
        self.energy_icon = pygame.image.load('./Res/Picture/image/energy_coin/energy_coin.png').convert_alpha()
        self.energy = Label(self.manager, 580, 350, 500, 30, str(self.thing.cost))

    def draw(self):
        GameData.surface.blit(self.attack_icon, self)
        GameData.surface.blit(self.energy_icon, pygame.rect.Rect(550, 355, 0, 0))
        self.manager.draw()
        self.manager.update()

    def set_thing(self,thing):
        self.thing = thing
        self.attack.set_text(str(self.thing.egg_type(0,0,0,0,0,0,0).hurt))
        self.energy.set_text(str(self.thing.cost))