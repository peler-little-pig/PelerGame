import math
import pygame


def rotate_at_pos(surface, pos, origin_pos, degree):
    rect = surface.get_rect(topleft=(pos[0] - origin_pos[0], pos[1] - origin_pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - rect.center
    rotate_offset = offset_center_to_pivot.rotate(-degree)
    rotate_center = (pos[0] - rotate_offset.x, pos[1] - rotate_offset.y)
    rotate_surface = pygame.transform.rotate(surface, degree)
    rotate_rect = rotate_surface.get_rect(center=rotate_center)
    return rotate_surface, rotate_rect
