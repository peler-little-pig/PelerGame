import math


def get_degree(x1, y1, x2, y2):
    dir = (x2 - x1, y2 - y1)
    length = math.hypot(*dir)
    if length == 0.0:
        dir = (0, -1)
    else:
        dir = (dir[0] / length, dir[1] / length)
    return math.degrees(math.atan2(-dir[1], dir[0])),dir
