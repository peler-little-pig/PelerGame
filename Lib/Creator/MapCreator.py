import random
import os
import shutil


def choose(path):
    files = os.listdir(path)
    return path + '/' + random.choice(files)


def space_create(world_path, path, name):
    file_list = []
    with open(world_path, 'r', encoding='utf-8') as f:
        data = eval(f.read())
    for i in range(len(data)):
        data[i][0] = eval(data[i][0])
        file_list.append(data[i][0])
    with open(f'{path}/{name}.pworld', 'w', encoding='utf-8') as f:
        f.write(str(data))
    for file in file_list:
        shutil.copy(file, path)


def map_create(world_path, path, count):
    for i in range(count):
        name = '0' + str(i) if i < 10 else str(i)
        os.mkdir(path + '/' + name)
        space_create(world_path + '/' + random.choice(os.listdir(world_path)),
                     path + '/' + name,
                     name)

def clean(path):
    for dir in os.listdir(path):
        shutil.rmtree(path+'/'+dir)