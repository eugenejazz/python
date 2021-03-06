# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, 2, 4, 0]
list2 = [a ** 2 for a in list1]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
other_fruits = ['pinapple', 'cherry', 'melon']
new_list = list(set(fruits + other_fruits))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers = [237, 6, 4.234, -101, 9, -67, 8, 16]
result = [ i for i in numbers if i % 3 == 0 and i >=0 and i % 4 !=0]