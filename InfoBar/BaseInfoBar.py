import pygame


class BaseInfoBar(pygame.rect.Rect):
    def __init__(self, x, y, size, value) -> None:
        super().__init__(x, y, *size)
        self.value = value

    def draw(self):
        ...

    def process(self):
        ...
