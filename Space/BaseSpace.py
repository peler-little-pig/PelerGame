import pygame


class BaseSpace(object):
    def __init__(self, name):
        super().__init__()
        self.name:str = name

    def mix(self, **kwargs) -> list:
        ...

    def process(self, **kwargs):
        for block in self.mix():
            block.process()

    def draw(self, **kwargs):
        ...

    def can_move_up(self):
        ...

    def can_move_down(self):
        ...

    def can_move_left(self):
        ...

    def can_move_right(self):
        ...

    def move_up(self):
        ...

    def move_down(self):
        ...

    def move_left(self):
        ...

    def move_right(self):
        ...

    def is_in_this_space(self):
        ...
