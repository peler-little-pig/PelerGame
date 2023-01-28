import pygame
from Lib.Compute.MoveCompute import *
from Lib.Math.Math import *
from Lib.Compute.DistanceCompute import *

class BaseCoin(pygame.rect.Rect):
    def __init__(self, left: float, top: float):
        super().__init__(left, top, 20, 20)
        self.is_should_delete = False
        self.speed = 0

    def draw(self):
        ...

    def process(self):
        follow_move(self)

        if is_close(self,ShareData.good_actor,250):
            degree, dir = get_degree(*self.center, *ShareData.good_actor.center)
            self.x = self.x + dir[0] * self.speed
            self.y = self.y + dir[1] * self.speed
