import pygame


class Base(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float):
        super().__init__(left, top, width, height)

    def draw(self):
        ...
