import pygame
from Thing.BaseThing import *
from  Value import *


class BaseActor(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.thing = BaseThing(self.x + 25, self.y + 35, 50, 30)

    def fire(self):
        self.thing.fire()

    def draw(self):
        pygame.draw.rect(Value.surface, (0, 0, 255), self)
        self.thing.draw()
