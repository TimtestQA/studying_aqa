# Домашнее задание на тему "Циклы"
#
# Задание 1:
# Создайте пустой список и с помощью цикла 'for' заполните его числами от 0 до 100 (range в помощь).
from itertools import count
#
numerics_list = []
for num in range(0,101):
    numerics_list.append(num)

# Задание 2:
# С помощью цикла `while` необходимо удалять все элементы с конца списка сформированного в первом задании,
# до тех пор, пока общее количество элементов не станет 51. Результат должен получиться следующий [0, 1, 2, ...., 48, 49, 50].

while len(numerics_list) > 51:
    del numerics_list[-1]

print(numerics_list)


# Задание 3:
# Используйте цикл `while` и инструкцию `break` для поиска первого числа, которое делится на 7 без остатка,
# в диапазоне от 1 до 100.

total = 1
while  1 <= total <= 100 :
    if total // 7:
        break
    else:
        print(total)
        total += 1


