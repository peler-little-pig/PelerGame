from Lib.Compute.SpaceCompute import *
from Lib.Math.Math import *


class BaseEgg(object):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose) -> None:
        self.rect = pygame.rect.Rect(left, top, width, height)

        degree, self.dir = get_degree(left, top, x, y)

        self.egg_image = pygame.image.load('./Res/image/egg/egg.png').convert_alpha()
        self.egg_image = pygame.transform.rotate(self.egg_image, degree)
        self.speed = 10

        self.whose = whose

    def draw(self):
        self.rect = self.egg_image.get_rect(center=self.rect.center)
        ConstData.surface.blit(self.egg_image, self.rect)

    def update(self):
        self.rect.x = self.rect.x + self.dir[0] * self.speed
        self.rect.y = self.rect.y + self.dir[1] * self.speed

    def process(self):
        if EventData.is_move_up:
            self.rect.move_ip(0, ConstData.MOVE_SPEED)
        if EventData.is_move_down:
            self.rect.move_ip(0, -ConstData.MOVE_SPEED)
        if EventData.is_move_left:
            self.rect.move_ip(ConstData.MOVE_SPEED, 0)
        if EventData.is_move_right:
            self.rect.move_ip(-ConstData.MOVE_SPEED, 0)

        self.update()

    def is_hit_wall(self):
        return is_hit_wall(self.rect)

    def is_hit_bad_actor(self):
        if self.whose == SpecalData.GOOD_ACTOR:
            for bad_actor in ShareData.bad_actor_group.bad_actors():
                if self.rect.colliderect(bad_actor):
                    if bad_actor.is_alive():
                        bad_actor.blood -= 3
                        return True
            return False
        else:
            return False

    def is_hit_good_actor(self):
        if self.whose == SpecalData.BAD_ACTOR:
            if self.rect.colliderect(ShareData.good_actor):
                if ShareData.good_actor.is_alive():
                    ShareData.good_actor.get_hurt(2.5)
                return True
            return False
        else:
            return False

    def is_fly_away(self):
        return self.rect.x > ConstData.WINDOW_WIDTH + ConstData.DRAW_AREA_ADD

    def is_hit_blocking_block(self):
        return is_hit_blocking_block(self.rect, active_area(self.rect))

    def is_hit_box_block(self):
        area = active_area(self.rect)
        if type(area) == RoomSpace:
            for block in area.box_block_list:
                if self.rect.colliderect(block):
                    block.blood -= 3
                    return True
        return False

    def is_should_delete(self):
        return self.is_fly_away() \
               or self.is_hit_wall() \
               or self.is_hit_good_actor() \
               or self.is_hit_bad_actor() \
               or self.is_hit_blocking_block() \
               or self.is_hit_box_block()
