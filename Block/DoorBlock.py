from Block.BaseBlock import *


class DoorBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)

    def draw(self):
        pygame.draw.rect(Value.surface, Value.DOOR_BLOCK_COLOR, self)
