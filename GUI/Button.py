from GUI.Base import Base
import pygame
from Data.AllData import *


class Button(Base):
    def __init__(self, left: float, top: float, width: float, height: float):
        super().__init__(left, top, width, height)

    def draw(self):
        pygame.draw.rect(ConstData.surface, (0, 0, 255), self)
