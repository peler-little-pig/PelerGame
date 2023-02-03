from Thing.BaseThing import *
from Egg.GunEgg import *


class GunThing(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(left, top, 100, 40, (17, 17), 68, 5, './Res/Picture/image/gun/gun.png', 1, GunEgg)
