import pygame
from Data.AllData import *

class BaseBlock(pygame.rect.Rect):
    def __init__(self, left: float, top: float) -> None:
        super().__init__(left, top, *ConstData.BLOCK_SIZE_TUPLE)

    # def is_need_draw(self):
    #     return -ConstData.DRAW_AREA_ADD < self.x < ConstData.WINDOW_WIDTH \
    #            or -ConstData.DRAW_AREA_ADD < self.y < ConstData.WINDOW_HEIGHT

    def draw(self):
        ...

    def process(self):
        ...
