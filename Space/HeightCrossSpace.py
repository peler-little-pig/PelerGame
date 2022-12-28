from typing import List

from Block.BaseBlock import BaseBlock
from Block.CornerBlock import CornerBlock
from Space.BaseSpace import *
from Value import *


class HeightCrossSpace(Space):
    def __init__(self, name):
        super().__init__(name)

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []

    def mix(self):
        return self.base_block_list + self.corner_block_list

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self, good_actor: GoodActor):
        return True

    def can_move_down(self, good_actor: GoodActor):
        return True

    def can_move_left(self, good_actor: GoodActor):
        return good_actor.left > self.corner_block_list[0].right

    def can_move_right(self, good_actor: GoodActor):
        return good_actor.right < self.corner_block_list[1].left

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
        return not (good_actor.top < self.corner_block_list[0].top - Value.NORMAL_ACTOR_SIZE_TUPLE[1]
                    or good_actor.bottom > self.corner_block_list[2].bottom + Value.NORMAL_ACTOR_SIZE_TUPLE[1]
                    or good_actor.left < self.corner_block_list[0].left
                    or good_actor.right > self.corner_block_list[1].right)
