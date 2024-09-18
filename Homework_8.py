# Задание 1:
# Создайте текстовый файл с именем data.txt и наполните его несколькими строками текста.
# Напишите программу, которая открывает файл, читает его построчно и принтит каждую строку.

with open('data.txt', 'r+') as file:
    for line in file.readlines():
        print(line.strip())


# Задание 2:
# Напишите скрипт, который запрашивает у пользователя его имя и возраст, а затем записывает эту информацию в файл userinfo.txt.
# Каждая запись должна быть отдельной строкой в файле.


user_info = [input('Введите Имя: '),':', input('Укажите возраст: ')]
user_info_text = ''.join(user_info)


with open('userinfo.txt', 'a+') as new_user_file:
    new_user_file.write(f'{user_info_text}\n')
    new_user_file.seek(0)
    print(new_user_file.read())
#
# Задание 3:
# Создайте original.txt и запишите в него любую информацию.
# Напишите программу, которая копирует все содержимое файла original.txt в copy.txt.

with open('original.txt', 'r+') as original:
        with open('copy.txt', 'w+') as copy_original:
                copy_original.write(original.read())
                copy_original.seek(0)
