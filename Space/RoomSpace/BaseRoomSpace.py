from typing import List
from Coin.EnergyCoin import EnergyCoin
from BetterPygame.Rect import *
from Block.BoxBlock import BoxBlock
from Block.CornerBlock import CornerBlock
from Block.BlockingBlcok import BlockingBlock
from Block.DoorBlock import DoorBlock
from Block.GroundBlock import GroundBlock
from Space.BaseSpace import *
from Treasure.BaseTreasure import *
from Treasure.EnergyTreasure import EnergyTreasure


class BaseRoomSpace(BaseSpace):
    def __init__(self, name):
        super().__init__(name)

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

    def process(self):
        super().process()

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self):
        if self.top_door_block_list:
            return (not ShareData.good_actor.top < self.corner_block_list[0].bottom) \
                   or (ShareData.good_actor.left > self.top_door_block_list[0].left
                       and ShareData.good_actor.right < self.top_door_block_list[-1].right and self.is_door_open)
        else:
            return not ShareData.good_actor.top < self.corner_block_list[0].bottom

    def can_move_down(self):
        if self.bottom_door_block_list:
            return (not ShareData.good_actor.bottom > self.corner_block_list[2].top) \
                   or (ShareData.good_actor.left > self.bottom_door_block_list[0].left
                       and ShareData.good_actor.right < self.bottom_door_block_list[-1].right and self.is_door_open)
        else:
            return not ShareData.good_actor.bottom > self.corner_block_list[2].top

    def can_move_left(self):
        if self.left_door_block_list:
            return (not ShareData.good_actor.left < self.corner_block_list[0].right) \
                   or (ShareData.good_actor.top > self.left_door_block_list[0].top
                       and ShareData.good_actor.bottom < self.left_door_block_list[-1].bottom and self.is_door_open)
        else:
            return not ShareData.good_actor.left < self.corner_block_list[0].right

    def can_move_right(self):
        if self.right_door_block_list:
            return (not ShareData.good_actor.right > self.corner_block_list[1].left) \
                   or (ShareData.good_actor.top > self.right_door_block_list[0].top
                       and ShareData.good_actor.bottom < self.right_door_block_list[
                           -1].bottom and self.is_door_open)
        else:
            return not ShareData.good_actor.right > self.corner_block_list[1].left

    def move_up(self):
        # if self.can_move_up(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, ActorData.MOVE_SPEED)

    def move_down(self):
        # if self.can_move_down(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, -ActorData.MOVE_SPEED)

    def move_left(self):
        # if self.can_move_left(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(ActorData.MOVE_SPEED, 0)

    def move_right(self):
        # if self.can_move_right(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(-ActorData.MOVE_SPEED, 0)

    def is_in_this_space(self):
        if not (ShareData.good_actor.top < self.corner_block_list[0].top
                or ShareData.good_actor.bottom > self.corner_block_list[2].bottom
                or ShareData.good_actor.left < self.corner_block_list[0].left
                or ShareData.good_actor.right > self.corner_block_list[1].right):
            return True
        else:
            return False
