from typing import List
from Data.AllData import *


class HireActorGroup(List):
    def __init__(self):
        super().__init__()

    def draw(self):
        for hire_actor in self:
            hire_actor.draw()

    def process(self):
        for hire_actor in self:
            hire_actor.process()
        self.hire()

    def hire(self):
        for hire_actor in self:
            if not hire_actor.is_hired:
                if hire_actor.colliderect(ShareData.good_actor):
                    if EventData.is_right_mouse_down:
                        hire_actor.hire()