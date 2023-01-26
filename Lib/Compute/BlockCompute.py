from Space.RoomSpace import RoomSpace
import pygame


def is_hit_blocking_block(rect: pygame.rect.Rect, area):
    if type(area) == RoomSpace:
        for block in area.blocking_block_list:
            if rect.colliderect(block):
                return True
    return False


def is_hit_box_block(rect: pygame.rect.Rect, area):
    if type(area) == RoomSpace:
        for block in area.box_block_list:
            if rect.colliderect(block):
                return True
    return False
