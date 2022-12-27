import pygame
from Value import *
from Actor.BaseActor import *


class BaseThing(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)

    def draw(self):
        pygame.draw.rect(Value.surface, (255, 255, 255), self)

    def rotate(self):
        pass
