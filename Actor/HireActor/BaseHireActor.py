from Actor.BaseActor import *
import random
from Coin.EnergyCoin import *
from Coin.MoneyCoin import MoneyCoin
from Speak.BaseSpeak import BaseSpeak
from Thing.GunThing import *


class BaseHireActor(BaseActor):
    def __init__(self, x, y):
        super().__init__(x, y, *ActorData.SIZE_TUPLE)
        self.move_x = 0
        self.move_y = 0

        self.walk_around_WAIT = 130
        self.walk_around_wait = 0

        self.follow_good_actor_wait = 0
        self.follow_good_actor_WAIT = 200

        self.fire_to_bad_WAIT = random.randint(20, 50)
        self.fire_to_bad_wait = self.fire_to_bad_WAIT

        self.blood = 10

        self.alive_image = pygame.image.load('./Res/Picture/image/hire_actor/alive.png').convert_alpha()
        self.dead_image = pygame.image.load('./Res/Picture/image/hire_actor/dead.png').convert_alpha()

        self.thing = GunThing(self.centerx, self.centery + 10)

        self.is_hired = False
        self.speak = BaseSpeak(self)
        self.cost = 10

    def draw(self):
        if self.is_alive():
            GameData.surface.blit(self.alive_image, self)
            super().draw()
            self.speak.draw()
        else:
            GameData.surface.blit(self.dead_image, self)

    def fire_to_bad(self):
        distance_ = 100000
        bad_actor_ = None
        for bad_actor in ShareData.bad_actor_group.bad_actors():
            distance_value = distance(bad_actor,self)
            if distance_value < distance_:
                bad_actor_ = bad_actor
                distance_ = distance_value
        if self.fire_to_bad_wait == 0:
            self.thing.fire(*bad_actor_.center, SpecialData.GOOD_ACTOR)
            self.fire_to_bad_wait = self.fire_to_bad_WAIT
        else:
            self.fire_to_bad_wait -= 1

    def walk_around(self):
        if self.walk_around_wait == 0:
            self.move_x = random.randint(-1, 1)
            self.move_y = random.randint(-1, 1)
            self.walk_around_wait = self.walk_around_WAIT
        else:
            self.walk_around_wait -= 1

        if is_hit_wall(self) or is_hit_blocking_block(self, active_area(self)) \
                or is_hit_box_block(self, active_area(self)):
            self.move_x = -self.move_x
            self.move_y = -self.move_y
            self.walk_around_wait = 0
        self.move_ip(self.move_x, self.move_y)

    def process(self):
        if self.is_alive():
            super().process()
            self.speak.process()
            if self.is_hired:
                self.thing.rotate(*ShareData.good_actor.center)
                self.walk_around()
                self.fire_to_bad()
                self.follow_good_actor()
        follow_move(self)

    def move_ip(self, x: float, y: float) -> None:
        super().move_ip(x, y)
        self.thing.move_ip(x, y)

    def move_to(self, x: int, y: int) -> None:
        self.left = x
        self.top = y
        self.thing.move_to(self.centerx, self.centery + 10)

    def is_alive(self):
        return self.blood > 0

    def hire(self):
        self.speak.begin_say('hello', 100)
        self.is_hired = True

    def follow_good_actor(self):
        if self.follow_good_actor_wait == 0:
            if self.walk_around_wait == self.walk_around_WAIT:
                self.move_to(*ShareData.good_actor.topleft)
                self.follow_good_actor_wait = self.follow_good_actor_WAIT
        else:
            self.follow_good_actor_wait -= 1
