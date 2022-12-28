from typing import List

from Space.BaseSpace import *
from Space.RoomSpace import *
from Space.WidthCrossSpace import *
from Space.HeightCrossSpace import *


class WorldSpace(Space):
    def __init__(self, name):
        super().__init__(name)
        self.area_list: List[RoomSpace, WidthCrossSpace, HeightCrossSpace] = []

    def draw(self):
        for area in self.area_list:
            area.draw()

    def can_move_up(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_up(good_actor)
        return False

    def can_move_down(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_down(good_actor)
        return False

    def can_move_left(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_left(good_actor)
        return False

    def can_move_right(self, good_actor: GoodActor):
        for area in self.area_list:
            if area.is_in_this_space(good_actor):
                return area.can_move_right(good_actor)
        return False

    def move_up(self, good_actor: GoodActor):
        if self.can_move_up(good_actor):
            for area in self.area_list:
                area.move_up(good_actor)
            return True
        else:
            return False

    def move_down(self, good_actor: GoodActor):
        if self.can_move_down(good_actor):
            for area in self.area_list:
                area.move_down(good_actor)
            return True
        else:
            return False

    def move_left(self, good_actor: GoodActor):
        if self.can_move_left(good_actor):
            for area in self.area_list:
                area.move_left(good_actor)
            return True
        else:
            return False

    def move_right(self, good_actor: GoodActor):
        if self.can_move_right(good_actor):
            for area in self.area_list:
                area.move_right(good_actor)
            return True
        else:
            return False

    def search(self, name: str):
        for area in self.area_list:
            if area.name == name:
                return area

    def process(self, good_actor: GoodActor):
        Value.is_move_up = False
        Value.is_move_down = False
        Value.is_move_left = False
        Value.is_move_right = False
        if Value.is_key_w_down:
            Value.is_move_up = self.move_up(good_actor)
        if Value.is_key_s_down:
            Value.is_move_down = self.move_down(good_actor)
        if Value.is_key_a_down:
            Value.is_move_left = self.move_left(good_actor)
        if Value.is_key_d_down:
            Value.is_move_right = self.move_right(good_actor)
