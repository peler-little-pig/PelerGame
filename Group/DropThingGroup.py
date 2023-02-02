from Thing.BaseThing import *


class DropThingGroup(List[BaseThing]):
    def __init__(self):
        super().__init__()

    def draw(self):
        for thing in self:
            thing.draw()

    def process(self):
        self.pick_up()
        for thing in self:
            thing.process()
            follow_move(thing.rect)

    def pick_up(self):
        for i in range(len(self)):
            if self[i].rect.colliderect(ShareData.good_actor):
                if EventData.is_right_mouse_down:
                    thing = self[i]
                    thing.rect.left = ShareData.good_actor.centerx
                    thing.rect.top = ShareData.good_actor.centery + 10
                    ShareData.good_actor.thing_list.append(self[i])
                    ShareData.good_actor.thing_index = len(ShareData.good_actor.thing_list) - 1
                    ShareData.good_actor.thing = ShareData.good_actor.thing_list[ShareData.good_actor.thing_index]
                    del self[i]
