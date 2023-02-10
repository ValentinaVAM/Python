# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
N = int(input('Введите число N: ')) 
list_A=[]
for i in range(N):
    list_A.append(randint(1, N))
if N > 0:
    print(*list_A)
    X = int(input('Введите число X: '))
    res = list_A[0]
    for i in list_A:
        if abs(i - X) < abs(res - X):
            res = i
    print(f'Самый близкий по величине элемент к числу {X} -> {res}')
else:
    print('Введите натуральное число N')

# 2-й вариант решения:

# from random import randint
# n = int(input('Введите количество элементов: '))
# lst = [randint(1, n) for i in range(n)]
# print(lst)

# input_set = set(lst)
# num = int(input('Введите искомое число: '))
# dif = 0
# if num > max(input_set):
#     print(max(input_set))
# elif num < min(input_set):
#     print(min(input_set))
# else:
#     while True:
#         if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
#             print(num - dif, num + dif)
#             break
#         elif num - dif in input_set:
#             print(num - dif)
#             break
#         elif num + dif in input_set:
#             print(num + dif)
#             break
#         else:
#             dif += 1    