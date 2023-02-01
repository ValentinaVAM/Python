# Задача №13. 
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

from random import randint
days_num = int(input('Введите количество дней: '))
warm_days, max_warm_days = 0, 0
for _ in range (days_num):
    temp = randint(-50, 50)
    print(temp, end= ' ')
    if temp > 0:
        warm_days +=1
    else:
        if warm_days > max_warm_days:
            max_warm_days = warm_days
        warm_days = 0
print()
if warm_days > max_warm_days:
    max_warm_days = warm_days
print(f'Самая длинная оттепель длилась {max_warm_days} дня/дней')
