from xmlrpc.client import boolean
#
# Задание 1:
# 1. Исследуйте создание функций в Python с использованием ключевого слова `def`. Напишите примеры функций, решающих следующие задачи:
#   - Функция для вычисления суммы двух чисел.
#   - Функция для нахождения максимального числа в списке.
#   - Функция, которая принимает имя пользователя и выводит приветствие на экран.

def summ(num1,num2):
    summ = num1 + num2
    return summ

def max_digit(list):
    max_in_list = max(list)
    return max_in_list
list_for_test = [9,1,2,3,4]



def privet(*args):
    name = input()
    return f'Привет {name}'
# Задание 2:
# Напишите функцию для покупки билета в кинотеатр, которая будет проверять возраст
# и наличие взрослого сопровождающего, если человеку меньше 18.

def ticket_payment(full_name=None, age=None, adult=False):
    full_name = input('Укажите Имя ')
    age = int(input('Укажите возраст '))
    if age <18 :
        adult = bool(input('''У вас будет сопровождающий 18+?
Будет введите - Да. Не будет, нажмите Enter'''))
        if adult is True:
            return 'Билет продан под присмотром взрослого'
        else:
            return 'Билет продать нельзя'
    elif age > 18 and adult is False:
        return 'Билет продан'
    else:
        return 'Нельзя продать билет'
print(ticket_payment())


# Задание 3:
# 1. Изучите работу с возвращаемыми значениями из функций. Напишите функцию,
# которая принимает список чисел и возвращает новый список, содержащий квадраты этих чисел.

def list_square(list_digit):
    sqare_list = []
    for digit in list_digit:
        digit = digit** 2
        sqare_list.append(digit)
    return sqare_list

print(list_square(list_for_test))