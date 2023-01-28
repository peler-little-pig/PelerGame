import pygame
from Data.AllData import *


class Label(object):
    def __init__(self, x, y, text, color):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, 24)

    def draw(self):
        image_text = self.font.render(self.text, True, self.color)
        GameData.surface.blit(image_text,(self.x,self.y))
