from typing import List
from Egg.BaseEgg import *
from Value import *


class BaseThing(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.egg_list: List[BaseEgg] = []

    def fire(self):
        egg = BaseEgg(self.left, self.top, self.width, self.height)
        self.egg_list.append(egg)

    def draw(self):
        pygame.draw.rect(Value.surface, (255, 255, 255), self)
        for egg in self.egg_list:
            egg.draw()
            egg.move_ip(1, 0)

    def rotate(self):
        pass
