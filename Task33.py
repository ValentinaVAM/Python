# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


from random import randint


def change_my_marks_var1(marks):   # объявляем ф-цию, в которую передаем список оценок
    max_mark = max(marks)   # запоминаем максимальную оценку в списке
    min_mark = min(marks)   # запоминаем минимальную оценку в списке
    marks = [str(i) for i in marks]   # превращаем все элементы списка в строковый тип
    #marks = list(map(str, marks))   #аналог 14 строки
    return ' '.join(marks).replace(str(max_mark), str(min_mark))   # объединяем список в единую строку и заменяем в ней максимальные элементы на минимальные


def change_my_marks_var2(marks):   # объявляем ф-цию, в которую передаем список оценок
    max_mark = max(marks)   # запоминаем максимальную оценку в списке
    min_mark = min(marks)   # запоминаем минимальную оценку в списке
    for i in range(len(marks)):   # проходим по всем элементам списка
        if marks[i] == max_mark:   # если элемент = максимальной оценке...
            marks[i] = min_mark   # ...меняем его на минимальный
    return marks


marks_list = [randint(1, 5) for _ in range(int(input('Введите количество оценок: ')))]
print(*marks_list)
print(change_my_marks_var1(marks_list))   # вызываем первый вариант ф-ции
print(*change_my_marks_var2(marks_list))   # вызываем второй вариант ф-ции

