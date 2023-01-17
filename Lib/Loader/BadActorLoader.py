from Space.BadActorSpace import *
from Actor.BadActor import *
from Data.AllData import *
def room_reader():
    info = []
    for area in ShareData.world.area_list:
        if type(area) == RoomSpace:
            info.append(area)
    return info


def create_bad_actor(bad_actor_list: list, room: RoomSpace):
    bad_actor_number = room.bad_actor_number
    for i in range(bad_actor_number):
        x = random.randint(room.corner_block_list[0].right + 30,
                           room.corner_block_list[1].left - 30 - ConstData.NORMAL_ACTOR_SIZE_TUPLE[0])
        y = random.randint(room.corner_block_list[0].bottom + 30,
                           room.corner_block_list[2].top - 30 - ConstData.NORMAL_ACTOR_SIZE_TUPLE[1])
        bad_actor_list.append(BadActor(x, y))


def bad_actor_group_loader():
    bad_actor_group = BadActorGroup()
    room_list = room_reader()
    for room in room_list:
        bad_actor_group.group[room] = []
        create_bad_actor(bad_actor_group.group[room], room)
    return bad_actor_group
