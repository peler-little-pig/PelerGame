from Actor.GoodActor import *


class Space(object):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def mix(self):
        ...

    def draw(self):
        ...

    def can_move_up(self, good_actor: GoodActor):
        ...

    def can_move_down(self, good_actor: GoodActor):
        ...

    def can_move_left(self, good_actor: GoodActor):
        ...

    def can_move_right(self, good_actor: GoodActor):
        ...

    def move_up(self, good_actor: GoodActor):
        ...

    def move_down(self, good_actor: GoodActor):
        ...

    def move_left(self, good_actor: GoodActor):
        ...

    def move_right(self, good_actor: GoodActor):
        ...

    def is_in_this_space(self, good_actor: GoodActor):
        ...