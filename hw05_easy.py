# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
try:
    for n in range(1, 10):
        os.mkdir("dir_" + str(n))
except:
    print("Directory already exist")

import os
try:
    for n in range(1, 10):
        os.rmdir("dir_" + str(n))
except:
    print("Directory not exist")



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dir = os.listdir()
#print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

name = __file__
shutil.copyfile(name, "copy_of_file")


# Функции для hw05_normal

def newdir(name):
    path = os.path.join(name)
    try:
        os.mkdir(path)
        print("Create directory", name)
    except:
        print("Directory already exist")

def deldir(name):
    path = os.path.join(name)
    try:
        os.rmdir(path)
        print("Remove directory", name)
    except:
        print("Directory not exist")

def lsdir(name):
    path = os.path.join(name)
    try:
        print(os.listdir(path))
    except:
        print("Directory not exist")


