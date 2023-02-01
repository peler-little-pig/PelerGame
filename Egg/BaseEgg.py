from Lib.Compute.SpaceCompute import *
from Lib.Compute.BlockCompute import *
from Lib.Compute.MoveCompute import *
from Lib.Math.Math import *


class BaseEgg(object):
    def __init__(self, left: float, top: float, width: float, height: float, x, y, whose, image_path, speed,
                 hurt) -> None:
        self.rect = pygame.rect.Rect(left, top, width, height)

        degree, self.dir = get_degree(left, top, x, y)

        self.egg_image = pygame.image.load(image_path).convert_alpha()
        self.egg_image = pygame.transform.rotate(self.egg_image, degree)
        self.speed = speed
        self.hurt = hurt

        self.whose = whose

    def draw(self):
        self.rect = self.egg_image.get_rect(center=self.rect.center)
        GameData.surface.blit(self.egg_image, self.rect)

    def update(self):
        self.rect.x = self.rect.x + self.dir[0] * self.speed
        self.rect.y = self.rect.y + self.dir[1] * self.speed

    def process(self):
        follow_move(self.rect)

        self.update()

    def is_hit_wall(self):
        return is_hit_wall(self.rect)

    def is_hit_bad_actor(self):
        if self.whose == SpecialData.GOOD_ACTOR:
            for bad_actor in ShareData.bad_actor_group.bad_actors():
                if self.rect.colliderect(bad_actor):
                    if bad_actor.is_alive():
                        bad_actor.blood -= self.hurt
                        return True
            return False
        else:
            return False

    def is_hit_good_actor(self):
        if self.whose == SpecialData.BAD_ACTOR:
            if self.rect.colliderect(ShareData.good_actor):
                if ShareData.good_actor.is_alive():
                    ShareData.good_actor.get_hurt(self.hurt)
                return True
            return False
        else:
            return False

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
        return self.is_hit_wall() \
               or self.is_hit_good_actor() \
               or self.is_hit_bad_actor() \
               or self.is_hit_blocking_block() \
               or self.is_hit_box_block()
