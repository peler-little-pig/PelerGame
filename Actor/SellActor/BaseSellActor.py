from Actor.BaseActor import *
import random
from Speak.BaseSpeak import BaseSpeak
from Thing.BloodDrinkThing import BloodDrinkThing, follow_move
from Thing.EnergyDrinkThing import EnergyDrinkThing
from Data.AllData import *


class BaseSellActor(BaseActor):
    def __init__(self, centerx,centery):
        super().__init__(0, 0, 100, 130)
        self.centerx = centerx
        self.centery = centery

        self.image = pygame.image.load('./Res/Picture/image/seller/drinking_seller.png').convert_alpha()
        self.speak = BaseSpeak(self)
        self.cost = 10

    def draw(self):
        GameData.surface.blit(self.image, self)
        self.speak.draw()

    def process(self):
        self.speak.process()
        follow_move(self)

    def sell(self):
        money = ShareData.good_actor.money_info_bar.value
        if money < self.cost:
            ShareData.good_actor.speak.begin_say('钱不够，唉', 100)
        else:
            ShareData.good_actor.money_info_bar.set_value(money - self.cost)
            ShareData.drop_thing_group.append(
                random.choice([BloodDrinkThing, EnergyDrinkThing])(self.centerx, self.bottom + 50))
            self.cost *= 2
