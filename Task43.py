# """Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках. """
# Ввод: 
# 5 
# 1 2 3 4 5 
# Вывод: 
# 0 
# Ввод:
# 5 
# 1 5 1 5 1
# Вывод:
# 2


def number_list(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите число: ')))
    return list_1


def count_pair(list_1: list):
    sum_count = 0
    for i in set(list_1):
        sum_count += list_1.count(i) // 2
    return sum_count


list_2 = (number_list(int(input('Введите количество чисел: '))))
print(list_2)
print(count_pair(list_2))
