import pygame


def colliderects(rect: pygame.rect.Rect, rect_list):
    result = False
    for r in rect_list:
        result = result or rect.colliderect(r)
    return result
