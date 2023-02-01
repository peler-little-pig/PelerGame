import pygame

from pygame_gui import UIManager, UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton

manager = UIManager((800, 600), './Lib/GUI/data/quick_theme.json')
hello_button = UIButton((350, 280), 'Hello')