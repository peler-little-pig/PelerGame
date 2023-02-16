from Space.RoomSpace.BaseRoomSpace import *


class TreasureRoomSpace(BaseRoomSpace):
    def __init__(self, name):
        super().__init__(name)

    def init(self,treasure_group):
        self.treasure = self.create_thing_treasure()
        # treasure_group.append(self.treasure)

    def create_thing_treasure(self):
        width = self.corner_block_list[1].right - self.corner_block_list[0].left
        height = self.corner_block_list[3].bottom - self.corner_block_list[0].top
        return BaseTreasure(self.corner_block_list[0].x + (width / 2),
                            self.corner_block_list[0].y + (height / 2),
                            100, 50)

    def process(self):
        super().process()
        self.treasure.process()

    def draw(self):
        super().draw()
        self.treasure.draw()
