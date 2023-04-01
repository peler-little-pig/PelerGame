from Actor.TreasureActor.BaseTreasureActor import *
from Coin.EnergyCoin import EnergyCoin


class EnergyTreasureActor(BaseTreasureActor):
    def __init__(self, centerx, centery, width: float, height: float):
        super().__init__(centerx, centery, width, height, './Res/Picture/image/treasure/close.png', './Res/Picture/image/treasure/open.png')

    def open(self):
        for i in range(5):
            ShareData.coin_group.append(EnergyCoin(self.left, self.top))