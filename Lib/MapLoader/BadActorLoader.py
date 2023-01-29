from Lib.Creator.BadActorCreator import *


def room_reader(world):
    info = []
    for area in world.area_list:
        if type(area) == RoomSpace:
            info.append(area)
    return info


def bad_actor_group_loader(world):
    bad_actor_group = BadActorGroup()
    room_list = room_reader(world)
    for room in room_list:
        bad_actor_group.group[room] = []
        create_bad_actor(bad_actor_group.group[room], room)
    return bad_actor_group
