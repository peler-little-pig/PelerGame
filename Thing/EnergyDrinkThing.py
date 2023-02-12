from Egg.NoneEgg import NoneEgg
from Thing.BaseThing import *
from Egg.GunEgg import *


class EnergyDrinkThing(BaseThing):
    def __init__(self, left: float, top: float):
        super().__init__(
            left=left,
            top=top,
            width=30,
            height=30,
            rotate_point=(5, 15),
            length=30,
            WAIT=0,
            image_path='./Res/Picture/image/drink/energy.png',
            cost=0,
            egg_type=NoneEgg,
            name='能量药水')

        self.is_used = False

    def fire(self, x, y, whose):
        if not self.is_used:
            self.image = pygame.image.load('./Res/Picture/image/drink/empty.png')
            self.image_rotate = self.image
            self.image_flip = pygame.transform.flip(self.image, True, False)
            ShareData.good_actor.add_energy(200)
            self.is_used = True
