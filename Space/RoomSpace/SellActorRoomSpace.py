from Actor.SellActor.BaseSellActor import BaseSellActor
from Space.RoomSpace.BaseRoomSpace import *


class SellActorRoomSpace(BaseRoomSpace):
    def __init__(self, name):
        super().__init__(name)

    def init(self, sell_group):
        self.sell = self.create_sell_treasure()
        sell_group.append(self.sell)

    def create_sell_treasure(self):
        width = self.corner_block_list[1].right - self.corner_block_list[0].left
        height = self.corner_block_list[3].bottom - self.corner_block_list[0].top
        return BaseSellActor(self.corner_block_list[0].x + (width / 2),
                             self.corner_block_list[0].y + (height / 2))

    def process(self):
        super().process()

    def draw(self):
        super().draw()
