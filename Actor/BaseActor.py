import pygame


class BaseActor(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.thing = None

    def draw(self):
        self.thing.draw()

    def process(self):
        self.thing.process()
