import pygame


def colliderect_top(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect2.top + 3 >= rect1.bottom >= rect2.top
    return False


def colliderect_bottom(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect2.bottom - 3 <= rect1.top <= rect2.bottom
    return False


def colliderect_left(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect2.left + 3 >= rect1.right >= rect2.left
    return False


def colliderect_right(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect2.right <= rect1.left <= rect2.right
    return False
