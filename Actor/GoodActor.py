from Actor.BaseActor import *
from InfoBar.BloodInfoBar import *
from InfoBar.ProtectionInfoBar import *
from InfoBar.EnergyInfoBar import *
from Data.AllData import *

class GoodActor(BaseActor):
    def __init__(self):
        super().__init__(ConstData.WINDOW_WIDTH / 2 - 25, ConstData.WINDOW_HEIGHT / 2 - 35,
                         *ConstData.NORMAL_ACTOR_SIZE_TUPLE)
        self.right_image = pygame.image.load('./Res/image/good_actor/good_actor.png').convert_alpha()
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image

        self.blood_info_bar = BloodInfoBar(5)
        self.protection_info_bar = ProtectionInfoBar(5)
        self.energy_info_bar = EnergyInfoBar(300)

        ShareData.blood_info_bar = self.blood_info_bar
        ShareData.protection_info_bar = self.protection_info_bar
        ShareData.energy_info_bar = self.energy_info_bar

    def draw(self):
        ConstData.surface.blit(self.image, self)
        self.blood_info_bar.draw()
        self.protection_info_bar.draw()
        self.energy_info_bar.draw()
        super().draw()

    def process(self):
        if EventData.is_mouse_down:
            if self.energy_info_bar.value > 0:
                self.thing.fire()

        super().process()
        self.thing.rotate()
        self.blood_info_bar.process()
        self.protection_info_bar.process()
        self.energy_info_bar.process()

        if EventData.is_move_left:
            self.image = self.left_image
        if EventData.is_move_right:
            self.image = self.right_image
