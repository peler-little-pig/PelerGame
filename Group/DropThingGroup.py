import random

from Thing.ThingList import *


class DropThingGroup(List[BaseThing]):
    def __init__(self):
        super().__init__()

    def draw(self):
        for thing in self:
            thing.draw()

    def process(self):
        for thing in self:
            thing.process()
            follow_move(thing.rect_rotate)
        self.pick_up()

    def pick_up(self):
        for i in range(len(self)):
            if self[i].rect_rotate.colliderect(ShareData.good_actor):
                if EventData.is_right_mouse_down:
                    thing = type(self[i])(ShareData.good_actor.centerx,ShareData.good_actor.centery + 10)
                    # thing.rect.left = ShareData.good_actor.centerx
                    # thing.rect.top = ShareData.good_actor.centery + 10
                    ShareData.good_actor.thing_list.append(thing)
                    ShareData.good_actor.thing_index = len(ShareData.good_actor.thing_list) - 1
                    ShareData.good_actor.thing = ShareData.good_actor.thing_list[ShareData.good_actor.thing_index]
                    del self[i]
                    EventData.is_right_mouse_down = False
                    break

    def append(self, __object) -> None:
        super().append(__object)

    def append_random(self, x, y):
        super().append(random.choice(thing_list)(x, y))
