from Block.BaseBlock import *


class CornerBlock(BaseBlock):
    def __init__(self, left: float, top: float):
        super().__init__(left, top)

    def draw(self):
        pygame.draw.rect(Value.surface, Value.CORNER_BLOCK_COLOR, self)

    def can_move_up(self, top: float):
        return self.bottom <= top

    def can_move_down(self,bottom:float):
        return self.top >= bottom

    def can_move_left(self,left:float):
        return self.right <= left

    def can_move_right(self,right:float):
        return self.left >= right