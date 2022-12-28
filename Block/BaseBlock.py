import pygame
from Value import *

class BaseBlock(pygame.rect.Rect):
    def __init__(self, left: float, top: float) -> None:
        super().__init__(left, top, *Value.BLOCK_SIZE_TUPLE)

    def draw(self):
        pygame.draw.rect(Value.surface, Value.BASE_BLOCK_COLOR, self)
