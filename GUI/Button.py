import pygame_gui
import pygame
from Data.AllData import *


class Button(pygame_gui.elements.UIButton):
    def __init__(self, manager, left: float, top: float, width: float, height: float, text: str,**kwargs):
        super().__init__(pygame.rect.Rect(left, top, width, height), text, manager=manager,**kwargs)
        self.click_function = None

    def event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self:
                self.click_function()
