from typing import List


class MapGroup(List):
    def __init__(self):
        super().__init__()
        self.i = 0

    def world(self):
        return self[self.i][0]

    def bad_actor_group(self):
        return self[self.i][1]

    def drop_thing_group(self):
        return self[self.i][2]

    def next(self):
        self.i += 1

    def append(self, world, bad_actor_group, drop_thing_group) -> None:
        super().append([world, bad_actor_group, drop_thing_group])
