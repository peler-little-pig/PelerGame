from Block.BaseBlock import *
import pygame


class BlockingBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/Picture/image/blocking_block/new.png').convert()

    def draw(self):
        # if self.is_need_draw():
            GameData.surface.blit(self.image, self)


    def is_hit(self):
        return self.colliderect(ShareData.good_actor)