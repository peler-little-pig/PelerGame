from typing import List
from Egg.BaseEgg import *
import pygame
from Data.AllData import *
from Lib.BetterPygame.Surface import *


class BaseThing():
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        self.egg_list: List[BaseEgg] = []
        self.WAIT = 5
        self.wait = 0

        self.image = pygame.image.load('./Res/image/gun/gun.png').convert_alpha()
        self.rect = pygame.rect.Rect(left, top, width, height)
        self.image_rotate = self.image
        self.rect_rotate = self.rect

        self.degree = 0
        self.dir = ()

    def fire(self, x, y, whose):
        if self.wait == 0:
            egg = BaseEgg(self.rect.x+self.dir[0]*68, self.rect.y+self.dir[1]*68, 15, 10, x, y, whose)

            self.egg_list.append(egg)
            self.wait = self.WAIT

            ShareData.good_actor.energy_info_bar.value -= 1
        else:
            self.wait -= 1

    def draw(self):
        # pygame.draw.rect(GameData.surface, (0, 0, 0), self.image_rotate.get_rect(center=self.rect_rotate.center))
        GameData.surface.blit(self.image_rotate, self.rect_rotate)
        for egg in self.egg_list:
            egg.draw()

    def rotate(self, x, y):
        self.degree, self.dir = get_degree(self.rect.x, self.rect.y, x, y)
        # if -90 < self.degree < 90:
        self.image_rotate, self.rect_rotate = rotate_at_pos(self.image, self.rect.topleft, (17, 17), self.degree)
        # self.rect = self.image.get_rect(center=self.rect.center)
        # else:
        #     self.image_rotate, self.rect_rotate = rotate_at_pos(self.image, self.rect.topleft, (17, 17), 180-self.degree)
        #     self.image_rotate = pygame.transform.flip(self.image_rotate,True,False)
            # self.rect = self.image.get_rect(left=self.rect.left,top=self.rect.top)

    def process(self):
        for i in range(len(self.egg_list)):
            egg = self.egg_list[i]

            egg.process()
            if egg.is_should_delete():
                del self.egg_list[i]
                break

    def move_ip(self, x: float, y: float):
        self.rect.move_ip(x, y)
