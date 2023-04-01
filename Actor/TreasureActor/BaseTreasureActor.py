from Compute.MoveCompute import *
from Compute.PositionCompute import *


class BaseTreasureActor(pygame.rect.Rect):
    def __init__(self, centerx, centery, width: float, height: float, close_image_path, open_image_path):
        super().__init__(0, 0, width, height)
        self.centerx = centerx
        self.centery = centery
        self.close_image = pygame.image.load(close_image_path).convert()
        self.open_image = pygame.image.load(open_image_path).convert()
        self.image = self.close_image

        self.is_open = False

    def draw(self):
        GameData.surface.blit(self.image, self)

    def process(self):
        follow_move(self)
        if not self.is_open:
            if self.colliderect(ShareData.good_actor):
                if EventData.is_right_mouse_down:
                    self.open()
                    self.image = self.open_image
                    self.is_open = True
                    EventData.is_right_mouse_down = False

    def open(self):
        ...