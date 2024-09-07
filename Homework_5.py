# Домашнее задание на тему "Условные операторы и вложенные операторы":
# Задание 1

num = int(input())

print(positive_num = 'Число положительное' if num > 0 else 'Число отрицательное')

if num < 0:
    print('Число отрицательное')
elif num = 0:
    print('Число равно нулю')

num =  int(input())
positive_num = 'Число положительное' if num > 0 else 'Число отрицательное'

print(positive_num)

if num > 0:
    if 0 < num < 10:
        print('Число от 1 до 9')
    elif num >= 10:
        print("Число 10 и больше")
    elif num == 0:
        print('Число равно нулю')

# Задание 2

is_raining = True
is_sunny = True

if is_raining and is_sunny:
    print('дождь при солнце')

is_raining = False
is_sunny = True

if is_raining and is_sunny:
    print('Сегодня солнечная погода, отличный день для прогулки!')

is_raining = True
is_sunny = False

if is_raining and is_sunny:
    print('Сегодня идет дождь, возьмите зонт!')

is_raining = False
is_sunny = False

if is_raining and is_sunny:
    print('Сегодня облачно, но без осадков')