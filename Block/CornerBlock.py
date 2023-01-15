from Block.BaseBlock import *
import pygame


class CornerBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./Res/image/corner_block/corner_block.png').convert()

    def draw(self):
        # if self.is_need_draw():
            ConstData.surface.blit(self.image, self)

    def can_move_up(self, top: float):
        return self.bottom <= top

    def can_move_down(self, bottom: float):
        return self.top >= bottom

    def can_move_left(self, left: float):
        return self.right <= left

    def can_move_right(self, right: float):
        return self.left >= right
