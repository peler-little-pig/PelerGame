import pygame
from Data.AllData import *
from Lib.Compute.MoveCompute import *


class BaseTreasure(pygame.rect.Rect):
    def __init__(self, centerx,centery, width: float, height: float):
        super().__init__(0, 0, width, height)
        self.centerx = centerx
        self.centery = centery
        self.close_image = pygame.image.load('./Res/Picture/image/treasure/close.png').convert()
        self.open_image = pygame.image.load('./Res/Picture/image/treasure/open.png').convert()
        self.image = self.close_image

    def draw(self):
        GameData.surface.blit(self.image, self)

    def process(self):
        self.open()
        follow_move(self)

    def open(self):
        if self.colliderect(ShareData.good_actor):
            if EventData.is_right_mouse_down:
                self.image = self.open_image