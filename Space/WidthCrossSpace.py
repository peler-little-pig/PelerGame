from typing import List

from Block.BaseBlock import BaseBlock
from Block.CornerBlock import CornerBlock
from Space.BaseSpace import *


class WidthCross(Space):
    def __init__(self):
        super().__init__()

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []

    def mix(self):
        return self.base_block_list + self.corner_block_list

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self, good_actor: GoodActor):
        return good_actor.top > self.corner_block_list[0].bottom

    def can_move_down(self, good_actor: GoodActor):
        return good_actor.bottom < self.corner_block_list[3].top

    def can_move_left(self, good_actor: GoodActor):
        return True

    def can_move_right(self, good_actor: GoodActor):
        return True

    def move_up(self, good_actor: GoodActor):
        if self.can_move_up(good_actor):
            for block in self.base_block_list:
                block.move_ip(0, Value.MOVE_SPEED)

    def move_down(self, good_actor: GoodActor):
        if self.can_move_down(good_actor):
            for block in self.base_block_list:
                block.move_ip(0, -Value.MOVE_SPEED)

    def move_left(self, good_actor: GoodActor):
        if self.can_move_left(good_actor):
            for block in self.base_block_list:
                block.move_ip(Value.MOVE_SPEED, 0)

    def move_right(self, good_actor: GoodActor):
        if self.can_move_right(good_actor):
            for block in self.base_block_list:
                block.move_ip(-Value.MOVE_SPEED, 0)

    # def is_in_this_space(self, good_actor: GoodActor):
    #     return good_actor.top > self.base_block_list[0].bottom \
    #            and good_actor.bottom < self.corner_block_list[2].bottom \
    #            and good_actor.left > self.corner_block_list[0].right \
    #            and good_actor.right < self.corner_block_list[1].left

