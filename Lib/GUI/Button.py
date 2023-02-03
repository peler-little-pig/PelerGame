import pygame_gui
import pygame
from Data.AllData import *


class Button(pygame_gui.elements.UIButton):
    def __init__(self, left: float, top: float, width: float, height: float, text: str):
        super().__init__(pygame.rect.Rect(left, top, width, height), text, manager=GameData.UI_MANAGER)
        GameData.UI_MANAGER.ui_list.append(self)

    def event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self:
                print('HelloWorld')
