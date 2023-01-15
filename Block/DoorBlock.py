from Block.BaseBlock import *
import pygame


class DoorBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.open_image = pygame.image.load('./Res/image/door_block/door_block_open.png').convert()
        self.close_image = pygame.image.load('./Res/image/door_block/door_block_close.png').convert()
        self.image = self.open_image

    def draw(self):
        # if self.is_need_draw():
            ConstData.surface.blit(self.image, self)

    def open_or_close(self, is_open: bool):
        if is_open:
            self.image = self.open_image
        else:
            self.image = self.close_image
