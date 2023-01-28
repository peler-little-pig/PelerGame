import pygame
from Data.AllData import *


def follow_move(rect: pygame.rect.Rect):
    if EventData.is_move_up:
        rect.move_ip(0, ActorData.MOVE_SPEED)
    if EventData.is_move_down:
        rect.move_ip(0, -ActorData.MOVE_SPEED)
    if EventData.is_move_left:
        rect.move_ip(ActorData.MOVE_SPEED, 0)
    if EventData.is_move_right:
        rect.move_ip(-ActorData.MOVE_SPEED, 0)