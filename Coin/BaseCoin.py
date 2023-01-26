import pygame
from Lib.Compute.MoveCompute import *

class BaseCoin(pygame.rect.Rect):
    def __init__(self, left: float, top: float):
        super().__init__(left, top, 20, 20)
        self.is_should_delete = False

    def draw(self):
        ...

    def process(self):
        follow_move(self)
        if self.colliderect(ShareData.good_actor):
            ShareData.good_actor.energy_info_bar.value += 10
            self.is_should_delete = True
