# Домашнее задание на тему "Словари в автоматизации":
#
# Задание 1:
# 1. Ознакомьтесь с понятием словарей в Python и узнайте, для чего они используются в автоматизации.
# 2. Создайте словарь `student`, который будет содержать информацию о студенте:
#   - Имя студента (ключ: "name")
#   - Возраст студента (ключ: "age")
#   - Список предметов (type list), которые он изучает (ключ: "subjects")
#   - Средний балл (ключ: "average_score")
# 3. Обновите значение ключа "average_score" в словаре `student` на новое значение (например, 4.75).
# 4. Добавьте новый предмет в список предметов студента (например, "Физика").
# 5. Удалите ключ "age" из словаря `student`, так как эта информация больше не нужна.
# 6. Проверьте наличие ключей "age" и "gender" в словаре `student`. Выведите соответствующее сообщение, если ключ существует или не существует.
# 7. Получите список всех ключей словаря `student` и выведите его на экран.
# 8. Получите список всех значений словаря `student` и выведите его на экран.


student = {
    "name": "Timofey",
    "age": 33,
    "subjekts": [
        "python",
        "seleium"
    ],
    "average_score": 4
}

student ["average_score"] = 4.75
student ["subjekts"].append("physiks")
del student ["age"]

assert "age" in student, "Ключ 'Age'отсутствует в теле"

assert "gender" in student, "Ключ 'gender'отсутствует в теле"

print(student.keys())

print((student.values())


# Задание 2:
# Выполните следующие задания, используя response:
#
# Вывести значение ключа icon из списка trustfactors
# Вывести значение id из campaign
# Проверить, что helpIcon равен False
# Получите значение поля type третьего элемента списка services


response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}

icon_value = response['conditions']["trustfactors"][0]["icon"]
campaign_id_value = response["conditions"]["campaign"]["id"]

print(icon_value, campaign_id_value, sep = "\n")

helpicon_is_false = response["conditions"]["trustfactors"][0]["helpIcon"]

print(services_type_info)


assert False == helpicon_is_false, "helpIcon is not False"

services_type_info = response["services"][2]
