from Actor.BaseActor import *
import random
from Lib.Compute.SpaceCompute import *
from Lib.Compute.BlockCompute import *
from Lib.Compute.MoveCompute import *
from Data.AllData import *
from Coin.EnergyCoin import *
from Coin.MoneyCoin import *


class BadActor(BaseActor):
    def __init__(self, x, y):
        super().__init__(x, y, *ActorData.SIZE_TUPLE)
        self.move_x = 0
        self.move_y = 0

        self.walk_around_WAIT = 130
        self.walk_around_wait = 0

        self.fire_to_good_WAIT = random.randint(30, 60)
        self.fire_to_good_wait = self.fire_to_good_WAIT

        self.blood = 20

        self.alive_image = pygame.image.load('./Res/image/bad_actor/bad_actor_alive.png').convert_alpha()
        self.dead_image = pygame.image.load('./Res/image/bad_actor/bad_actor_dead.png').convert_alpha()

        self.is_coin_given = False

    def draw(self):
        if self.is_alive():
            GameData.surface.blit(self.alive_image, self)
            super().draw()
        else:
            GameData.surface.blit(self.dead_image, self)

    def fire_to_good(self):
        # if is_close(self, ShareData.good_actor, 500):
            if self.fire_to_good_wait == 0:
                self.thing.fire(*ShareData.good_actor.center, SpecialData.BAD_ACTOR)
                self.fire_to_good_wait = self.fire_to_good_WAIT
            else:
                self.fire_to_good_wait -= 1

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
        # print(self.thing.rect_rotate)
        if active_area(self) == active_area(ShareData.good_actor):
            if self.is_alive():
                super().process()
                self.thing.rotate(*ShareData.good_actor.center)
                self.walk_around()
                self.fire_to_good()
            else:
                self.give_coin()

        follow_move(self)

    def give_coin(self):
        if not self.is_coin_given:
            ShareData.coin_group.append(EnergyCoin(self.centerx, self.centery))
            # ShareData.coin_group.append(MoneyCoin(self.left, self.top))
            self.is_coin_given = True

    def move_ip(self, x: float, y: float) -> None:
        super().move_ip(x, y)
        self.thing.move_ip(x, y)

    def is_alive(self):
        return self.blood > 0
