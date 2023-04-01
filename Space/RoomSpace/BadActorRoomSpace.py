from Actor.TreasureActor.EnergyTreasureActor import EnergyTreasureActor
from Space.RoomSpace.BaseRoomSpace import *


class BadActorRoomSpace(BaseRoomSpace):
    def __init__(self, name):
        super().__init__(name)

        self.blocking_block_list: List[BlockingBlock] = []
        self.box_block_list: List[BoxBlock] = []

        self.is_door_need_close = False
        self.is_end = False
        self.is_give_treasure = False
        self.treasure = None
        self.bad_actor_number = 0

    def mix(self):
        return super().mix() + self.blocking_block_list + self.box_block_list

    def process(self):
        super().process()
        self.delete_box_block()
        for door in self.top_door_block_list + self.bottom_door_block_list \
                    + self.left_door_block_list + self.right_door_block_list:
            door.open_or_close(self.is_door_open)

        if self.is_give_treasure:
            if self.treasure is None:
                if self.is_end:
                    self.treasure = self.create_energy_treasure()
            else:
                self.treasure.process()

    def create_energy_treasure(self):
        x = self.corner_block_list[0].right + 100
        y = self.corner_block_list[0].bottom + 100
        return EnergyTreasureActor(x, y, 100, 50)

    def draw(self):
        for block in self.mix():
            block.draw()
        if self.treasure is not None:
            self.treasure.draw()

    def can_move_up(self):
        if self.is_hit_blocking_or_box_block_top():
            return super().can_move_up()
        else:
            return False

    def can_move_down(self):
        if self.is_hit_blocking_or_box_block_bottom():
            return super().can_move_down()
        else:
            return False

    def can_move_left(self):
        if self.is_hit_blocking_or_box_block_left():
            return super().can_move_left()
        else:
            return False

    def can_move_right(self):
        if self.is_hit_blocking_or_box_block_right():
            return super().can_move_right()
        else:
            return False

    def move_up(self):
        # if self.can_move_up(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, ActorData.MOVE_SPEED)

    def move_down(self):
        # if self.can_move_down(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(0, -ActorData.MOVE_SPEED)

    def move_left(self):
        # if self.can_move_left(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(ActorData.MOVE_SPEED, 0)

    def move_right(self):
        # if self.can_move_right(ShareData.good_actor):
        for block in self.mix():
            block.move_ip(-ActorData.MOVE_SPEED, 0)

    def is_in_this_space(self):
        if super().is_in_this_space():
            if self.is_door_need_close:
                self.is_door_open = False
                self.is_door_need_close = False
            return True
        else:
            return False

    def is_hit_blocking_or_box_block_top(self):
        if ShareData.good_actor.is_block_by_the_block:
            for block in self.blocking_block_list + self.box_block_list:
                if colliderect_bottom(ShareData.good_actor, block):
                    return False
            else:
                return True
        else:
            return True

    def is_hit_blocking_or_box_block_bottom(self):
        if ShareData.good_actor.is_block_by_the_block:
            for block in self.blocking_block_list + self.box_block_list:
                if colliderect_top(ShareData.good_actor, block):
                    return False
            else:
                return True
        else:
            return True

    def is_hit_blocking_or_box_block_left(self):
        if ShareData.good_actor.is_block_by_the_block:
            for block in self.blocking_block_list + self.box_block_list:
                if colliderect_right(ShareData.good_actor, block):
                    return False
            else:
                return True
        else:
            return True

    def is_hit_blocking_or_box_block_right(self):
        if ShareData.good_actor.is_block_by_the_block:
            for block in self.blocking_block_list + self.box_block_list:
                if colliderect_left(ShareData.good_actor, block):
                    return False
            else:
                return True
        else:
            return True

    def delete_box_block(self):
        for i in range(len(self.box_block_list)):
            box_block = self.box_block_list[i]
            if box_block.is_should_delete():
                self.give_coin(self.box_block_list[i])
                self.base_block_list.append(GroundBlock(box_block.left, box_block.top))
                del self.box_block_list[i]
                break

    def give_coin(self, box_block):
        if not box_block.is_coin_given:
            ShareData.coin_group.append(EnergyCoin(box_block.centerx, box_block.centery))
            # ShareData.coin_group.append(MoneyCoin(self.left, self.top))
            box_block.is_coin_given = True
