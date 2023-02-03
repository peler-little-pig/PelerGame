from Group.DropThingGroup import DropThingGroup
from Group.MapGroup import MapGroup
from MapLoader.SpaceLoader import *
from MapLoader.BadActorLoader import *
import os


def map_loader():
    folders = os.listdir('./Res/Map')
    maps = MapGroup()
    for f in folders:
        world = world_loader(f'./Res/Map/{f}/{f}.pworld')
        maps.append(world, bad_actor_group_loader(world), DropThingGroup())
    return maps
