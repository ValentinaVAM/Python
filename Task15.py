# Задача №15. 
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

melon_num = int(input('Введите количество арбузов: '))
mass_max = mass_min = int(input('Введите массу первого арбуза: '))
for _ in range(melon_num - 1):
    melon_mass = int(input('Введите массу арбуза: '))
    if melon_mass > mass_max:
        mass_max = melon_mass
    elif melon_mass < mass_min:
        mass_min = melon_mass
print(f'Для себя возьми арбуз массой {mass_max}кг, для тещи - арбуз массой {mass_min}кг')