from typing import Tuple
from Data.AllData import *

import pygame
import pygame_gui


class Manager(pygame_gui.UIManager):
    def __init__(self):
        super().__init__((GameData.WINDOW_WIDTH, GameData.WINDOW_HEIGHT))
        self.ui_list = []

    def draw(self):
        super().draw_ui(GameData.surface)

    def process(self):
        super().update(GameData.fps_clock.tick(60) / 1000)

    def event(self, event):
        super().process_events(event)

        for ui in self.ui_list:
            ui.event(event)
