from Coin.BaseCoin import *
import pygame
from Data.AllData import *


class EnergyCoin(BaseCoin):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/image/energy_coin/energy_coin.png').convert_alpha()
        self.speed = 7

    def draw(self):
        ConstData.surface.blit(self.image, self)

    def process(self):
        super().process()
        if self.colliderect(ShareData.good_actor):
            ShareData.good_actor.add_energy(2)
            self.is_should_delete = True
