from Coin.EnergyCoin import EnergyCoin
from Compute.MoveCompute import *
from Treasure.BaseTreasure import *


class EnergyTreasure(BaseTreasure):
    def __init__(self, centerx, centery, width: float, height: float):
        super().__init__(centerx, centery, width, height)
        self.close_image = pygame.image.load('./Res/Picture/image/treasure/close.png').convert()
        self.open_image = pygame.image.load('./Res/Picture/image/treasure/open.png').convert()
        self.image = self.close_image

        self.is_open = False

    def draw(self):
        GameData.surface.blit(self.image, self)

    def process(self):
        self.open()
        follow_move(self)

    def open(self):
        if not self.is_open:
            if self.colliderect(ShareData.good_actor):
                if EventData.is_right_mouse_down:
                    self.image = self.open_image
                    for i in range(10):
                        ShareData.coin_group.append(EnergyCoin(self.left,self.top))
                    self.is_open = True
                    EventData.is_right_mouse_down = False
