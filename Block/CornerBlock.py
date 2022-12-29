from Block.BaseBlock import *
import pygame


class CornerBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image = pygame.image.load('./rec/image/corner_block/corner_block.png')

    def draw(self):
        Value.surface.blit(self.image, self)

    def can_move_up(self, top: float):
        return self.bottom <= top

    def can_move_down(self, bottom: float):
        return self.top >= bottom

    def can_move_left(self, left: float):
        return self.right <= left

    def can_move_right(self, right: float):
        return self.left >= right
