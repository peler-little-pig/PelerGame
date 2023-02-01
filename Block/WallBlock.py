from Block.BaseBlock import *
import pygame


class WallBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.image_list = [
            pygame.image.load(f'./Res/Picture/image/wall_block/wall_block{i}.png').convert() for i in range(1, 6)]
        self.image_tuple = (0, 0, 0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 0, 0, 0)
        self.image_index = 0
        self.image_WAIT = 5
        self.image_wait = self.image_WAIT

    def draw(self):
        # if self.is_need_draw():
            GameData.surface.blit(self.image_list[self.image_tuple[self.image_index]], self)

    def process(self):
        if self.image_wait == 0:
            if self.image_index != len(self.image_tuple) - 1:
                self.image_index += 1
            else:
                self.image_index = 0
            self.image_wait = self.image_WAIT
        else:
            self.image_wait -= 1