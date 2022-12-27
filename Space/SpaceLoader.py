from Block.CornerBlock import *
from Block.DoorBlock import *
from Space.RoomSpace import *
from Space.WidthCrossSpace import *
from Space.GroupSpace import *


def room_loader(file: str, input_x=0, input_y=0):
    room = Room()

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


def width_cross_loader(file: str, input_x=0, input_y=0):
    width_cross = WidthCross()

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


def group_loader(file: str, input_x=0, input_y=0):
    world = World()

    x = input_x
    y = input_y
    move = False
    with open(file, 'r', encoding='utf-8') as f:
        data = eval(f.read())
        is_room = True
        for d in data:
            if is_room:
                room = room_loader(d, x, y)

                if move:
                    door_block_y = room.door_block_list[0].y
                    for block in room.mix():
                        block.y += y-door_block_y + 40

                world.area_list.append(room)
                x = room.door_block_list[0].right
                y = room.door_block_list[0].top - Value.BLOCK_SIZE
            else:
                width_cross = width_cross_loader(d, x, y)
                world.area_list.append(width_cross)
                x = width_cross.corner_block_list[1].right
                print(x)

            is_room = not is_room
            move = True

    return world
