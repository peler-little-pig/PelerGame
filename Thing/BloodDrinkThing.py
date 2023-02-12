from Egg.NoneEgg import NoneEgg
from Thing.BaseThing import *
from Egg.GunEgg import *


class BloodDrinkThing(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(
            left=left,
            top=top,
            width=30,
            height=30,
            rotate_point=(5, 15),
            length=30,
            WAIT=0,
            image_path='./Res/Picture/image/drink/blood.png',
            cost=0,
            egg_type=NoneEgg,
            name='生命药水')

        self.is_used = False

    def fire(self, x, y, whose):
        if not self.is_used:
            self.image = pygame.image.load('./Res/Picture/image/drink/empty.png')
            self.image_rotate = self.image
            self.image_flip = pygame.transform.flip(self.image, True, False)
            ShareData.good_actor.add_blood(2.5)
            self.is_used = True
