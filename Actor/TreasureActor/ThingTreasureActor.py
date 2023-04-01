from Actor.TreasureActor.BaseTreasureActor import *


class ThingTreasureActor(BaseTreasureActor):
    def __init__(self, centerx, centery, width: float, height: float):
        super().__init__(centerx, centery, width, height, './Res/Picture/image/treasure/close.png',
                         './Res/Picture/image/treasure/open.png')

    def open(self):
        ShareData.drop_thing_group.append_random(self.center)