from Egg.BaseEgg import *


class NoneEgg(BaseEgg):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose):
        super().__init__(0, 0, 0, 0, 0, 0, 0, './Res/Picture/image/egg/egg.png', 0, 0)

    def draw(self):
        ...

    def update(self):
        ...

    def process(self):
        ...

    def is_hit_wall(self):
        ...

    def is_hit_bad_actor(self):
        ...

    def is_hit_good_actor(self):
        ...

    def is_hit_blocking_block(self):
        ...

    def is_hit_box_block(self):
        ...

    def is_should_delete(self):
        ...

