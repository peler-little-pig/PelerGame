from Block.BaseBlock import *
import pygame


class NextBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/image/ground_block/ground_block.png').convert()

    def draw(self):
        # if self.is_need_draw():
            pygame.draw.rect(ConstData.surface,(255,255,255),self)
        # pass

    def process(self):
        if self.colliderect(ShareData.good_actor):
            ShareData.game.next_world()
