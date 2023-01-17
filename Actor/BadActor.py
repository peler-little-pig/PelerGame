from Actor.BaseActor import *
import random
from Compute.SpaceCompute import *
from Data.AllData import *


class BadActor(BaseActor):
    def __init__(self, x, y):
        super().__init__(x, y, *ConstData.NORMAL_ACTOR_SIZE_TUPLE)
        self.move_x = 0
        self.move_y = 0

        self.walk_around_WAIT = 130
        self.walk_around_wait = 0

        self.fire_to_good_WAIT = random.randint(60,150)
        self.fire_to_good_wait = 0

        self.blood = 15

        self.alive_image = pygame.image.load('./Res/image/bad_actor/bad_actor_alive.png').convert_alpha()
        self.dead_image = pygame.image.load('./Res/image/bad_actor/bad_actor_dead.png').convert_alpha()

    def draw(self):
        if self.is_alive():
            ConstData.surface.blit(self.alive_image, self)
            super().draw()
        else:
            ConstData.surface.blit(self.dead_image, self)

    def fire_to_good(self):
        if self.fire_to_good_wait == 0:
            self.thing.fire(*ShareData.good_actor.center,SpecalData.BAD_ACTOR)
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

        if is_hit_wall(self):
            self.move_x = -self.move_x
            self.move_y = -self.move_y
            self.walk_around_wait = 0
        self.move_ip(self.move_x, self.move_y)

    def process(self):
        if self.is_alive():
            super().process()
            self.thing.rotate(*ShareData.good_actor.center)
            self.walk_around()
            self.fire_to_good()

        if EventData.is_move_up:
            self.move_ip(0, ConstData.MOVE_SPEED)
        if EventData.is_move_down:
            self.move_ip(0, -ConstData.MOVE_SPEED)
        if EventData.is_move_left:
            self.move_ip(ConstData.MOVE_SPEED, 0)
        if EventData.is_move_right:
            self.move_ip(-ConstData.MOVE_SPEED, 0)

    def move_ip(self, x: float, y: float) -> None:
        super().move_ip(x, y)
        self.thing.move_ip(x, y)

    def is_alive(self):
        return self.blood > 0
