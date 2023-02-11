import pygame_gui
import pygame
from Data.AllData import *


class Label(pygame_gui.elements.UILabel):
    def __init__(self, manager, left: float, top: float, width: float, height: float, text: str,**kwargs):
        super().__init__(pygame.rect.Rect(left, top, width, height), text, manager=manager,**kwargs)
        self.text_horiz_alignment = 'left'

    def event(self, event):
        ...
