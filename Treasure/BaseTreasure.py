from Compute.MoveCompute import *
from Compute.PositionCompute import *


class BaseTreasure(pygame.rect.Rect):
    def __init__(self, centerx, centery, width: float, height: float):
        super().__init__(0, 0, width, height)
        self.centerx = centerx
        self.centery = centery
        self.close_image = pygame.image.load('./Res/Picture/image/treasure/close.png').convert()
        self.open_image = pygame.image.load('./Res/Picture/image/treasure/open.png').convert()
        self.image = self.close_image

        self.is_open = False

    def draw(self):
        GameData.surface.blit(self.image, self)

    def process(self):
        follow_move(self)
        self.open()

    def open(self):
        if not self.is_open:
            if self.colliderect(ShareData.good_actor):
                if EventData.is_right_mouse_down:
                    self.image = self.open_image
                    # x,y = middle(self,)
                    ShareData.drop_thing_group.append_random(self.center)
                    self.is_open = True
                    EventData.is_right_mouse_down = False
