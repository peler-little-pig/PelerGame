from Egg.BaseEgg import *


class GunEgg(BaseEgg):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose):
        super().__init__(left, top, width, height, x, y, whose, './Res/image/egg/egg.png', 10, 3)
