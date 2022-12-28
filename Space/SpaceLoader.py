from Space.WorldSpace import *
from Value import *


def room_loader(file: str, input_x=0, input_y=0, name=''):
    room = RoomSpace(name)

    X = input_x
    x = input_x
    y = input_y
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for d in data:
            for s in d:
                if s == '!':
                    room.corner_block_list.append(CornerBlock(x, y))
                elif s == '#':
                    room.base_block_list.append(BaseBlock(x, y))
                elif s == 'T':
                    room.top_door_block_list.append(DoorBlock(x, y))
                elif s == 'B':
                    room.bottom_door_block_list.append(DoorBlock(x, y))
                elif s == 'L':
                    room.left_door_block_list.append(DoorBlock(x, y))
                elif s == 'R':
                    room.right_door_block_list.append(DoorBlock(x, y))
                x += Value.BLOCK_SIZE
            y += Value.BLOCK_SIZE
            x = X

    return room


def width_cross_loader(file: str, input_x=0, input_y=0, name=''):
    width_cross = WidthCrossSpace(name)

    X = input_x
    x = input_x
    y = input_y
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for d in data:
            for s in d:
                if s == '!':
                    width_cross.corner_block_list.append(CornerBlock(x, y))
                elif s == '#':
                    width_cross.base_block_list.append(BaseBlock(x, y))
                x += Value.BLOCK_SIZE
            y += Value.BLOCK_SIZE
            x = X

    return width_cross


def height_cross_loader(file: str, input_x=0, input_y=0, name=''):
    height_cross = HeightCrossSpace(name)

    X = input_x
    x = input_x
    y = input_y
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for d in data:
            for s in d:
                if s == '!':
                    height_cross.corner_block_list.append(CornerBlock(x, y))
                elif s == '#':
                    height_cross.base_block_list.append(BaseBlock(x, y))
                x += Value.BLOCK_SIZE
            y += Value.BLOCK_SIZE
            x = X

    return height_cross


def world_loader(file: str, input_x=0, input_y=0, name=''):
    world = WorldSpace(name)

    with open(file, 'r', encoding='utf-8') as f:
        data: tuple = eval(f.read())
        for _d in data:
            d = _d[0]
            info = _d[1]
            if d[-4:] == 'room':
                if info[1]:
                    width_cross_name = info[1][0]
                    state = info[1][1]
                    width_cross: WidthCrossSpace = world.search(width_cross_name)
                    if state == 'top':
                        room = room_loader(d, 0, 0, info[0])
                        x = width_cross.corner_block_list[0].left - Value.BLOCK_SIZE * 2
                        y = width_cross.corner_block_list[0].top - \
                            room.corner_block_list[0].top - room.corner_block_list[2].bottom
                        for block in room.mix():
                            block.x += x
                            block.y += y

                    elif state == 'bottom':
                        room = room_loader(d, 0, 0, info[0])
                        x = width_cross.corner_block_list[0].left - Value.BLOCK_SIZE * 2
                        y = width_cross.corner_block_list[2].bottom
                        for block in room.mix():
                            block.x += x
                            block.y += y

                    elif state == 'left':
                        room = room_loader(d, 0, 0, info[0])
                        x = width_cross.corner_block_list[0].left - \
                            room.corner_block_list[1].right - room.corner_block_list[0].left
                        y = width_cross.corner_block_list[0].top - Value.BLOCK_SIZE
                        for block in room.mix():
                            block.x += x
                            block.y += y

                    elif state == 'right':
                        room = room_loader(d, 0, 0, info[0])
                        x = width_cross.corner_block_list[1].right
                        y = width_cross.corner_block_list[1].top - room.left_door_block_list[0].top \
                            + Value.BLOCK_SIZE
                        for block in room.mix():
                            block.x += x
                            block.y += y
                else:
                    room = room_loader(d, input_x, input_y, info[0])
                world.area_list.append(room)

            if d[-5:] == 'cross':
                if info[1]:
                    room_name = info[1][0]
                    state = info[1][1]
                    room: RoomSpace = world.search(room_name)
                    if state == 'top':
                        height_cross = height_cross_loader(d, 0, 0, info[0])
                        x = room.top_door_block_list[0].left - Value.BLOCK_SIZE
                        y = room.top_door_block_list[0].top - \
                            height_cross.corner_block_list[0].top - height_cross.corner_block_list[2].bottom
                        for block in height_cross.mix():
                            block.x += x
                            block.y += y
                        world.area_list.append(height_cross)

                    elif state == 'bottom':
                        x = room.bottom_door_block_list[0].left - Value.BLOCK_SIZE
                        y = room.bottom_door_block_list[0].bottom
                        height_cross = height_cross_loader(d, x, y, info[0])
                        world.area_list.append(height_cross)

                    elif state == 'left':
                        width_cross = width_cross_loader(d, 0, 0, info[0])
                        x = room.left_door_block_list[0].left - \
                            width_cross.corner_block_list[1].right - width_cross.corner_block_list[0].left
                        y = room.left_door_block_list[0].top - Value.BLOCK_SIZE
                        for block in width_cross.mix():
                            block.x += x
                            block.y += y
                        world.area_list.append(width_cross)

                    elif state == 'right':
                        x = room.right_door_block_list[0].right
                        y = room.right_door_block_list[0].top - Value.BLOCK_SIZE
                        width_cross = width_cross_loader(d, x, y, info[0])
                        world.area_list.append(width_cross)

    return world
