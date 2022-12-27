from typing import List
from Block.BaseBlock import BaseBlock
from Block.CornerBlock import CornerBlock
from Block.DoorBlock import DoorBlock
from Space.BaseSpace import *

from Value import Value


class Room(Space):
    def __init__(self):
        super().__init__()

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []
        self.top_door_block_list: List[DoorBlock] = []
        self.bottom_door_block_list: List[DoorBlock] = []
        self.left_door_block_list: List[DoorBlock] = []
        self.right_door_block_list: List[DoorBlock] = []

    def mix(self):
        return self.base_block_list + self.corner_block_list \
               + self.top_door_block_list + self.bottom_door_block_list \
               + self.right_door_block_list + self.left_door_block_list

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self, good_actor: GoodActor):
        if self.top_door_block_list:
            return (not good_actor.top < self.corner_block_list[0].bottom) \
                   or (good_actor.left > self.top_door_block_list[0].left
                       and good_actor.right < self.top_door_block_list[-1].right)
        else:
            return not good_actor.top < self.corner_block_list[0].bottom

    def can_move_down(self, good_actor: GoodActor):
        if self.bottom_door_block_list:
            return (not good_actor.bottom > self.corner_block_list[2].top) \
                   or (good_actor.left > self.bottom_door_block_list[0].left
                       and good_actor.right < self.bottom_door_block_list[-1].right)
        else:
            return not good_actor.bottom > self.corner_block_list[2].top

    def can_move_left(self, good_actor: GoodActor):
        if self.left_door_block_list:
            return (not good_actor.left < self.corner_block_list[0].right) \
                   or (good_actor.top > self.left_door_block_list[0].top
                       and good_actor.bottom < self.left_door_block_list[-1].bottom)
        else:
            return not good_actor.left < self.corner_block_list[0].right

    def can_move_right(self, good_actor: GoodActor):
        if self.right_door_block_list:
            return (not good_actor.right > self.corner_block_list[1].left) \
                   or (good_actor.top > self.right_door_block_list[0].top
                       and good_actor.bottom < self.right_door_block_list[-1].bottom)
        else:
            return not good_actor.right > self.corner_block_list[1].left

    def move_up(self, good_actor: GoodActor):
        # if self.can_move_up(good_actor):
        for block in self.mix():
            block.move_ip(0, Value.MOVE_SPEED)

    def move_down(self, good_actor: GoodActor):
        # if self.can_move_down(good_actor):
        for block in self.mix():
            block.move_ip(0, -Value.MOVE_SPEED)

    def move_left(self, good_actor: GoodActor):
        # if self.can_move_left(good_actor):
        for block in self.mix():
            block.move_ip(Value.MOVE_SPEED, 0)

    def move_right(self, good_actor: GoodActor):
        # if self.can_move_right(good_actor):
        for block in self.mix():
            block.move_ip(-Value.MOVE_SPEED, 0)

    def is_in_this_space(self, good_actor: GoodActor):
        return not (good_actor.top < self.corner_block_list[0].top
                    or good_actor.bottom > self.corner_block_list[2].bottom
                    or good_actor.left < self.corner_block_list[0].left
                    or good_actor.right > self.corner_block_list[1].right)
