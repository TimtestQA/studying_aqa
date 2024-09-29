

class Car:

    def __init__(self, brand, model, year = '100'):
        self.brand = brand
        self.model = model
        self.year = year

    def change_year(self,year = None):
        self.year = year


    def get_description(self):
        return f'Марка {self.brand}, Модель {self.model},Год выпуска {self.year}'

    def start_engine(self):
        return 'Двигатель запущен'


class ElectricCar(Car):

    def __init__(self,brand, model, year, battery_capacity):
        super().__init__(brand, model, year)

        self.batterry_capacity = battery_capacity


    def start_engine(self):
        return 'Электродвигатель запущен'

    @property
    def get_battery_info(self):
        return f'Емкость батареи: {self.batterry_capacity} кВтч'


class Truck(Car):
    def __init__(self,brand, model, year,load_capacity):
        super().__init__(brand, model, year)

        self.load_capacity = load_capacity

    @property
    def get_load_info(self):
        return f'Грузоподъемность {self.load_capacity} Тонн'


car = Car(brand='Nissan',model='march',year='2001')
tesla = ElectricCar(brand='Tesla', model='X', year='2024',battery_capacity='1000')
man = Truck(brand='Man',model='Monster',year='2012',load_capacity='10')

print(car.get_description())

print(car.start_engine(),'\n')

print(tesla.get_description())

print(tesla.start_engine())

print(tesla.get_battery_info,'\n')

print(man.get_description())

print(man.get_load_info)

man.change_year(year='2024')

assert man.year == '2024', 'Год не изменился проверь что ты там наделал'
print(man.year,'Год успешно изменен у тебя новая тачка')


