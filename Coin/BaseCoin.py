import pygame


class BaseCoin(pygame.rect.Rect):
    def __init__(self, left: float, top: float):
        super().__init__(left, top, 20, 20)

    def draw(self):
        ...

    def process(self):
        ...
