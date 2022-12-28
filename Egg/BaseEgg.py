import pygame
from Value import *


class BaseEgg(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)

    def draw(self):
        pygame.draw.rect(Value.surface, (0, 255, 255), self)

    def process(self):
        if Value.is_move_up:
            self.move_ip(0, Value.MOVE_SPEED)
        if Value.is_move_down:
            self.move_ip(0, -Value.MOVE_SPEED)
        if Value.is_move_left:
            self.move_ip(Value.MOVE_SPEED, 0)
        if Value.is_move_right:
            self.move_ip(-Value.MOVE_SPEED, 0)
        self.move_ip(4, 0)
