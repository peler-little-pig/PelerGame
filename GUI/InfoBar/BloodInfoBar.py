import pygame
from Data.AllData import *
from GUI.InfoBar.BaseInfoBar import BaseInfoBar


class BloodInfoBar(BaseInfoBar):
    def __init__(self, value):
        super().__init__(10, 10, InfoBarData.SIZE_TUPLE, value)
        self.full_image = pygame.image.load('./Res/Picture/image/blood_info_bar/full_heart.png').convert_alpha()
        self.half_image = pygame.image.load('./Res/Picture/image/blood_info_bar/half_heart.png').convert_alpha()

    def draw(self):
        x = self.x
        for i in range(int(self.value)):
            GameData.surface.blit(self.full_image, self)
            self.x += 30
        if int(self.value) != self.value:
            GameData.surface.blit(self.half_image, self)
        self.x = x
