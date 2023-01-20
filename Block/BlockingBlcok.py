from Block.BaseBlock import *
import pygame
import Lib.BetterPygame.Rect as BRect


class BlockingBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        # self.image = pygame.image.load('./Res/image/ground_block/ground_block.png').convert()

    def draw(self):
        # if self.is_need_draw():
        pygame.draw.rect(ConstData.surface, (0, 0, 255), self)

    # pass

    def is_hit(self):
        return self.colliderect(ShareData.good_actor)