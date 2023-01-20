from Space.RoomSpace import RoomSpace
from Space.WidthCrossSpace import *
from Space.HeightCrossSpace import *
import pygame
from Data.AllData import *


def is_hit_wall(rect: pygame.rect.Rect):
    area = active_area(rect)
    if type(area) == RoomSpace:
        return (rect.top < area.corner_block_list[0].bottom
                or rect.bottom > area.corner_block_list[2].top
                or rect.left < area.corner_block_list[0].right
                or rect.right > area.corner_block_list[1].left)
    elif type(area) == WidthCrossSpace:
        return (rect.top < area.corner_block_list[0].bottom
                or rect.bottom > area.corner_block_list[2].top
                or rect.left < area.corner_block_list[0].left
                or rect.right > area.corner_block_list[1].right)
    elif type(area) == HeightCrossSpace:
        return (rect.top < area.corner_block_list[0].top
                or rect.bottom > area.corner_block_list[2].bottom
                or rect.left < area.corner_block_list[0].right
                or rect.right > area.corner_block_list[1].left)


def active_area(rect: pygame.rect.Rect):
    for area in ShareData.world.area_list:
        if type(area) == RoomSpace:
            if not (rect.top < area.corner_block_list[0].top
                    or rect.bottom > area.corner_block_list[2].bottom
                    or rect.left < area.corner_block_list[0].left
                    or rect.right > area.corner_block_list[1].right):
                return area
        elif type(area) == WidthCrossSpace:
            if not (rect.top < area.corner_block_list[0].top
                    or rect.bottom > area.corner_block_list[2].bottom
                    or rect.left < area.corner_block_list[0].left -
                    ConstData.NORMAL_ACTOR_SIZE_TUPLE[0]
                    or rect.right > area.corner_block_list[1].right +
                    ConstData.NORMAL_ACTOR_SIZE_TUPLE[
                        0]):
                return area
        elif type(area) == HeightCrossSpace:
            if not (rect.top < area.corner_block_list[0].top - ConstData.NORMAL_ACTOR_SIZE_TUPLE[1]
                    or rect.bottom > area.corner_block_list[2].bottom +
                    ConstData.NORMAL_ACTOR_SIZE_TUPLE[1]
                    or rect.left < area.corner_block_list[0].left
                    or rect.right > area.corner_block_list[1].right):
                return area


def is_hit_blocking_block(rect: pygame.rect.Rect, area):
    if type(area) == RoomSpace:
        for block in area.blocking_block_list:
            if rect.colliderect(block):
                return True
    return False
