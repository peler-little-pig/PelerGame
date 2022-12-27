from Actor.GoodActor import *


class Space(object):
    def __init__(self):
        super().__init__()

    def mix(self):
        ...

    def draw(self):
        ...

    def move_up(self, good_actor: GoodActor):
        ...

    def move_down(self, good_actor: GoodActor):
        ...

    def move_left(self, good_actor: GoodActor):
        ...

    def move_right(self, good_actor: GoodActor):
        ...
