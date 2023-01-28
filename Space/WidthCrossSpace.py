from Block.BaseBlock import BaseBlock
from Block.CornerBlock import CornerBlock
from Space.BaseSpace import *
from Data.AllData import *

class WidthCrossSpace(BaseSpace):
    def __init__(self, name):
        super().__init__(name)

        self.base_block_list: List[BaseBlock] = []
        self.corner_block_list: List[CornerBlock] = []

    def mix(self):
        return self.base_block_list + self.corner_block_list

    def draw(self):
        for block in self.mix():
            block.draw()

    def can_move_up(self):
        return ShareData.good_actor.top > self.corner_block_list[0].bottom

    def can_move_down(self):
        return ShareData.good_actor.bottom < self.corner_block_list[3].top

    def can_move_left(self):
        return True

    def can_move_right(self):
        return True

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
        return not (ShareData.good_actor.top < self.corner_block_list[0].top
                    or ShareData.good_actor.bottom > self.corner_block_list[2].bottom
                    or ShareData.good_actor.left < self.corner_block_list[0].left - ActorData.SIZE_TUPLE[0]
                    or ShareData.good_actor.right > self.corner_block_list[1].right + ActorData.SIZE_TUPLE[
                        0])
