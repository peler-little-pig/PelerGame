from Space.Space import *


class WidthCross(Space):
    def __init__(self):
        super().__init__()

        self.base_block_list: List[BaseBlock] = []

    def draw(self):
        for wall in self.base_block_list:
            wall.draw()

    def move_up(self, good_actor: GoodActor):
        if good_actor.top > self.base_block_list[0].bottom:
            for block in self.base_block_list:
                block.move_ip(0, Value.MOVE_SPEED)

    def move_down(self, good_actor: GoodActor):
        if good_actor.bottom < self.base_block_list[-1].top:
            for block in self.base_block_list:
                block.move_ip(0, -Value.MOVE_SPEED)

    def move_left(self, good_actor: GoodActor):
        for block in self.base_block_list:
            block.move_ip(Value.MOVE_SPEED, 0)

    def move_right(self, good_actor: GoodActor):
        for block in self.base_block_list:
            block.move_ip(-Value.MOVE_SPEED, 0)
