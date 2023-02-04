from InfoBar.BaseInfoBar import *
import pygame
from Data.AllData import *


class SkillInfoBar(BaseInfoBar):
    def __init__(self, value):
        super().__init__(10, 100, (value, 20), value)

    def draw(self):
        self.width = self.value/4
        pygame.draw.rect(GameData.surface, (0, 255, 0), self)
