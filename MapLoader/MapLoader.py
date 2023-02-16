from Group.DropThingGroup import DropThingGroup
from Group.MapGroup import MapGroup
from Group.SellActorGroup import SellActorGroup
from MapLoader.SpaceLoader import *
from MapLoader.BadActorLoader import *
import os


def map_loader():
    folders = os.listdir('./Res/Map')
    maps = MapGroup()
    for f in folders:
        world = world_loader(f'./Res/Map/{f}/{f}.pworld')
        bad_actor_group = bad_actor_group_loader(world)
        drop_thing_group = DropThingGroup()
        sell_actor_group = SellActorGroup()
        maps.append(world, bad_actor_group, drop_thing_group,sell_actor_group)
        for area in world.area_list:
            area.init(sell_actor_group)
    return maps
