from Lib.MapLoader.SpaceLoader import *
from Lib.MapLoader.BadActorLoader import *
import os


def map_loader():
    folders = os.listdir('./Res/Map')
    world_list = []
    for f in folders:
        world = world_loader(f'./Res/Map/{f}/{f}.pworld')
        world_list.append([world, bad_actor_group_loader(world)])
    return world_list
