from Space.RoomSpace.BadActorRoomSpace import BadActorRoomSpace
# from Space.RoomSpace.SellActorRoomSpace import SellActorRoomSpace
# from Space.RoomSpace.TreasureRoomSpace import TreasureRoomSpace
from Space.WidthCrossSpace import *
from Space.HeightCrossSpace import *
import pygame
from Data.AllData import *


def is_hit_wall(rect: pygame.rect.Rect):
    area = active_area(rect)
    if type(area) == WidthCrossSpace:
        return (rect.top < area.corner_block_list[0].bottom
                or rect.bottom > area.corner_block_list[2].top
                or rect.left < area.corner_block_list[0].left
                or rect.right > area.corner_block_list[1].right)
    elif type(area) == HeightCrossSpace:
        return (rect.top < area.corner_block_list[0].top
                or rect.bottom > area.corner_block_list[2].bottom
                or rect.left < area.corner_block_list[0].right
                or rect.right > area.corner_block_list[1].left)
    elif area is not None:
        return (rect.top < area.corner_block_list[0].bottom
                or rect.bottom > area.corner_block_list[2].top
                or rect.left < area.corner_block_list[0].right
                or rect.right > area.corner_block_list[1].left)


def active_area(rect: pygame.rect.Rect):
    for area in ShareData.world.area_list:
        if type(area) == BadActorRoomSpace:
            if not (rect.top < area.corner_block_list[0].top
                    or rect.bottom > area.corner_block_list[2].bottom
                    or rect.left < area.corner_block_list[0].left
                    or rect.right > area.corner_block_list[1].right):
                return area
        elif type(area) == WidthCrossSpace:
            if not (rect.top < area.corner_block_list[0].top
                    or rect.bottom > area.corner_block_list[2].bottom
                    or rect.left < area.corner_block_list[0].left -
                    ActorData.SIZE_TUPLE[0]
                    or rect.right > area.corner_block_list[1].right +
                    ActorData.SIZE_TUPLE[
                        0]):
                return area
        elif type(area) == HeightCrossSpace:
            if not (rect.top < area.corner_block_list[0].top - ActorData.SIZE_TUPLE[1]
                    or rect.bottom > area.corner_block_list[2].bottom +
                    ActorData.SIZE_TUPLE[1]
                    or rect.left < area.corner_block_list[0].left
                    or rect.right > area.corner_block_list[1].right):
                return area
