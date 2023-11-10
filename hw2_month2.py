# # Задача: 1
# # Создайте класс "Транспортное средство" (Vehicle) с атрибутами "brand" (марка) и "model" (модель). 
# # У класса должен быть метод "info()", который выводит информацию о транспортном средстве (марка и модель).
# # Затем создайте подкласс "Автомобиль" (Car), который наследует от класса "Транспортное средство". 
# # В классе "Автомобиль" определите дополнительный атрибут "year" (год выпуска), а также переопределите 
# # метод "info()" для вывода дополнительной информации о годе выпуска автомобиля.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year
    def info(self):
        print(f"Марка - {self.brand}, модель - {self.model} год выпуска - {self.year}")
car = Car ("Mersedes", 's-class', 2002)
car.info()


# Задача: 2
# Создайте три класса: "Родитель" (Parent), "Мама" (Mother) и "Папа" (Father).
# Класс "Родитель" должен содержать атрибуты "first_name" (имя) и "last_name" (фамилия), 
# а также метод "get_full_name()", который возвращает полное имя родителя (имя и фамилию).
# Классы "Мама" и "Папа" должны наследоваться от класса "Родитель". 
# Каждый из этих классов должен иметь свой дополнительный атрибут: "child_count" (количество детей у родителя). 
# Определите метод "get_child_count()" в каждом из классов "Мама" и "Папа", 
# чтобы возвращать количество детей у соответствующего родителя.

class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        print(f"ФИО:{self.first_name} {self.last_name}")
        

class Mother (Parent):
    def __init__(self, first_name, last_name, child_count):
        super().__init__(first_name, last_name)
        self.child_count = child_count

    def get_child_count(self):
        super().get_full_name()
        print (f"Баласынын саны - {self.child_count} ")

    
class Father (Parent):
    def __init__(self, first_name, last_name, child_count):
        super().__init__(first_name, last_name)
        self.child_count = child_count

    def get_child_count(self):
        super().get_full_name()
        print (f"Баласынын саны - {self.child_count} ")
        
mather = Mother("Aigul", "Alymidinova", 2)
mather.get_child_count()
father = Father("Majit", "Bakybaev",3)
father.get_child_count()
