# coding: utf8

__author__ = 'Никифоров Евгений Алексеевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'kiwi', 'watermelon']

number = 0

for i in range(1,len(fruits)):
    if len(fruits[number]) < len(fruits[i]):
        number = i

length = len(fruits[number])

for num, fruit in enumerate(fruits):
	print (str(num) + ".", '{:>{length}}'.format(fruit,length = length))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
food = ['apple', 'cherry', 'kiwi', 'tomato']

for fruit in fruits:
	for foo in food:
		if fruit == foo:
			fruits.remove(foo)
			break

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_one = [6, 4, 1, 24, 41, 237, 200]
list_two = []
for i in range(len(list_one)):
    if list_one[i] % 2 == 0:
        list_two.append(list_one[i] / 4)
    else:
        list_two.append(list_one[i] * 2)
