import pygame
from Data.AllData import *

class BaseBlock(pygame.rect.Rect):
    def __init__(self, left: float, top: float) -> None:
        super().__init__(left, top, *BlockData.BLOCK_SIZE_TUPLE)

    # def is_need_draw(self):
    #     return -GameData.DRAW_AREA_ADD < self.x < GameData.WINDOW_WIDTH \
    #            or -GameData.DRAW_AREA_ADD < self.y < GameData.WINDOW_HEIGHT

    def draw(self):
        ...

    def process(self):
        ...
