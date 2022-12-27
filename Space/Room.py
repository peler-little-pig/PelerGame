from typing import List
from Block.BaseBlock import BaseBlock
from Block.CornerBlock import CornerBlock
from Block.DoorBlock import DoorBlock
from Space.Space import *


class Room(Space):
    def __init__(self):
        super().__init__()

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []
        self.door_block_list: List[DoorBlock] = []

    def mix(self):
        return self.base_block_list + self.corner_block_list + self.door_block_list

    def draw(self):
        for wall in self.mix():
            wall.draw()

    def move_up(self, good_actor: GoodActor):
        if good_actor.top > self.corner_block_list[0].bottom \
                or (good_actor.left > self.door_block_list[0].right
                    and good_actor.right < self.door_block_list[-1].left):
            for block in self.mix():
                block.move_ip(0, Value.MOVE_SPEED)

    def move_down(self, good_actor: GoodActor):
        if good_actor.bottom < self.corner_block_list[2].top \
                or (good_actor.left > self.door_block_list[0].right
                    and good_actor.right < self.door_block_list[-1].left):
            for block in self.mix():
                block.move_ip(0, -Value.MOVE_SPEED)

    def move_left(self, good_actor: GoodActor):
        if good_actor.left > self.corner_block_list[0].right \
                or (good_actor.top > self.door_block_list[0].bottom
                    and good_actor.bottom < self.door_block_list[-1].top):
            for block in self.mix():
                block.move_ip(Value.MOVE_SPEED, 0)

    def move_right(self, good_actor: GoodActor):
        if good_actor.right < self.corner_block_list[1].left \
                or (good_actor.top > self.door_block_list[0].bottom
                    and good_actor.bottom < self.door_block_list[-1].top):
            for block in self.mix():
                block.move_ip(-Value.MOVE_SPEED, 0)
