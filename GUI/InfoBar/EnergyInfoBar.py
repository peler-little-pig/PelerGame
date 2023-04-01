import pygame
from Data.AllData import *
from GUI.InfoBar.BaseInfoBar import BaseInfoBar


class EnergyInfoBar(BaseInfoBar):
    def __init__(self, value):
        super().__init__(10, 70, (value, 20), value)

    def draw(self):
        self.width = self.value
        pygame.draw.rect(GameData.surface, (0, 0, 255), self)
