from Thing.BaseThing import *
from Egg.HandGunEgg import *


class HandGunThing(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(left, top, (0, 0),20, 10, './Res/image/hand_gun/hand_gun.png', 0, HandGunEgg)
