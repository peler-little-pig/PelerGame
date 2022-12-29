from Block.BaseBlock import *
import pygame

class DoorBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.open_image = pygame.image.load('./rec/image/door_block/door_block_open.png')
        self.close_image = pygame.image.load('./rec/image/door_block/door_block_close.png')

    def draw(self):
        Value.surface.blit(self.close_image, self)
