from typing import List

from Block.CornerBlock import CornerBlock
from Block.BlockingBlcok import BlockingBlock
from Block.DoorBlock import DoorBlock
from Space.BaseSpace import *
from Data.AllData import *


class RoomSpace(BaseSpace):
    def __init__(self, name):
        super().__init__(name)

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []
        self.top_door_block_list: List[DoorBlock] = []
        self.bottom_door_block_list: List[DoorBlock] = []
        self.left_door_block_list: List[DoorBlock] = []
        self.right_door_block_list: List[DoorBlock] = []
        self.blocking_block_list: List[BlockingBlock] = []

        self.is_door_need_close = False
        self.is_door_open = True

        self.bad_actor_number = 0

        self.blocking_block_can_move_up = True
        self.blocking_block_can_move_down = True
        self.blocking_block_can_move_left = True
        self.blocking_block_can_move_right = True

    def mix(self):
        return self.base_block_list + self.corner_block_list \
               + self.top_door_block_list + self.bottom_door_block_list \
               + self.right_door_block_list + self.left_door_block_list \
               + self.blocking_block_list

    def process(self):
        super().process()
        self.is_hit_blocking_block()
        for door in self.top_door_block_list + self.bottom_door_block_list \
                    + self.left_door_block_list + self.right_door_block_list:
            door.open_or_close(self.is_door_open)

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self):
        if self.blocking_block_can_move_up:
            if self.top_door_block_list:
                return (not ShareData.good_actor.top < self.corner_block_list[0].bottom) \
                       or (ShareData.good_actor.left > self.top_door_block_list[0].left
                           and ShareData.good_actor.right < self.top_door_block_list[-1].right and self.is_door_open)
            else:
                return not ShareData.good_actor.top < self.corner_block_list[0].bottom
        else:
            return False

    def can_move_down(self):
        if self.blocking_block_can_move_down:
            if self.bottom_door_block_list:
                return (not ShareData.good_actor.bottom > self.corner_block_list[2].top) \
                       or (ShareData.good_actor.left > self.bottom_door_block_list[0].left
                           and ShareData.good_actor.right < self.bottom_door_block_list[-1].right and self.is_door_open)
            else:
                return not ShareData.good_actor.bottom > self.corner_block_list[2].top
        else:
            return False

    def can_move_left(self):
        if self.blocking_block_can_move_left:
            if self.left_door_block_list:
                return (not ShareData.good_actor.left < self.corner_block_list[0].right) \
                       or (ShareData.good_actor.top > self.left_door_block_list[0].top
                           and ShareData.good_actor.bottom < self.left_door_block_list[-1].bottom and self.is_door_open)
            else:
                return not ShareData.good_actor.left < self.corner_block_list[0].right
        else:
            return False

    def can_move_right(self):
        if self.blocking_block_can_move_right:
            if self.right_door_block_list:
                return (not ShareData.good_actor.right > self.corner_block_list[1].left) \
                       or (ShareData.good_actor.top > self.right_door_block_list[0].top
                           and ShareData.good_actor.bottom < self.right_door_block_list[
                               -1].bottom and self.is_door_open)
            else:
                return not ShareData.good_actor.right > self.corner_block_list[1].left
        else:
            return False

    def move_up(self):
        # if self.can_move_up(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, ConstData.MOVE_SPEED)

    def move_down(self):
        # if self.can_move_down(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, -ConstData.MOVE_SPEED)

    def move_left(self):
        # if self.can_move_left(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(ConstData.MOVE_SPEED, 0)

    def move_right(self):
        # if self.can_move_right(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(-ConstData.MOVE_SPEED, 0)

    def is_in_this_space(self):
        if not (ShareData.good_actor.top < self.corner_block_list[0].top
                or ShareData.good_actor.bottom > self.corner_block_list[2].bottom
                or ShareData.good_actor.left < self.corner_block_list[0].left
                or ShareData.good_actor.right > self.corner_block_list[1].right):
            if self.is_door_need_close:
                self.is_door_open = False
                self.is_door_need_close = False
            return True
        else:
            return False

    def is_hit_blocking_block(self):
        if self.blocking_block_list:
            is_hit = False
            for block in self.blocking_block_list:
                if block.is_hit():
                    is_hit = True
                    if (self.blocking_block_can_move_up
                            and self.blocking_block_can_move_down
                            and self.blocking_block_can_move_left
                            and self.blocking_block_can_move_right):
                        if EventData.is_move_up:
                            self.blocking_block_can_move_up = False
                        if EventData.is_move_down:
                            self.blocking_block_can_move_down = False
                        if EventData.is_move_left:
                            self.blocking_block_can_move_left = False
                        if EventData.is_move_right:
                            self.blocking_block_can_move_right = False

            if not is_hit:
                self.blocking_block_can_move_up = True
                self.blocking_block_can_move_down = True
                self.blocking_block_can_move_left = True
                self.blocking_block_can_move_right = True
