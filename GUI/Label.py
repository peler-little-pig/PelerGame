import pygame_gui
import pygame
from Data.AllData import *


class Label(pygame_gui.elements.UILabel):
    def __init__(self, left: float, top: float, width: float, height: float, text: str):
        super().__init__(pygame.rect.Rect(left, top, width, height), text, manager=GameData.UI_MANAGER)

    def event(self, event):
        ...
