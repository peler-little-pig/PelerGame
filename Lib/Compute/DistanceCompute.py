def is_close(rect1, rect2, distance):
    return abs(rect1.centerx - rect2.centerx) <= distance and \
           abs(rect1.centery - rect2.centery) <= distance
