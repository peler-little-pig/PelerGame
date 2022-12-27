from typing import List

from Space.Space import *
from Space.Room import *
from Space.WidthCross import *


class World(Space):
    def __init__(self):
        super().__init__()
        self.area_list: List[Space, WidthCross] = []

    def draw(self):
        for area in self.area_list:
            area.draw()

    def move_up(self, good_actor: GoodActor):
        for area in self.area_list:
            area.move_up(good_actor)

    def move_down(self, good_actor: GoodActor):
        for area in self.area_list:
            area.move_down(good_actor)

    def move_left(self, good_actor: GoodActor):
        for area in self.area_list:
            area.move_left(good_actor)

    def move_right(self, good_actor: GoodActor):
        for area in self.area_list:
            area.move_right(good_actor)


