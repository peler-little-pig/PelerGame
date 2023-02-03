from Block.BaseBlock import *
import pygame


class BoxBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/Picture/image/box_block/box_block.png').convert()
        self.blood = 5
        self.is_coin_given = False

    def draw(self):
        # if self.is_need_draw():
            GameData.surface.blit(self.image, self)

    # pass

    def is_hit(self):
        return self.colliderect(ShareData.good_actor)

    def is_should_delete(self):
        return self.blood <= 0
