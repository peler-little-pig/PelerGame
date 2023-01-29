import random
from Data.SpaceData import SpaceData as data


def create_ground_block(width, height):
    return [['@'] * width for i in range(height)]


def create_wall_block(string):
    string[0] = ['#'] * len(string[0])
    string[-1] = ['#'] * len(string[-1])
    for line in string:
        line[0] = '#'
        line[-1] = '#'
    return string


def creat_corner_block(string):
    string[0][0] = '!'
    string[0][-1] = '!'
    string[-1][0] = '!'
    string[-1][-1] = '!'
    return string


def create_door(string, position):
    if position == data.TOP:
        width = random.randint(2, len(string[0]) - 8)
        for i in range(6):
            string[0][width + i] = 'T'
    elif position == data.BOTTOM:
        width = random.randint(2, len(string[-1]) - 8)
        for i in range(6):
            string[-1][width + i] = 'B'
    elif position == data.LEFT:
        height = random.randint(2, len(string) - 8)
        for i in range(6):
            string[height + i][0] = 'L'
    elif position == data.RIGHT:
        height = random.randint(2, len(string) - 8)
        for i in range(6):
            string[height + i][-1] = 'R'

    return string


def save_space(string, path):
    with open(path, 'w', encoding='utf-8') as f:
        for line in string:
            for s in line:
                f.write(s[0])
            f.write('\n')


def create_blocking_block(string):
    max_count = len(string[0]) * len(string) // 10
    count = random.randint(0, max_count)
    for i in range(count):
        x = random.randint(5, len(string[0]) - 5)
        y = random.randint(5, len(string) - 5)
        string[y][x] = '-'
    return string


def create_box_block(string):
    max_count = len(string[0]) * len(string) // 3
    count = random.randint(0, max_count)
    for i in range(count):
        x = random.randint(5, len(string[0]) - 5)
        y = random.randint(5, len(string) - 5)
        string[y][x] = '='
    return string


def create_width_cross(path):
    width = random.randint(data.CROSS_MIN, data.CROSS_MAX)
    string = create_ground_block(width, 8)
    string[0] = ['#'] * len(string[0])
    string[-1] = ['#'] * len(string[-1])
    string = creat_corner_block(string)
    save_space(string, path)


def create_height_cross(path):
    height = random.randint(data.CROSS_MIN, data.CROSS_MAX)
    string = create_ground_block(8, height)
    for i in range(len(string)):
        string[i][0] = '#'
        string[i][-1] = '#'
    string = creat_corner_block(string)
    save_space(string, path)


def create_home(path):
    width, height = random.randint(data.HOME_MIN, data.HOME_MAX), random.randint(data.HOME_MIN, data.HOME_MAX)
    door = random.choice([data.TOP, data.BOTTOM, data.LEFT, data.RIGHT])
    string = create_ground_block(width, height)
    string = create_wall_block(string)
    string = creat_corner_block(string)
    string = create_door(string, door)
    for i in range(len(string)):
        for j in range(7):
            string[i].insert(0, [' '])
    save_space(string, path)
    return door


def create_next_room(path, door):
    width, height = random.randint(data.HOME_MIN, data.HOME_MAX), random.randint(data.HOME_MIN, data.HOME_MAX)
    string = create_ground_block(width, height)
    string = create_wall_block(string)
    string = creat_corner_block(string)
    string = create_door(string, door)
    save_space(string, path)


def create_room(path, door, door_count):
    width, height = random.randint(data.ROOM_MIN, data.ROOM_MAX), random.randint(data.ROOM_MIN, data.ROOM_MAX)
    door_list = [door]
    possible = [data.TOP, data.BOTTOM, data.LEFT, data.RIGHT]
    possible.remove(door)
    for i in range(door_count - 1):
        choose = random.randint(0, len(possible) - 1)
        door_list.append(possible[choose])
        del possible[choose]

    string = create_ground_block(width, height)
    string = create_wall_block(string)
    string = creat_corner_block(string)
    # string = create_blocking_block(string)
    string = create_box_block(string)

    for door in door_list:
        string = create_door(string, door)
    save_space(string, path)
    return door_list


def create_space(path, str_index):
    # room_count = random.randint(data.ROOM_COUNT_MAX, data.ROOM_COUNT_MAX)
    room_count = 7
    index = 0
    world_list = []

    home_door = create_home(path + '/home.proom')
    world_list.append((path + '/home.proom', (str(index), ())))
    index += 1

    def room(room_num, door, i):
        door_count = 2
        room_num += 1
        if room_num < room_count:
            door_ = ''
            if door == data.TOP:
                door_ = data.BOTTOM
                create_height_cross(path + f'/{i}.pheightcross')
                world_list.append((path + f'/{i}.pheightcross', (str(i), (str(i - 1), door))))
                i += 1
            elif door == data.BOTTOM:
                door_ = data.TOP
                create_height_cross(path + f'/{i}.pheightcross')
                world_list.append((path + f'/{i}.pheightcross', (str(i), (str(i - 1), door))))
                i += 1
            elif door == data.LEFT:
                door_ = data.RIGHT
                create_width_cross(path + f'/{i}.pwidthcross')
                world_list.append((path + f'/{i}.pwidthcross', (str(i), (str(i - 1), door))))
                i += 1
            elif door == data.RIGHT:
                door_ = data.LEFT
                create_width_cross(path + f'/{i}.pwidthcross')
                world_list.append((path + f'/{i}.pwidthcross', (str(i), (str(i - 1), door))))
                i += 1

            door_list = create_room(path + f'/{i}.proom', door_, door_count)
            world_list.append((path + f'/{i}.proom', (str(i), (str(i - 1), door))))
            i += 1
            for d in door_list:
                if d != door_:
                    i = room(room_num, d, i)
            return i
        return None, None

    room(0, home_door, index)

    with open(path + f'/{str_index}.pworld', 'w', encoding='utf-8') as f:
        f.write(str(world_list))
