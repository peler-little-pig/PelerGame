from typing import List
from Egg.BaseEgg import *
from Value import *


class BaseThing(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.egg_list: List[BaseEgg] = []
        self.WAIT = 5
        self.wait = 0

    def fire(self, degree):
        if self.wait == 0:
            egg = BaseEgg(degree,self.left, self.top, self.width - 30, self.height)
            self.egg_list.append(egg)
            self.wait = self.WAIT
        else:
            self.wait -= 1

    def draw(self):
        pygame.draw.rect(Value.surface, (255, 255, 255), self)
        for egg in self.egg_list:
            egg.draw()

    def rotate(self):
        pass

    def process(self):
        if Value.is_mouse_down:
            x_different = Value.mouse_down_x - self.x
            y_different = self.y - Value.mouse_down_y
            self.fire((x_different,y_different))
        for egg in self.egg_list:
            egg.process()
