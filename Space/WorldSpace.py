from typing import List

from Space.BaseSpace import *
from Space.RoomSpace import *
from Space.WidthCrossSpace import *


class World(Space):
    def __init__(self):
        super().__init__()
        self.area_list: List[Space, WidthCross] = []

    def draw(self):
        for area in self.area_list:
            area.draw()

    def can_move_up(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_up(good_actor)

    def can_move_down(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_down(good_actor)

    def can_move_left(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_left(good_actor)

    def can_move_right(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_right(good_actor)

    def move_up(self, good_actor: GoodActor):
        if self.can_move_up(good_actor):
            for area in self.area_list:
                area.move_up(good_actor)

    def move_down(self, good_actor: GoodActor):
        if self.can_move_down(good_actor):
            for area in self.area_list:
                area.move_down(good_actor)

    def move_left(self, good_actor: GoodActor):
        if self.can_move_left(good_actor):
            for area in self.area_list:
                area.move_left(good_actor)

    def move_right(self, good_actor: GoodActor):
        if self.can_move_right(good_actor):
            for area in self.area_list:
                area.move_right(good_actor)


