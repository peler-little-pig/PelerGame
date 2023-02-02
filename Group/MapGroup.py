from typing import List


class MapGroup(List):
    def __init__(self):
        super().__init__()
        self.i = 0

    def get_world(self):
        return self[self.i][0]

    def get_bad_actor_group(self):
        return self[self.i][1]

    def next(self):
        self.i += 1