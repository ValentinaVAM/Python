# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:
# 2 4
# 6

def sum_numbers(a, b):
    if a == 0:
        return b
    return sum_numbers(a-1, b+1)


print(sum_numbers(int(input('Введите число a: ')),
      int(input('Введите число b: '))))
