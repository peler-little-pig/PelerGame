from typing import List
from Data.AllData import *


class SellActorGroup(List):
    def __init__(self):
        super().__init__()

    def draw(self):
        for sell_actor in self:
            sell_actor.draw()

    def process(self):
        for sell_actor in self:
            sell_actor.process()
        self.sell()

    def sell(self):
        for sell_actor in self:
            if sell_actor.colliderect(ShareData.good_actor):
                sell_actor.speak.begin_say(f'购买饮料？{sell_actor.cost}元一瓶', 1)
                if EventData.is_right_mouse_down:
                    sell_actor.sell()
                    EventData.is_right_mouse_down = False
