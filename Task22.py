# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
N = int(input('Введите кол-во элементов N множества: ')) 
list_1=[]
for i in range(N):
    list_1.append(randint(1, 10))
set_1 = set(list_1)
from random import randint
M = int(input('Введите кол-во элементов M множества: ')) 
list_2=[]
for i in range(M):
    list_2.append(randint(1, 10))
set_2 = set(list_2)
print(set_1)
print(set_2)
K = set_1.intersection(set_2)
res = sorted(K)
print(*res)