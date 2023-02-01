from typing import List
from Egg.BaseEgg import *
import pygame
from Data.AllData import *
from Lib.BetterPygame.Surface import *


class BaseThing(object):
    def __init__(self, left: float, top: float, width: float, height: float, rotate_point, length, WAIT, image_path,
                 cost, egg_type) -> None:
        self.egg_list: List[BaseEgg] = []
        self.WAIT = WAIT
        self.wait = 0

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.rect.Rect(left, top, width, height)
        self.image_rotate = self.image
        self.rect_rotate = self.rect
        self.image_flip = pygame.transform.flip(self.image, True, False)
        self.rect_flip = self.image_flip.get_rect(topleft=self.rect.topleft)

        self.degree = 0
        self.dir = ()

        self.egg_type = egg_type
        self.cost = cost
        self.rotate_point = rotate_point
        self.length = length

    def fire(self, x, y, whose):
        if ShareData.good_actor.energy_info_bar.value - self.cost >= 0:
            if self.wait == 0:
                egg = self.egg_type(self.rect.x + self.dir[0] * self.length, self.rect.y + self.dir[1] * self.length,
                                    15, 10, x, y, whose)

                self.egg_list.append(egg)
                self.wait = self.WAIT
                if whose == SpecialData.GOOD_ACTOR:
                    ShareData.good_actor.energy_info_bar.value -= self.cost
            else:
                self.wait -= 1

    def draw(self):
        # pygame.draw.rect(GameData.surface, (0, 0, 0), self.image_rotate.get_rect(center=self.rect_rotate.center))
        GameData.surface.blit(self.image_rotate, self.rect_rotate)
        for egg in self.egg_list:
            egg.draw()

    def rotate(self, x, y):
        self.degree, self.dir = get_degree(self.rect.x, self.rect.y, x, y)
        if -90 < self.degree < 90:
            self.image_rotate, self.rect_rotate = rotate_at_pos(self.image, self.rect.topleft, self.rotate_point,
                                                                self.degree)
        else:
            self.image_rotate, self.rect_rotate = rotate_at_pos(self.image_flip, self.rect_flip.topleft, (
                self.rect.width - self.rotate_point[0], self.rotate_point[1]),
                                                                180 + self.degree)

    def process(self):
        for i in range(len(self.egg_list)):
            egg = self.egg_list[i]

            egg.process()
            if egg.is_should_delete():
                del self.egg_list[i]
                break

    def move_ip(self, x: float, y: float):
        self.rect.move_ip(x, y)
        self.rect_flip.move_ip(x, y)
