# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
from hw05_easy import newdir
from hw05_easy import deldir
from hw05_easy import lsdir

print(" ")
print(" [1] - Change directory")
print(" [2] - List files in directory")
print(" [3] - Remove directory")
print(" [4] - Create directory")
print(" ")
do = int(input("Input number of action: "))

if do == 1:
    dirname = input('Input path to directory:')
    os.chdir(dirname)

    try:
        cwd = os.getcwd()
        print('Change directory to ', cwd)
    except(FileNotFoundError, OSError):
        print('Wrong path: ', ui_dir)

elif do == 2:
    dirname = input('Input path to directory:')
    lsdir(dirname)

elif do == 3:
    dirname = input('Input path to directory:')
    deldir(dirname)

elif do == 4:
    dirname = input('Input path to directory:')
    newdir(dirname)


    