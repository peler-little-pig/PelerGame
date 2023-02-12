import math


def is_close(rect1, rect2, distance):
    return abs(rect1.centerx - rect2.centerx) <= distance and \
           abs(rect1.centery - rect2.centery) <= distance


def distance(rect1, rect2):
    return math.dist(rect1.center, rect2.center)
