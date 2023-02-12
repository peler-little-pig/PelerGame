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
                ShareData.good_actor.drop_thing_info_bar.set_thing(self[i])
                ShareData.good_actor.drop_thing_info_bar.draw()
                ShareData.good_actor.speak.begin_say(f'{self[i].name}?真是一件好武器',10)
                if EventData.is_right_mouse_down:
                    thing = self[i]
                    thing.rect.left = ShareData.good_actor.centerx
                    thing.rect.top = ShareData.good_actor.centery + 10
                    ShareData.good_actor.thing_list.append(thing)
                    ShareData.good_actor.thing_index = len(ShareData.good_actor.thing_list) - 1
                    ShareData.good_actor.thing = ShareData.good_actor.thing_list[ShareData.good_actor.thing_index]
                    ShareData.good_actor.thing_info_bar.set_thing(ShareData.good_actor.thing)
                    del self[i]
                    EventData.is_right_mouse_down = False
                    break

    def append(self, __object) -> None:
        super().append(__object)

    def append_random(self, center):
        thing = random.choice(thing_list)(0, 0)
        thing.rect.center = center
        super().append(thing)
