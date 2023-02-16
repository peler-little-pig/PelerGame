import random
import shutil
import os
from Data.SpaceData import SpaceData as data

map_path = './Res/Map'
map_index = '00'
file_name_int = 0


def home(door):
    global file_name_int
    with open('./Res/MapModel/special/home.proom', 'r', encoding='utf-8') as f:
        text = f.readlines()
    if door == data.TOP:
        text[0] = text[0].replace('D', 'T')
    elif door == data.BOTTOM:
        text[-1] = text[-1].replace('D', 'B')
    elif door == data.RIGHT:
        for i in range(len(text)):
            if text[i][-2] == 'D':
                text[i] = text[i][:-2] + 'R\n'
    for i in range(len(text)):
        text[i] = text[i].replace('D', '#')
    file_path = f'{map_path}/{map_index}/{file_name_int}.proom'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def next(door):
    global file_name_int
    with open('./Res/MapModel/special/next.proom', 'r', encoding='utf-8') as f:
        text = f.readlines()
    if door == data.TOP:
        text[0] = text[0].replace('D', 'T')
    elif door == data.BOTTOM:
        text[-1] = text[-1].replace('D', 'B')
    elif door == data.RIGHT:
        for i in range(len(text)):
            if text[i][-2] == 'D':
                text[i] = text[i][:-2] + 'R\n'
    elif door == data.LEFT:
        for i in range(len(text)):
            if text[i][0] == 'D':
                text[i] = 'L' + text[i][1:]
    for i in range(len(text)):
        text[i] = text[i].replace('D', '#')
    file_path = f'{map_path}/{map_index}/{file_name_int}.proom'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def treasure(door):
    global file_name_int
    with open('./Res/MapModel/special/treasure.proom', 'r', encoding='utf-8') as f:
        text = f.readlines()
    if door == data.TOP:
        text[0] = text[0].replace('D', 'T')
    elif door == data.BOTTOM:
        text[-1] = text[-1].replace('D', 'B')
    elif door == data.RIGHT:
        for i in range(len(text)):
            if text[i][-2] == 'D':
                text[i] = text[i][:-2] + 'R\n'
    elif door == data.LEFT:
        for i in range(len(text)):
            if text[i][0] == 'D':
                text[i] = 'L' + text[i][1:]
    for i in range(len(text)):
        text[i] = text[i].replace('D', '#')
    file_path = f'{map_path}/{map_index}/{file_name_int}.ptreasureroom'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def sell(door):
    global file_name_int
    with open('./Res/MapModel/special/sell.proom', 'r', encoding='utf-8') as f:
        text = f.readlines()
    if door == data.TOP:
        text[0] = text[0].replace('D', 'T')
    elif door == data.BOTTOM:
        text[-1] = text[-1].replace('D', 'B')
    elif door == data.RIGHT:
        for i in range(len(text)):
            if text[i][-2] == 'D':
                text[i] = text[i][:-2] + 'R\n'
    elif door == data.LEFT:
        for i in range(len(text)):
            if text[i][0] == 'D':
                text[i] = 'L' + text[i][1:]
    for i in range(len(text)):
        text[i] = text[i].replace('D', '#')
    file_path = f'{map_path}/{map_index}/{file_name_int}.psellroom'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def cross(type):
    global file_name_int
    file = ''
    if type == data.WIDTH_CROSS:
        file = './Res/MapModel/cross/width.pwidthcross'
    elif type == data.HEIGHT_CROSS:
        file = './Res/MapModel/cross/height.pheightcross'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()
    file_path = f'{map_path}/{map_index}/{file_name_int}.p{type}cross'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def room(*args):
    global file_name_int
    file = random.choice(os.listdir('./Res/MapModel/room'))
    with open(f'./Res/MapModel/room/{file}', 'r', encoding='utf-8') as f:
        text = f.readlines()
    for door in args:
        if door == data.TOP:
            text[0] = text[0].replace('D', 'T')
        elif door == data.BOTTOM:
            text[-1] = text[-1].replace('D', 'B')
        elif door == data.RIGHT:
            for i in range(len(text)):
                if text[i][-2] == 'D':
                    text[i] = text[i][:-2] + 'R\n'
        elif door == data.LEFT:
            for i in range(len(text)):
                if text[i][0] == 'D':
                    text[i] = 'L' + text[i][1:]
    for i in range(len(text)):
        text[i] = text[i].replace('D', '#')
    file_path = f'{map_path}/{map_index}/{file_name_int}.proom'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def info(index):
    global file_name_int
    file = f'./Res/MapModel/info/{index}.pinfo'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()
    file_path = f'{map_path}/{map_index}/{file_name_int}.pinfo'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(text)
    file_name_int += 1
    return file_path


def world(file):
    global file_name_int
    with open(file, 'r', encoding='utf-8') as f:
        content = eval(f.read())
    for i in range(len(content)):
        content[i][0] = eval(content[i][0])
    file_path = f'{map_path}/{map_index}/{map_index}.pworld'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(str(content))


def map(number):
    global map_index
    for i in range(number):
        file = random.choice(os.listdir('./Res/MapModel/world'))
        os.mkdir(f'{map_path}/{map_index}')
        world(f'./Res/MapModel/world/{file}')
        map_index = '0' + str(int(map_index) + 1) if int(map_index) < 10 else str(int(map_index) + 1)


def clean():
    dirs = os.listdir('./Res/Map')
    for dir in dirs:
        shutil.rmtree(f'./Res/Map/{dir}')
