import pygame
from Value import *


class BaseEgg(pygame.rect.Rect):
    def __init__(self, degree, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.degree:tuple = degree
        self.speed = 6

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
        # num = self.speed / (self.degree[0]+self.degree[1])
        # self.move_ip(num*self.degree[0],-num*self.degree[1])
        # self.move_ip(self.degree[0]/10, -self.degree[1]/10)
