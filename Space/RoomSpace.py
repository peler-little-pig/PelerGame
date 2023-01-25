from typing import List
from Lib.BetterPygame.Rect import *
from Block.BoxBlock import BoxBlock
from Block.CornerBlock import CornerBlock
from Block.BlockingBlcok import BlockingBlock
from Block.DoorBlock import DoorBlock
from Block.GroundBlock import GroundBlock
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
        self.box_block_list: List[BoxBlock] = []

        self.is_door_need_close = False
        self.is_door_open = True

        self.bad_actor_number = 0

    def mix(self):
        return self.base_block_list + self.corner_block_list \
               + self.top_door_block_list + self.bottom_door_block_list \
               + self.right_door_block_list + self.left_door_block_list \
               + self.blocking_block_list + self.box_block_list

    def process(self):
        super().process()
        self.delete_box_block()
        for door in self.top_door_block_list + self.bottom_door_block_list \
                    + self.left_door_block_list + self.right_door_block_list:
            door.open_or_close(self.is_door_open)

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self):
        if self.is_hit_blocking_or_box_block_top():
            if self.top_door_block_list:
                return (not ShareData.good_actor.top < self.corner_block_list[0].bottom) \
                       or (ShareData.good_actor.left > self.top_door_block_list[0].left
                           and ShareData.good_actor.right < self.top_door_block_list[-1].right and self.is_door_open)
            else:
                return not ShareData.good_actor.top < self.corner_block_list[0].bottom
        else:
            return False

    def can_move_down(self):
        if self.is_hit_blocking_or_box_block_bottom():
            if self.bottom_door_block_list:
                return (not ShareData.good_actor.bottom > self.corner_block_list[2].top) \
                       or (ShareData.good_actor.left > self.bottom_door_block_list[0].left
                           and ShareData.good_actor.right < self.bottom_door_block_list[-1].right and self.is_door_open)
            else:
                return not ShareData.good_actor.bottom > self.corner_block_list[2].top
        else:
            return False

    def can_move_left(self):
        if self.is_hit_blocking_or_box_block_left():
            if self.left_door_block_list:
                return (not ShareData.good_actor.left < self.corner_block_list[0].right) \
                       or (ShareData.good_actor.top > self.left_door_block_list[0].top
                           and ShareData.good_actor.bottom < self.left_door_block_list[-1].bottom and self.is_door_open)
            else:
                return not ShareData.good_actor.left < self.corner_block_list[0].right
        else:
            return False

    def can_move_right(self):
        if self.is_hit_blocking_or_box_block_right():
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

    def is_hit_blocking_or_box_block_top(self):
        for block in self.blocking_block_list + self.box_block_list:
            if colliderect_bottom(ShareData.good_actor, block):
                return False
        else:
            return True

    def is_hit_blocking_or_box_block_bottom(self):
        for block in self.blocking_block_list + self.box_block_list:
            if colliderect_top(ShareData.good_actor, block):
                return False
        else:
            return True

    def is_hit_blocking_or_box_block_left(self):
        for block in self.blocking_block_list + self.box_block_list:
            if colliderect_right(ShareData.good_actor, block):
                return False
        else:
            return True

    def is_hit_blocking_or_box_block_right(self):
        for block in self.blocking_block_list + self.box_block_list:
            if colliderect_left(ShareData.good_actor, block):
                return False
        else:
            return True

    def delete_box_block(self):
        for i in range(len(self.box_block_list)):
            box_block = self.box_block_list[i]
            if box_block.is_should_delete():
                self.base_block_list.append(GroundBlock(box_block.left, box_block.top))
                del self.box_block_list[i]
                break
