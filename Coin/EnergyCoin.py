from Coin.BaseCoin import *
import pygame
from Data.AllData import *


class EnergyCoin(BaseCoin):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/image/energy_coin/energy_coin.png').convert_alpha()

    def draw(self):
        ConstData.surface.blit(self.image, self)
