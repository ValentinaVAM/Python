# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint

list_1 = [randint(-20, 20) for i in range(randint(5, 15))]
print(list_1)
max_index = int(input("Введите MAX: "))
min_index = int(input("Введите MIN: "))
list_2 = []
if max_index >= min_index:
    for i in range(len(list_1)):
        if max_index >= list_1[i] and min_index <= list_1[i]:
            list_2.append(i)
print(list_2)
