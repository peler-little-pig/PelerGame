from Block.BaseBlock import *
import pygame


class WallBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load(f'./Res/Picture/image/wall_block/new.png').convert()

    def draw(self):
        # if self.is_need_draw():
        GameData.surface.blit(self.image, self)

    def process(self):
        ...
