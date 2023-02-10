from Actor.BaseActor import *
from InfoBar.BloodInfoBar import *
from InfoBar.MoneyInfoBar import MoneyInfoBar
from InfoBar.ProtectionInfoBar import *
from InfoBar.EnergyInfoBar import *
from Data.AllData import *
from Speak.BaseSpeak import BaseSpeak
from Thing.HandGunThing import *
from Thing.GunThing import *
from Treasure import BaseTreasure
from Compute.BlockCompute import *
from InfoBar.SkillInfoBar import *


class GoodActor(BaseActor):
    def __init__(self):
        super().__init__(GameData.WINDOW_WIDTH / 2 - 25, GameData.WINDOW_HEIGHT / 2 - 35,
                         *ActorData.SIZE_TUPLE)
        self.skill_image = pygame.image.load('./Res/Picture/image/good_actor/skill.png').convert_alpha()
        self.normal_image = pygame.image.load('./Res/Picture/image/good_actor/good_actor.png').convert_alpha()
        self.right_image = self.normal_image
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image

        self.blood_max = 5
        self.protection_max = 5
        self.energy_max = 180

        self.skill_last_max = 600
        self.skill_add = 0.5
        self.is_skill = False

        self.blood_info_bar = BloodInfoBar(self.blood_max)
        self.protection_info_bar = ProtectionInfoBar(self.protection_max)
        self.energy_info_bar = EnergyInfoBar(self.energy_max)
        self.skill_info_bar = SkillInfoBar(self.skill_last_max)
        self.money_info_bar = MoneyInfoBar(0)

        self.add_protection_WAIT = 60
        self.add_protection_wait = 0

        self.thing_list = [HandGunThing(self.centerx, self.centery + 10)]
        self.thing_index = 0
        self.thing = self.thing_list[self.thing_index]

        self.drop_thing_WAIT = 60
        self.drop_thing_wait = 0

        self.speak = BaseSpeak(self)

        self.is_block_by_the_block = True

    def draw(self):
        GameData.surface.blit(self.image, self)
        self.blood_info_bar.draw()
        self.protection_info_bar.draw()
        self.energy_info_bar.draw()
        self.skill_info_bar.draw()
        self.money_info_bar.draw()
        self.speak.draw()
        super().draw()
        for thing in self.thing_list:
            thing.draw_egg()

    def process(self):
        if self.is_alive():
            if EventData.is_left_mouse_down:
                self.speak.begin_say('hello',120)
                self.thing.fire(EventData.mouse_x, EventData.mouse_y, SpecialData.GOOD_ACTOR)
            if EventData.is_key_e_down or EventData.is_middle_mouse_down:
                self.is_skill = True
            self.skill()

            for thing in self.thing_list:
                thing.process()

            self.thing.rotate(EventData.mouse_x, EventData.mouse_y)
            self.blood_info_bar.process()
            self.protection_info_bar.process()
            self.energy_info_bar.process()
            self.skill_info_bar.process()
            self.money_info_bar.process()
            self.speak.process()

            self.add_protection()
            self.drop_thing()

            if EventData.is_move_left:
                self.image = self.left_image
            if EventData.is_move_right:
                self.image = self.right_image
        else:
            ShareData.game.is_game_running = False

    def drop_thing(self):
        if self.drop_thing_wait == 0:
            if EventData.is_key_q_down:
                if len(self.thing_list) > 1:
                    ShareData.drop_thing_group.append(self.thing)
                    del self.thing_list[self.thing_index]
                    self.thing_index_next()
                self.drop_thing_wait = self.drop_thing_WAIT
        else:
            self.drop_thing_wait -= 1

    def is_alive(self):
        return self.blood_info_bar.value > 0

    def get_hurt(self, hurt):
        if self.protection_info_bar.value != 0:
            if self.protection_info_bar.value >= hurt:
                self.protection_info_bar.value -= hurt
            else:
                self.protection_info_bar.value = 0
        else:
            self.blood_info_bar.value -= hurt

    def add_energy(self, value):
        if self.energy_info_bar.value + value > self.energy_max:
            self.energy_info_bar.value = self.energy_max
        else:
            self.energy_info_bar.value += value

    def add_protection(self):
        if self.add_protection_wait == 0:
            if self.protection_info_bar.value + 1 > self.protection_max:
                self.protection_info_bar.value = self.protection_max
            else:
                self.protection_info_bar.value += 1
            self.add_protection_wait = self.add_protection_WAIT
        else:
            self.add_protection_wait -= 1

    def thing_index_after(self):
        if self.thing_index == 0:
            self.thing_index = len(self.thing_list) - 1
        else:
            self.thing_index -= 1
        self.thing = self.thing_list[self.thing_index]
        self.speak.begin_say(self.thing.name+'aaa',60)

    def thing_index_next(self):
        if self.thing_index >= len(self.thing_list) - 1:
            self.thing_index = 0
        else:
            self.thing_index += 1
        self.thing = self.thing_list[self.thing_index]
        self.speak.begin_say(self.thing.ame+'aaa', 60)

    def skill(self):
        if self.is_skill:
            if self.skill_info_bar.value > 0:
                self.right_image = self.skill_image
                self.left_image = pygame.transform.flip(self.right_image, True, False)
                self.image = self.right_image
                self.is_block_by_the_block = False
                self.skill_info_bar.value -= 1
            else:
                self.is_skill = False
                self.right_image = self.normal_image
                self.left_image = pygame.transform.flip(self.right_image, True, False)
                self.image = self.right_image
                self.is_block_by_the_block = True
        else:
            if self.skill_info_bar.value + self.skill_add > self.skill_last_max:
                self.skill_info_bar.value = self.skill_last_max
            else:
                self.skill_info_bar.value += self.skill_add
