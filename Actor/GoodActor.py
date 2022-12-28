from Actor.BaseActor import *


class GoodActor(BaseActor):
    def __init__(self):
        super().__init__(Value.WINDOW_WIDTH / 2 - 25, Value.WINDOW_HEIGHT / 2 - 35, *Value.NORMAL_ACTOR_SIZE_TUPLE)
