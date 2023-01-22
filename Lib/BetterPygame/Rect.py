import pygame


def colliderect_top(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect1.bottom>rect2.bottom > rect1.top
    return False


def colliderect_bottom(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect1.top<rect2.top < rect1.bottom
    return False


def colliderect_left(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect1.right>rect2.right > rect1.left
    return False


def colliderect_right(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    if rect1.colliderect(rect2):
        return rect1.left<rect2.left < rect1.right
    return False