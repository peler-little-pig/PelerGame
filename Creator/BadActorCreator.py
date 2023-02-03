from Group.BadActorGroup import *
from Actor.BadActor import *
from Data.AllData import *


def create_bad_actor(bad_actor_list: list, room: RoomSpace):
    bad_actor_number = room.bad_actor_number
    for i in range(bad_actor_number):
        x = random.randint(room.corner_block_list[0].right + 30,
                           room.corner_block_list[1].left - 30 - ActorData.SIZE_TUPLE[0])
        y = random.randint(room.corner_block_list[0].bottom + 30,
                           room.corner_block_list[2].top - 30 - ActorData.SIZE_TUPLE[1])

        bad_actor = BadActor(x, y)
        while is_hit_blocking_block(bad_actor, room) or is_hit_box_block(bad_actor, room):
            x = random.randint(room.corner_block_list[0].right + 30,
                               room.corner_block_list[1].left - 30 - ActorData.SIZE_TUPLE[0])
            y = random.randint(room.corner_block_list[0].bottom + 30,
                               room.corner_block_list[2].top - 30 - ActorData.SIZE_TUPLE[1])

            bad_actor = BadActor(x, y)

        bad_actor_list.append(BadActor(x, y))
