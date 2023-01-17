from Thing.BaseThing import *


class BaseActor(pygame.rect.Rect):
    def __init__(self, left: float, top: float, width: float, height: float) -> None:
        super().__init__(left, top, width, height)
        self.thing = BaseThing(self.x + 25, self.y + 35, 50, 30)

    def draw(self):
        self.thing.draw()

    def process(self):
        self.thing.process()
