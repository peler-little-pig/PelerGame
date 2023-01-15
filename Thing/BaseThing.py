from typing import List
from Egg.BaseEgg import *
from Data.AllData import *
import pygame


class BaseThing():
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        self.egg_list: List[BaseEgg] = []
        self.WAIT = 5
        self.wait = 0

        self.image = pygame.image.load('./Res/image/gun/gun.png').convert_alpha()
        self.rect = pygame.rect.Rect(left, top, width, height)
        self.image_rotate = self.image

        self.degree = 0

    def fire(self):
        if self.wait == 0:
            egg = BaseEgg(self.rect.right, self.rect.top, 15, 10)
            self.egg_list.append(egg)
            self.wait = self.WAIT

            ShareData.energy_info_bar.value -= 1
        else:
            self.wait -= 1

    def draw(self):
        ConstData.surface.blit(self.image_rotate, self.rect)
        for egg in self.egg_list:
            egg.draw()

    def rotate(self):
        if EventData.is_mouse_move:
            self.degree, _ = get_degree(self.rect.x, self.rect.y, EventData.mouse_x, EventData.mouse_y)
            self.image_rotate = pygame.transform.rotate(self.image, self.degree)
            self.rect = self.image.get_rect(center=self.rect.center)

    def process(self):
        for i in range(len(self.egg_list)):
            egg = self.egg_list[i]

            egg.process()
            if egg.is_should_delete():
                del self.egg_list[i]
                break

    def move_ip(self, x: float, y: float):
        self.rect.move_ip(x, y)
